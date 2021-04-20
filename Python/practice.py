#  CRUD - create, read, update, delete
finished = 'y'
todoList = []
# add
def add():
    newTodo = input("Enter a new todo Item: ")
    todoList.append(newTodo)
# displaying
def display():
    for index, todoItem in enumerate(todoList):
        print(f"{index + 1} {todoItem}")
# updating
def update(index, updatedValue):
    updatedValue = input("Enter updated item: ")
    todoList[index] = updatedValue
# deleting
def delete():
    delItem = int(input("What do you want to delete? "))
    del todoList[delItem - 1 ]
while finished == 'y':
    # menu
    print('what would you like to do?')
    userInput = input(f"""
1. List todos
2. Add a todo item
3. Delete a todo item
4. update a todo item
5. end the app                                 
""")
    choice = int(userInput)
    if choice == 1:
        display()
    elif choice == 2:
        add()
    elif choice == 3:
        delete()
    elif choice == 4:
        update()
        finished = 'n'

        