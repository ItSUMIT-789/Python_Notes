# Sets {} : unordered, mutable, no duplicate , and contains various data types

# 1) Initialization
mySet = {2, 3, 4, 4, 4, 4, 4, 4, 4,  'True', 1 , 4, 5, 6}
mySet1 = set()

# 2) Don't init empty set b'caz it will consider it as dictionary
emptySet = {}


mySet1.add(7)
mySet1.add(2)
mySet1.add(4)
mySet1.add(7)
mySet1.add(3)
mySet1.add(1)

# [1, 2, 3, 4, 7]

print(mySet1)

mySet1.remove(7)
# mySet1.remove(1)

print(mySet1)
mySet1.pop() # it always removes the first element and returns the removed element.
mySet1.pop() # it always removes the first element and returns the removed element.
mySet1.pop() # it always removes the first element and returns the removed element.

print(mySet1)



# 3) What if we try to remove the element which does not exists in the set ?
# mySet1.remove(19) # keyError : key does not exist in 

# is there a way to overcome this error thing ?

mySet1.discard(19) 

mySet1.clear()

print(mySet1)
print('execution completed.')



