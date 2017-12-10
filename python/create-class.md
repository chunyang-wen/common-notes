### Dynamic create class in `Python`

[Reference](https://stackoverflow.com/questions/5924879/how-to-create-a-new-instance-from-a-class-object-in-python)

#### Difference of `__new__` and `__init__`

`__new__` only works with new class which inherits from `object`. It is responsible for allocating
memory and return the created instance

```python
def __new__(clas, *args, **kwargs):
    return object.__new__(*args, **kwargs)
```

When we call `a = A()`, it will first call `__new__` and then send the create instance to the first
argument of `__init__`

#### create a class using `type`

```python
ClassName = type('ClassName', (Base1, Base2), class_dict)

class Meta(type):
    @classmethod
    def __prepare__(mcs, cls, bases):
        pass
    def __new__(mcs, cls, bases, classdict):
        pass
```
