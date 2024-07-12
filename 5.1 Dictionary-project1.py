# CRUD > Create, Retrive, Update, Delete 

usersData = [] # empty list to contain all users data
# test = {'user': 'faijan', 'gmail': 'faijan@gmail.com', 'phonenumber': '1234'}
# test['gmail']



def create():
    # create
    userDataDict = {}
    username = input("Enter your username : ")
    email = input("Enter your email address : ")
    contact = input("Enter your contact : ")
    userDataDict['user'] = username
    userDataDict['gmail'] = email
    userDataDict['phonenumber'] = contact
    usersData.append(userDataDict)

def retrive():
    count = 1
    for user in usersData:
        print(f' {count}. {user}')
        count += 1

def update(index, gmail):
    usersData[index-1]['gmail'] = gmail
    print('one record updated.')

def delete(index):
    del usersData[index-1]

while True:
    choice = int(input('1. Create 2. Retrive 3. Update 4. Delete : '))

    if choice == 1:
        create()

    if choice == 2:
        retrive()
    
    if choice == 3:
        index = int(input("please provide the index value : "))
        gmail = input('please enter the new email : ')
        update(index, gmail)

    if choice == 4:
        index = int(input('please provide the index value : '))
        delete(index)

