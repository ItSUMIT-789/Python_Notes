# syntax : map(func, iterable)


#--- by using normal function
def someFunction(value):
    if value == 2 :
        return value + value
    return None

print(list(map(someFunction, [1, 2, 3])))


#-- by using lambda
#                  lambda function syntax => lambda arguments : expression

# lambda value : value + value
print(list(map(lambda value:  value + value if value == 2 else ' ' , [1, 2, 3])))
# without raoing the map in list it show the memory location of result



