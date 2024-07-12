'''
# string : ordered, immutable, text respresentation
'''


# 1) Initialize
string = 'Hello World !'
print(string)

# 2) Accessing the characters
char = string[3]
print(char)

# 3) Cant access characters
string[3] = 'f' # error string object doest not support item assignment 
# print(string)

# 4) String concatenation
greeting = 'hello'
name = 'user'
final_msg = greeting + ' ' + name
print(final_msg)

# 5) Iterating over every letter
sentence = 'This is a random sentence written by EDITOR'
print(sentence.lower())
if 'editor' in sentence.lower():
    print('pattern found.')
else:
    print('pattern not found.')


# 6) Strip method
my_string = '           this is USER EXAMPLE              '
print(my_string.lstrip()) # lstrip is use for removing left side whitespaces
print(my_string.rstrip()) # rstrip is use for removing right side whitespaces
print(my_string.strip()) # strip is use for removing both side whitespaces

# 7) Joint method
my_list = ['A'] * 6
print(my_list) # ['a', 'a', 'a', 'a', 'a', 'a']
my_string_ = ",".join(my_list)
print(my_string_)


