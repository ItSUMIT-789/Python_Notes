# Generators
'''
    1.  They are simple way of creating iterators , all the work we have done 
            is handled by generators.
    2.  They are easy to implement: we must have to create a function that
            return element with yield instead of return.
    3.  They can contain one or more yeild statements
    4.  When called, it returns an object(iterator) but does not start execution
        immidiately
    5.  Once the function yeilds, the function is paused and the control is 
        transferred to the caller
    6.  Local variables and their state are remembered between successive calls.

'''

def power_of_two(number):
    for n in range(number + 1):
        yield 2**n


power = power_of_two(5)

print(f'''{next(power)}      
{next(power)}
{next(power)}
{next(power)}''')
# OR
print(next(power) )


#  Generators can be used in for loop directly. This will save memory as generator
for i in range(100):
    print(i)

print('this is from generators', next(power))





