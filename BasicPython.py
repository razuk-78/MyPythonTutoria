'''
 * tools:
    * pep python style code checker
    * pip a CLI package manager, used to install packages
*under score:
    * "__var__"/"dunder function" double underscore meaning https://dbader.org/blog/meaning-of-underscores-in-python
    * "_var"  single underscore as prefix meaning means the var is private.
    * "__var" lets python interpreter assign some hashcode to similer var in the subclass to avoid conflict
    * "_" single underscore means this var is temperory or trivial.
* star/doublestars:
  */** prefix a function parameter:
      * func(*arg) means argument type of list.
      * func(**arg) means argument type of dictionary.
 * keywords:
    * self keyword meaning "this in c# for example"
    * with keyword means "using keyword in c# using(some disposable class)"
    * cls used as argument forstatic method
    * yield
 * useful console functions:
    * dir(module/class) list all function members try it in console.
    * help(module/class) shows document related to class/module try it in console.
* function type private, static, public

* attrebutes

* inheritence:
   * the parent fields are not deliverd to the subclass
'''

import sys
import os
print("from os.path "+os.path.abspath(os.path.join('MyLib')))
sys.path.append(os.path.abspath(os.path.join('MyLib')))
from ExampleClass import *
# useing system path to add referance to a module/library
# inheritance example:      



if __name__ == "__main__":
   #inheritance example
