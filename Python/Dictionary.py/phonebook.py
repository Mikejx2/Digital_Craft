import pickle

# with open('phonebook.pickle', 'wb') as fh:
#     pickle.dump(phonebook, fh)

with open('phonebook.pickle', 'rb') as fh:
    phonebook = pickle.load(fh)


# Main

userInput = ""







#function
def dumpPickle():
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook, fh)
def find():
    findName = input("Name: ")
    findPerson = phonebook[findName]
    print(f"Phone Number: {findPerson}")
    print(f"Found entry for {findName}")

def add():
    newName = input("Name: ")
    newNumber = input("Phone Number: ")
    phonebook[newName] = newNumber
    dumpPickle()
    print(f"Entry stored for {newName}")

def delete():
    delName = input("Name: ")
    del phonebook[delName]
    dumpPickle()
    print(f"Deleted entry for {delName}")

def displayAll():
    print( phonebook)
quitProgram = "5"


while quitProgram == "5":
    userInput = input('''
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)? ''')
    choice = userInput
    if choice == "1":
        find()
    elif choice == "2":
        add()
    elif choice == "3":
        delete()
    elif choice == "4":
        displayAll()
    elif choice == "5":
        print("Bye.")
        break
    else:
        print("Invaild selection!")
