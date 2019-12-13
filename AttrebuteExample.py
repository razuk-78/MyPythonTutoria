'''
* attrebutes/decorators
'''
#decorator without argument
#it will modify the return of client function
#client function without args
def function_decor_without_args(func):
    def  wrapper():
        return func().upper()       
    return wrapper
@function_decor_without_args
def test_decorator_attr_without_args(): 
    return "from test_decorator_attr_without_args() -> to upper case"  


#decorator without argument
#it will modify the return of client function
#client function with args
##############################################
def function_decorator_clientFunction_with_args (func):
    def wrapper(val):
        return func(val).upper()
    return wrapper
@function_decorator_clientFunction_with_args    
def test_clientFunction_with_args(val):
    return val #-> to upper case

#decorator with argument
###############################################
def function_decorator_with_args(atter_val):
    def decorator(func):
        def wrapper(func_val):
            func_val=atter_val + func_val
            return func(func_val)
        return wrapper
    return decorator

@function_decorator_with_args('decorator_value + ')
def test_decorator_with_args(val):
    return val


#print(fun(1, 1))
################################################
def time_this(original_function):                         
    def new_function(*args,**kwargs):
        print("starting timer")       
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print("Elapsed Time = {0}".format(after-before))      
        return x                                             
    return new_function

# class decorator/attribute
def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self,s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to 
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and 
            the attribute is an instance method then `time_this` is applied.
            """
            try:    
                x = super(NewCls,self).__getattribute__(s)
            except AttributeError:      
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return time_this(x)                 # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls

@time_all_class_methods
class Foo(object):
    def __init__(self, *args, **kwargs):
        print("from instance")
        super().__init__(*args, **kwargs)
    def a(self):
        print("entering a")
        import time
        time.sleep(3)
        print("exiting a")

#oF = Foo()
#oF.a()
if __name__ == "__main__":
    # test atter without parameter
    print(test_decorator_attr_without_args())
    # test atter with parameter
    print(test_clientFunction_with_args("from test_decorator_attr_with_args()"))
    # test decor with args
    # inject decorator args in function body
    print(test_decorator_with_args("client_func_value"))
    # test class atter
    oF = Foo()
    oF.a()





