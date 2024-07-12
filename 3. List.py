# List [] : in python, it is a collection of items that are 
#           ordered and mutable(changeable) , 
#           allows duplicate and 
#           contains various data types.

# Initialization
variables = [1, 4, 4, 'John', 1.1, True]
print(variables)

#List wrapping
my_list = list([1, 2, 2, 4, 'John', 1.1, True])
print(my_list)

#LIST METHODS

#1)append : it adds a new item to the end of the list.
fruits = []

fruits.append('mango')
fruits.append('banana')
fruits.append('pineapple')
fruits.append('watermelon')
fruits.append('guava')
fruits.append('orange')
fruits.append('cherry')
fruits.append('strawberry')
fruits.append('raspberry')



# 2) pop : it removes the last item/element from the list & pop returns the removed item.
removed_element = fruits.pop()
print(f'item {removed_element} has been removed.')
print(fruits)

# 3) Remove : it removes the specified element

print(f'before removing element from the list {fruits}')
fruits.remove("cherry")
print(f'after removing element from the list {fruits}')


# 4) Merging : it takes extra space
vegetables1 = ['tomato', 'carrot', 'cauliflower', 'broccoli', ]
vegetables2 = ['potato', 'pumpkin', 'onion', 'garlic']

vegetables = vegetables1 + vegetables2
print(vegetables)

# 5)Extend : extend another list into the existing list
vegetables2.extend(vegetables1)
print(vegetables2)

'''
# 6)Copying a list-
                    .copy Method
                    list(variable)
                    slicing [ : ]
'''
# 6--1).copy Method
original_list1 = [1, 2, 3, 4]
copy_list1 = original_list1
print(copy_list1)
copy_list1[2] = 300
print(copy_list1)
print(f'original list1 is {original_list1}')

# 6--2)list(variable)
original_list2 = [5, 6, 7, 8]
copy_list2 = original_list2
print(copy_list2)
copy_list2[2] = 400
print(copy_list2)
print(f'original list2 is {original_list2}')

# 6--3)slicing [ : ]
original_list3 = [9, 10, 11, 12]
copy_list3 = original_list3
print(copy_list3)
copy_list3[2] = 500
print(copy_list3)
print(f'original list3 is {original_list3}')

# 7)Accessing list through For loop
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
for day in weekdays:
    print(day)

# 8)Reverse a list
months = ['january', 'february', 'march', 'april', 'may', 'june' , 'july' , 'august' , 'september'] 
months.reverse()
print(months)

# 9)Sorting a list
numbers = [1, 6, 3, 5, 2, 7, 0, 4]
numbers.sort()
print(numbers)

# 10)Clear Method
numbers1 = [1, 6, 3, 5, 2, 7, 0, 4]
numbers1.clear()
print(numbers1)


