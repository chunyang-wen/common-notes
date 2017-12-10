#!/usr/bin/env python
# coding: utf-8
# author: chengfu.wcy(chengfu.wcy@antfin.com)

class _RouteClassAttributeToGetattr(object):
    def __init__(self, fget=None):
        self.fget = fget

    def __get__(self, instance, ownerclass=None):
        if instance is None:
            raise AttributeError()
        return self.fget(instance)

    def __set__(self, instance, value):
        raise AttributeError('cant set attribute')

    def __delete__(self, instance):
        raise AttributeError('cant delete attribute')

def _is_descriptor(obj):
    """Returns True if obj is a descriptor, False otherwise."""
    return (
            hasattr(obj, '__get__') or
            hasattr(obj, '__set__') or
            hasattr(obj, '__delete__'))

class _NameDict(dict):
    '''A dict that only supports name without prefix of "_" or "__"'''

    def __init__(self):
        super(_NameDict, self).__init__()
        self._member_names = []

    def __setitem__(self, key, value):
        if key.startswith('_') or key.startswith('__'):
            pass
        elif not _is_descriptor(value):
            self._member_names.append(key)
        super(_NameDict, self).__setitem__(key, value)

Enum = None

class EnumMeta(type):
    '''EnumMeta'''
    @classmethod
    def __prepare__(mcs, cls, bases):
        return _NameDict()

    @staticmethod
    def _get_mixins(bases):
        if not bases or Enum is None:
            return object, Enum

        member_type = first_enum = None
        if not issubclass(bases[0], Enum):
            member_type = bases[0]
            first_enum = bases[-1]
        else:
            for base in bases[0].__mro__:
                if issubclass(base ,Enum):
                    if first_enum is None:
                        first_enum = base
                else:
                    if member_type is None:
                        member_type = base
        return member_type, first_enum

    @staticmethod
    def _find_new_(classdict, member_type, first_enum):
        __new__ = classdict.get('__new__', None)
        if __new__:
            return None, True, True

        N__new__ = getattr(None, '__new__')
        O__new__ = getattr(object, '__new__')
        if Enum is None:
            E__new__ = N__new__
        else:
            E__new__ = Enum.__dict__['__new__']
        for method in ('__member_new__', '__new__'):
            for possible in (member_type, first_enum):
                try:
                    target = possible.__dict__[method]
                except (AttributeError, KeyError):
                    target = getattr(possible, method, None)
                if target not in [None, N__new__, O__new__, E__new__]:
                    if method == '__member_new__':
                        classdict['__new__'] = target
                        return None, False, True
                    if isinstance(target, staticmethod):
                        target = target.__get__(member_type)
                    __new__ = target
                    break
            if __new__ is not None:
                break
        else:
            __new__ = object.__new__
        if __new__ is object.__new__:
            use_args = False
        else:
            use_args = True
        return __new__, False, use_args

    def __new__(mcs, cls, bases, classdict):

        if type(classdict) is dict:
            origianl_dict = classdict
            classdict = _NameDict()
            for k, v in origianl_dict.iteritems():
                classdict[k] = v

        member_type, first_enum = mcs._get_mixins(bases)
        __new__, save_new, use_args = mcs._find_new_(classdict, member_type, first_enum)
        
        print 'save_new: ', save_new, ' use_args: ', use_args
        # All enum members, will construct for each of them
        members = dict((k, classdict[k]) for k in classdict._member_names)
        for name in classdict._member_names:
            del classdict[name]
        base_attributes = set([a for b in bases for a in b.__dict__])

        enum_class = super(EnumMeta, mcs).__new__(mcs, cls, bases, classdict)
        enum_class._member_names = []

        enum_class._member_map_ = {}
        enum_class._value2member_map_ = {}

        enum_class._member_type_ = member_type

        if __new__ is None:
            __new__ = enum_class.__new__

        print 'members: ', members
        for name in members.keys():
            value = members[name]
            print 'name: ', name, ' value: ', value
            if not isinstance(value, tuple):
                args = (value,)
            else:
                args = value
            if member_type is tuple:
                args = (args,)
            if not use_args or not args:
                enum_member = __new__(enum_class)
                if not hasattr(enum_member, '_value_'):
                    enum_member._value_ = value
            else:
                enum_member = __new__(enum_class, *args)
                if not hasattr(enum_member, '_value_'):
                    enum_member._value_ = member_type(*args)
            value = enum_member._value_
            enum_member._name_ = name
            enum_member.__objclass__ = enum_class
            enum_member.__init__(*args)
            enum_class._member_names.append(name)

            setattr(enum_class, name, enum_member)
            enum_class._member_map_[name] = enum_member
            enum_class._value2member_map_[value] = enum_member

        return enum_class

    def __getitem__(self, key):
        return self._member_map_[key]


tempdict = {}

def __new__(cls, value):
    if type(value) is cls:
        value = value.value
    if value in cls._value2member_map_:
        return cls._value2member_map_[value]
tempdict['__new__'] = __new__
del __new__

@_RouteClassAttributeToGetattr
def name(self):
    return self._name_

@_RouteClassAttributeToGetattr
def value(self):
    return self._value_

tempdict['name'] = name
tempdict['value'] = value
del name
del value
Enum = EnumMeta('Enum', (object,), tempdict)
