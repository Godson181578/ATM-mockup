"""
First Zuri Project
Simulation of an ATM machine functionalities

"""

# import random number generator library
import random

# used dictionary to create a database for user details
database = {}


def initialization():
    print('Welcome to Online Python Banking System')

    try:
        existingAccount = int(input('Do you have an account with us: 1 (yes) 2 (no) \n'))
        if existingAccount == 1:
            loginFunction()

        elif existingAccount == 2:
            registrationFunction()

        else:
            print('Invalid option selected')
            initialization()

    except ValueError:
        print('Oops!! You have entered an unaccepted value, try again..........')
        initialization()


def registrationFunction():
    print('****** User Registration ******')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('create a password \n')

    accountNumber = accountGeneratorFunction()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your account has been successfully created')
    print('Your account number is: {} '.format(accountNumber))
    print('Make sure you keep it safe')

    loginFunction()


def loginFunction():
    print('****** User Login ******')

    UserAccount = int(input('what is your account number \n'))
    password = input('What is your password \n')

    for accountNumber, userDetails in database.items():
        if accountNumber == UserAccount:
            if userDetails[3] == password:
                print(accountNumber, userDetails[3])
                bankOperationFunction(userDetails)

    print('Invalid account or Password')
    loginFunction()


def bankOperationFunction(user):
    print('welcome {} {}'.format(user[0], user[1]))

    selectedOption = int(input('what would you like to do? (1) deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if selectedOption == 1:
        depositFunction()

    elif selectedOption == 2:
        withdrawalFunction()

    elif selectedOption == 3:
        logoutFunction()

    elif selectedOption == 4:
        exit()
    else:
        print('Invalid option selected')
        bankOperationFunction(user)


def withdrawalFunction():
    accountBalance = 40000
    withdrawAmount = int(input("How much would you like to withdraw? \n"))
    if withdrawAmount > accountBalance:
        print('insufficient balance, try lower amount')

    else:
        currentBalance = accountBalance - withdrawAmount
        print('Withdrawal successful, Take your cash')



def depositFunction():
    mainBalance = 0
    depositBalance = int(input("How much would you like to deposit? \n"))
    mainBalance += depositBalance
    print('Deposit successful, current account balance is {}'.format(mainBalance))


def accountGeneratorFunction():
    return random.randrange(1111111111, 9999999999)


def logoutFunction():
    loginFunction()


initialization()
