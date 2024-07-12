# syntax : filter(func, iterable)


#--- by using normal function

def filterValue(value):
    if value == 2:
        return value
    

print(list(filter(filterValue, [1, 2, 3, 4])))

#-- by using lambda
#                  lambda function syntax => lambda arguments : expression

print(list(filter(lambda x: x == 2, [1, 2, 3, 4])))
