'''
Tuples () : ordered, immutable(unchangeable), 
            allows duplicate elements, contains various data types
'''

# 1) Three ways to define Tuples
myTuple = (3, 1, 4, 6, 3, 'Test', True, 10.1)
myTuple1 = tuple()
customTuple =  'name', 

print(customTuple)
print(10, type(customTuple))

example = 'some random string' ,
# print(example)



# 2) INDEXING -trying to change value in tuple it show error
myTuple[2] = 400
print(myTuple)


# 3) Accessing an element using indexing 
tuple1 = ('Faijan', 'Cats', 'Kittys')
# print(tuple1[2])


# 4) extracting all the items from the tuple using for loop.
# for name in tuple1:
#     print(name)



# 5) Unpacking values from tuples
userDetails = ('John Korah', 48)
a, b = userDetails
print(388888, a)

# 6) extracting with first and last value
firstValue, *otherData,  lastValue = userDetails
# print(f'User details are : Name : {name} \n Age : {age} \n Blood Group : {bloodGroup}')
# print(f'41 : {firstValue} , {lastValue}, {otherData}')


# 7) geting length of tuple  
fruits =  ('a', 'p', 'p', 'l', 'e')
# print(len(fruits))

# 8) Occurrences of item in the tuple
# print(fruits.count('x'))


# 9)find the index of the element in the tuple
print(fruits.index('p'))



fruits =  ('a', 'p', 'p', 'l', 'e')
# 10) accessing values using slicing
slicedData = fruits[2 : 5]
print(61, slicedData)

 
hoppedData = fruits[ : ]
print(hoppedData)
