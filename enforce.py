#!/usr/bin/env python3

'''
name: enforce.py 
desc: edit check for data format. Aborts job is data is improper
usage: 1. Add import enforce to top of python script.
       2. Call specific check based on the format of your data.
       Examples:
       Integer.check(1)
Float.check(2.0)
Positive.check(3)
String.check('4')
NotEmpty.check(5)
'''

import sys
script_name = sys.argv[0]

#----------------------#
class Enforce():
#----------------------#
    @classmethod
    def check(cls, value):
        pass
#----------------------#
class Typed(Enforce):
#----------------------#
    type = None
    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f'Aborting, {script_name} expected {cls.type}'

#----------------------#
class Integer(Typed):
#----------------------#
    type = int

#----------------------#
class Float(Typed):
#----------------------#
     type = float

#----------------------#
class String(Typed):
#----------------------#
    type = str

#----------------------#
class Positive(Enforce):
#----------------------#
    @classmethod
    def check(cls, value):
        assert  value > 0, 'Enforce.py expecting number > 0'

#----------------------#
class NotEmpty(Enforce):
#----------------------#
    @classmethod
    def check(cls, value):
        assert(len(str(value)) > 0), 'Enforce.py expecting argument to be read in.'
        super().check(value)

########################
# M A I N   L O G I C
########################
Integer.check(1)
Float.check(2.0)
Positive.check(3)
String.check('4')
NotEmpty.check(5)

