#range() function
range(1,5)
list(range(4))
#>>> [0,1,2,3]

#delegate function
def fun(dfun):
    for target_list in range(0,5):
        dfun(target_list)

def funb(data):
    print(data)
#-------------------------------------------------#
"""
Special parameters¶
By default, arguments may be passed to a Python function
either by position or explicitly by keyword.
For readability and performance,
it makes sense to restrict the way arguments can be
passed so that a developer need only look at the function
definition to determine if items are passed by position,
by position or keyword, or by keyword.
"""
def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
#The keyword isn't critical
standard_arg(arg=2)
#or
standard_arg(2)
#>>> 2
#The keyword is critical
kwd_only_arg(arg=5)
#will cast Error
# kwd_only_arg(5)
#>>> takes 0 positional arguments but 1 was given
#position only
pos_only_arg("position only")
#>>> position only
#will cast Error
#pos_only_arg(arg="position only")
#-----------------------------------------#

def foo(**kwds):
    print(kwds)
foo(name="alias",age=10)
#>>> {'name': 'alias', 'age': 10}
def foo(*kwds):
    print(kwds)
foo("alias",10)
#>>> ('alias', 10)
"""
Lambda Expressions¶
Small anonymous functions can be created with the lambda keyword.
 This function returns the sum of its two arguments:
lambda a, b: a+b. Lambda functions can be used wherever
function objects are required. They are syntactically
restricted to a single expression. Semantically,
they are just syntactic sugar for a normal function
definition. Like nested function definitions,
lambda functions can reference variables from the containing scope
"""