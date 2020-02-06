'''
* self
* cls
* help_func
* dir_fun
* static
* private function should be prefixed with _var
* dunder_func
* string interpolation prefix with f"{object}"
* meta data
'''

class KeyWord:
  #way to metadata to a func, some description
  def  __init__(self, id:'number', name:'string') -> 'construct':
      self.id = id
      self.name = name
  #use this attr to make static func
  @staticmethod
  def static_func_print():
      print("from static_func_print()")

  
 ##################class method####################
  #used to create a new instance of the object,
  # since it recieves a cls as parameter
  #used as constructor same as __init__(self)
  #this func could accessed as static method
  @classmethod
  def construtor_func(cls, id, name):
      return cls(id, name)
  @classmethod
  def access_fields_from_cls(cls) ->'void':
     # print(f"name from cls: {cls.name}") this will rais an error
     #can't access object's memeber from cls, access only static member
     cls.static_func_print()

 #####################dunder function##################
  #dunder function shouldn't be called directaly
  #some of them represent operators like"+, -, *, /, =, ..."
  #some of them used by other system function
  def __gt__(self, value):
      if self.id > value.id:   
            return True
      return False

  def __add__(self, other):
      return self.id + other.id

  def print(self):
      print(f"id: {self.id}   name: {self.name}")


def func_arg_as_array(*args):
    print(f'from func_array_dic_as_*args: {args}')
def func_arg_as_dic(**args):
    print(f'from func_array_dic_as_**args: {args}')
#--------------------------------------------------------------
#function argument passing types'
#positional passing 
def positional_passing(pos1, pos2, /):
    print( pos1 + pos2)
def keyWord_passing(*,kwd1,kwd2):   
    print(kwd1+kwd2)
def standard_passing(arg):
    print(arg)
if __name__ == "__main__":
    #print from static method
    KeyWord.static_func_print()

    #create an object instance from construct_func
    keyword1 = KeyWord.construtor_func(10,"from construct method")
    keyword1.print()
    KeyWord.access_fields_from_cls()

    #test dunder funtion __ge__ wich is greater than
    key1 = KeyWord(10,"key1")
    key2 = KeyWord(11,"key2")
    print(f"from dunder func: {key1 + key2}")
    print(f"from dunder func: {key1 < key2}")
    
    #function dir(object) used to list all object member
    '''print(dir(KeyWord))'''
    # function help(object) used to show object document
    '''print(help(KeyWord))'''
    #takes any number of args e.g: val1, val2, ... 
    func_arg_as_array(['a','b'],"val1", {'key':'val'})
    #takes args in form of dic key=value
    func_arg_as_dic(key1=["a","b"],key2={"key":"val"}, key3="val3")
    #-------------------------------------------------------------------------
    #position only
    #positional_passing(pos1="pos1", pos2="pos2")-> will cast error
    positional_passing("position_", "passing")

    #keyword only
    #keyWord_passing("first", "second")-> will cast error
    keyWord_passing(kwd1="keyword_", kwd2="Passing")
    #standard passing
    standard_passing("standard_passing")
    standard_passing(arg="standard_passing")
    
