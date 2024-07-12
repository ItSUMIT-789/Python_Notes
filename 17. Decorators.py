''' 
#     decorators can change/add/modify the functionality of the function      #

# we have already done this with functionalities like 'filter' and 'map'
# such functions are called 'Higher order functions' (HOF)
# decorator always takes function as an argument
# HOF can return a function
# Decorators in simple terms, take a function, adds some extra functionality
# and returns a function
'''
# example  \/
# filter(lambda x  : x == 2 , [1, 2, 3])
# map(lambda x : x , [1, 2, 3])


# 1)
# def custom_filter_function(func):
#     def child():
#         print('this is start of custom filter function')
#         func()
#         print('this is an end of custom filter function')
#     return child

# def test():
#     print('Testing')

# decorated_filter_function = custom_filter_function(test)

# print('Decorated filter function', decorated_filter_function)
# print('*' * 100)



# 2)

def outer(function):
    def inner():
        print('I am decorated function')
        function()
    return inner

@outer
def hello_world():
    print('hello world with decorators')



# 3)

# def outerFunction(function):
#     def innerFunction(num1, num2):
#         if num2 == 0:
#             print('We can"t divide with zero')
#             return
#         else:
#             return function(num1, num2)
#     return innerFunction

# @outerFunction
# def divide(a, b):
#     return a / b

# divide(1, 0)