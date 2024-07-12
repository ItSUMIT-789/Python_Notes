'''
    Python Closures

    There are three things we need in order to have a closure.

    1. we must have a nested function.
    2. the nested function must refer to a value defined in the enclosing function
    3. the enclosing function must return the nested function


'''
# 1) Exampal 1  - It show the error 
def parent(value):
    total = 1000
    total = total - value
    print(f'{value} amount has been debited now your current account balance is ${total}')

clone_parent = parent(400)
del clone_parent
clone_parent()

# 1) Exampal 2
def print_msg():
    total = 100000
    def printer(value):
        nonlocal total
        total = total - value
        print(f'{value} amount has been debited now your current account balance is ${total}')
    return printer

hidden_function = print_msg()
del print_msg

hidden_function(10000)
hidden_function(2500)
hidden_function(4000)
hidden_function(500)
hidden_function(5000)






