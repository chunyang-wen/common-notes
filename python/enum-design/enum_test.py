#!/usr/bin/env python
# coding: utf-8
#****************************************************************#
# ScriptName: enum_test.py
# Author: chengfu.wcy@alibaba-inc.com
# Create Date: 2017-12-09 16:31
# Modify Author: chengfu.wcy@alibaba-inc.com
# Modify Date: 2017-12-09 16:31
# Function:
#***************************************************************#

import enum
class Car(enum.Enum):
    A = 1
    B = 2

print dir(Car)
#print Car.name
print Car.A.name

print Car.B.value

print Car['A'].name
