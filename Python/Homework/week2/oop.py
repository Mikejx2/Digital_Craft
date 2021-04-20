
# class Button():
#     def __init__(self, color, height, width):
#         self.count = 0
#         self.color = color 
#         self.height  = height 
#         self.width = width
#     def click(self):
#         self.count += 1
# navButton = Button('green', '100px', '200px')
# helpButton = Button('yellow', '50px', '25px')
# navButton.click()
# navButton.click()
# navButton.click()
# navButton.click()
# print(f'nav: {navButton.count} help: {helpButton.count}')
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# print(f'nav: {navButton.count} help: {helpButton.count}')


# **********************************************************************

# class Students:

#     def __init__(self, first, last):
#         self.firstName = first
#         self.lastName = last
        

#     def greeting(self, name):
#         print(f"{self.firstName} {self.lastName} says good Morning {name}")

# sam = Students("sam", "hope")
# mike = Students("mike", "will")
# fred = Students("fred", "green")
# v = Students("v", "thomas")
# matt = Students("matt", "smith")

# sam.greeting("adam")
# mike.greeting("danni")
# fred.greeting("ericka")
# v.greeting("james")
# matt.greeting("dale")


# **********************************************************************
# Write code to

# -Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# -Have sonny greet jordan using the greet method.
# -Have jordan greet sonny using the greet method.
# -Write a print statement to print the contact info (email and phone) of Sonny.
# -Write another print statement to print the contact info of Jordan.

# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
    
#     # def greet(self, other_person):
#     #     print(f'Hello {self.name}, I am {other_person}!')

#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))


# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan","jordan@aol.com", "495-586-3456")

# jordan.greet(sonny)

# sonny.greet(jordan)

# print(f"{sonny.name} Email: {sonny.email} Phone Number: {sonny.phone}")

# print(f"{jordan.name} Email: {jordan.email} Phone Number: {jordan.phone}")


# **********************************************************************

# class CrazyString(str):
#     def __init__(self, word):
#         self.word = word

#     def reverse(self):
#         revString = ""

#         for char in self.word:
#             revString = char + revString

#         return revString    


# kanye = CrazyString("west")
# print(kanye.reverse())        


# **********************************************************************

# Build own parent class

# class Auto:
    
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color


#     def carDetails(self):
#         print(f"{self.make} {self.model} {self.color}")


# class Hybrid(Auto):

#     def carType(self):
#         print("I'm a hybrid car")

#     def carDetails(self):
#         print("I'm in a hybrid car")
#         super(Hybrid, self).carDetails()
#         print("after the hybrid class")

# class electricCar(Auto):
#     def carType(self):
#         print("I'm a electric car")



# # auto = Auto("honda", "accord", "green")


# hybrid = Hybrid("Toyota", "prius", "silver")

# hybrid.carDetails()




# **********************************************************************

# composition

class Campus:
    
    def __init__(self):
        self.students = [] # [student, studet, stud]
    
    def addStudent(self, firstName, campus):
        student = Student(firstName, campus)
        self.students.append(student)
    
    def showCurrentStudents(self):
        for studentObj in self.students:
            print(f"{studentObj.firstName} {studentObj.campus}")

campus = Campus()

campus.addStudent('Giselle','Las Vegas')
campus.addStudent('Carol', 'Atlanta')
campus.addStudent("Jacob", "Tampa")
campus.addStudent("Victoria", "Houston")
campus.addStudent("Brandon", "Dallas")
campus.addStudent("Dot", "Auburn")

campus.showCurrentStudents()


# **********************************************************************

# class AccountHolder:
#     def __init__(self, fName, accountType, status, balance):
#         self.fname = fName
#         self.accountType = accountType
#         self.status = status
#         self.balance = balance
#         # self.holders

#     def deposit(self):
#         pass
# class Bank:
#     def __init__(self, name, address):
#         self.name = name 
#         self.address = address 
#         self.accounts = [] #holds all of our accounts
#         # self.holders.append(self.accounts)
    
#     def open_new_account(self, fName, accountType, status, balance):
#         self.fname = fName
#         self.accountType = accountType
#         self.status = status
#         self.balance = balance
#         newAccount = Account(fName, accountType, stats, balance)
#         self.accounts.append(newAccount)

#     def show_account_holder(self):
#         # holder = input("Name: "):
#         for holder in self.accounts:
#             print(f"{holder}")
#         # show detailed account information for specific account holder
        
#     # def show_account(self):
#     #     for allAccounts in self.accounts:
#     #         print(f"{allAccounts.fname}")
#     #     # print all accoutn holders 
#     #     pass
#     # def show_bank_balance(self):
#     #     #show bank balance of entire bank
#     #     pass



# # tim = AccountHolder("tim","asd", "pending","2")

# bank = Bank("TD", "Tampa, FL")

# bank.open_new_account("mike", "checking", "open", "100")
# bank.open_new_account("tom", "savings", "closed", "0")
# bank.open_new_account("adam", "savings", "open", "1000")


# bank.show_account_holder()
