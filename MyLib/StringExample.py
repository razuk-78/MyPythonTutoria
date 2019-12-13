'''
* string formatter

'''
#old style
def func_string_formatter_old_style(val):
    return 'old style string format: %s' %val
#use the %x format specifier to convert an int value to a string and,
#  to represent it as a hexadecimal number:
def func_string_formatter_convert_int_to_string(string, num):
    return 'string value %s:  int to hex value %x'%(string, num)

def fun_string_formatter_3(string, num):
    return "string value: %(string)s, number value: %(num)x" % {"string": string, "num": num }

if __name__ == "__main__":
    print(func_string_formatter_old_style('some value'))

    #
    print(func_string_formatter_convert_int_to_string('some value', 9999))

    #
    print(fun_string_formatter_3("some value", 999))