##################################################
'''
Q1a: 
'''

# x = 9, y = 2

##################################################
'''
Q1b: 
'''

# x = 27, y = 2

##################################################
'''
Q2:
'''

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

##################################################
'''
Q3:
'''

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def normal_order(self):
        print(f'{self.first_name} {self.last_name}')

    def reverse_order(self):
        print(f'{self.last_name} {self.first_name}')

##################################################
'''
Q4:
''' 

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

##################################################
'''
Q5:
'''

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)
    
    def deposit(self, amount):
        print(f'Deposit: ${float(amount)}, Latest balance: ${self.balance - float(amount)}')
        self.balance -= float(amount)

    def withdraw(self, amount):
        print(f'Withdraw: ${float(amount)}, Latest balance: ${self.balance + float(amount)}')
        self.balance += float(amount)

##################################################
'''
Q6:
'''


##################################################
'''
Q7:
'''


##################################################
