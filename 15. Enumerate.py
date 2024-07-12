'''
Enumerate -- a built-in function that allows you to iterate through a sequence and keep track of the index of each element.

'''
userData = ['John', 'Bob', 'Michael', 'Vito', 'Max']


# Enumerate each name in the userData list and print the index and name.
#     \/    \/
for index, name in enumerate(userData):
    print(f'{index+1} : {name}')

