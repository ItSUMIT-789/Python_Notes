# Todo app
# add
# modify/update
# delete
# search 

Todos = ['buy groceries', 'buy shoes'] # to store the todos

def addTodo():
    text = input('Please enter a todo : ')
    Todos.append(text)

def showTodos():
    for index, todo in enumerate(Todos):
        print(index, todo)

def updateTodos():
    index = int(input('please enter a index value : '))
    newText = input("please enter a new todo: ")
    Todos[index] = newText


while True:
    print('please enter a choice \n1. add todo \n2. show todos \n3.update todos \n4. exit ')
    choice = int(input())
    if choice == 4:
        break 

    if choice == 1:
        addTodo()

    if choice == 2:
        showTodos()

    if choice == 3:
        updateTodos()




