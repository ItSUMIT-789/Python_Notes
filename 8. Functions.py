# Functions 
#       a function is declared using the 'def' keyword followed by the function name and parentheses containing 
#      any parameters the function may take.

# 1) Default function
def farewell():
     print('farewell users')

# 2) Parameterized function
def farewellUser(user):
    print(f',byeeee {user}')


farewell()

name = 'abc'
farewellUser(name)


# 3) Higher order functions : These are functions that can take other functions as arguments 
#                         and/or return functions
 

def apply_func(func, value):
    return func(value)

def square(value):
    return value * value 

apply_func(square, 4)

# 4) Nested functions
def parent():
    print("some statement from parent")

    def child1():
        print('some statement from child 1 ')

    def child2():
        print('some statement from child 2')

    child1()
    child2()

parent()

