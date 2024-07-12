usersData = []

def create():
    userDictionary = {}
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    userDictionary['name'] = name
    userDictionary['email'] = email
    userDictionary['password'] = password
    usersData.append(userDictionary)
    print("User created successfully!")

def retrieve():
    if not usersData:
        print("No users found.")
    else:
        for count, user in enumerate(usersData, start=1):
            print(f'{count}. {user}')

def update(index, new_email):
    if 0 < index <= len(usersData):
        usersData[index - 1]['email'] = new_email
        print('One record updated.')
    else:
        print("Invalid index.")

def delete(index):
    if 0 < index <= len(usersData):
        del usersData[index - 1]
        print("User deleted successfully.")
    else:
        print("Invalid index.")

def search_by_email(email):
    for user in usersData:
        if user['email'] == email:
            print(f'User found: {user}')
            return
    print("No user found with that email.")

def change_password(index, new_password):
    if 0 < index <= len(usersData):
        usersData[index - 1]['password'] = new_password
        print("Password updated successfully.")
    else:
        print("Invalid index.")

def list_all_emails():
    if not usersData:
        print("No users found.")
    else:
        for count, user in enumerate(usersData, start=1):
            print(f'{count}. {user["email"]}')

while True:
    try:
        choice = int(input('1. Create 2. Retrieve 3. Update 4. Delete 5. Search by Email 6. Change Password 7. List All Emails 8. Exit: '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue

    if choice == 1:
        create()
    elif choice == 2:
        retrieve()
    elif choice == 3:
        try:
            index = int(input("Please provide the index value: "))
            new_email = input('Please enter the new email: ')
            update(index, new_email)
        except ValueError:
            print("Invalid input. Index should be a number.")
    elif choice == 4:
        try:
            index = int(input('Please provide the index value: '))
            delete(index)
        except ValueError:
            print("Invalid input. Index should be a number.")
    elif choice == 5:
        email = input('Please enter the email to search: ')
        search_by_email(email)
    elif choice == 6:
        try:
            index = int(input("Please provide the index value: "))
            new_password = input('Please enter the new password: ')
            change_password(index, new_password)
        except ValueError:
            print("Invalid input. Index should be a number.")
    elif choice == 7:
        list_all_emails()
    elif choice == 8:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")





        




