# Dictionary {} : 'key'- value pair, ordered, mutable, 
#                 does not allow duplicate keys,
#                 and contains various data types.


# 1) define
userDetails = {
        'username': "JohnK",
        'name':"John korah", 
        'age':48, 
        'nationality':False, 
        'blood':'O+',
        'height': 5.11,
}
dictionary_ = dict(name='faijan', age=24)

# 2)Accessing value of the dict normal way
# print(userDetails['height'])

# For loop

#       for key in userDetails: # when we dont specify the items it considers keys
#           print(key)

#       for value in userDetails.values(): # we can specify values if we want values
#            print(value)


# what if i want both ? then we use items()
# for data in userDetails.items():
#     print(33, data)
#     key, value = data 
#     print(34, key, value)




simpleExample = { 'name':"Bob" , 'age':20 }
print('==>', simpleExample['age'])


# something is 
# something is ('age', 20)
for key in simpleExample:
     print(key, simpleExample[key])  #another simple way





