#!/usr/bin/env python3

'''
name: enforce.py 
desc: Pre-processing data edit check for data format. Aborts job is data is improper.
      Appearing to be redundant in functionality, this was intended 
      to be baked into Test Driven Design, as a supplement for data
      edits, prior to actual processing, that, and I am a beginner,
      so please "flame" lightly, I am still learning to be pythonic.
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
        assert  value > 0, (script_name, 'expecting number > 0')

#----------------------#
class NotEmpty(Enforce):
#----------------------#
    @classmethod
    def check(cls, value):
        assert(len(str(value)) > 0), (script_name, 'expecting argument to be read in.')
        super().check(value)

#----------------------#
class IsUpper(Enforce):
    @classmethod
    def check(self,name):
        self.name = name
        assert (str(self.name).isupper() ==True), (script_name, "expecting all UPPERCASE. You sent:", self.name)

           
########################
# M A I N   L O G I C
########################
Integer.check(1)
Float.check(2.0)
Positive.check(3)
String.check('4')
NotEmpty.check(5)
IsUpper.check("JOHN")

