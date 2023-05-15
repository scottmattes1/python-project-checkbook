##############################################################

###Initializations

#Import modules
import sys
import os

#Function to convert balance from string to integer to use add and subtract functions
#when we deposit and withdraw
def bal_to_int(bal):
    intbal = 0
    var = ''
    for char in bal:
        if char.isdigit():
            var = var + char
    intbal += int(var)
    return intbal

#Function to convert balance back to a string after we've deposited to it or withdrawn from it
def bal_to_string(bal):
    string = ''
    string = '$' + str(bal)
    if len(string) > 4:
        string = string[:-3] + ',' + string[-3:]
    if len(string) > 8:
        string = string[:-7] + ',' + string[-7:]
    return string

#Function to see the balance
def seebal(account_balance):
    print(f'Your balance is {account_balance}.')

#Subfunction to make deposits
def deposit(account_balance, amount):
    account_balance = bal_to_int(account_balance)
    account_balance = account_balance + int(amount)
    account_balance = bal_to_string(account_balance)
    return account_balance

#Function to make deposits
def makedeposit(account_balance):
    amount = input("How much would you like to deposit? ")
    account_balance = deposit(account_balance, amount)
    print(f"You deposited {bal_to_string(amount)}. Your new account balance is {account_balance}.")
    return account_balance
    
#Subfunction to make withdrawls
def withdraw(account_balance, amount):
    account_balance = bal_to_int(account_balance)
    account_balance = account_balance - int(amount)
    account_balance = bal_to_string(account_balance)
    return account_balance

#Function to make withdrawls
def makewithdrawl(account_balance):
    amount = input("How much would you like to withdraw? ")
    amount = int(amount)
    account_balance = withdraw(account_balance, amount)
    print(f"You withdrew {bal_to_string(amount)}. Your new account balance is {account_balance}.")
    return account_balance




###########################################################

### Application


# Main
def main(account_balance):
    #account_balance = '$5,000'
    print(
        """
        Welcome to PyBank!
        Please select an option:

        1) see balance
        2) make deposit
        3) make withdrawl
        4) quit

        """
        )
    
    while True:

        answer = input(": ")

        if answer == '1':
            seebal(account_balance)
        if answer == '2':
            account_balance = makedeposit(account_balance)
        if answer == '3':
            account_balance = makewithdrawl(account_balance)
        if answer == '4':
            break
            
        #Would you like to perform another action?
        answer = input("Would you like to perform another action? (Y/N)")
        if answer.lower() == 'y':
            continue
        else:
            break
           
    print('\nThanks for using PyBank! Have a great day!\n')
    return account_balance


#Superfunction to main that accesses the balance.txt file and reads in the account balance
#from the last session
if os.path.exists('balance.txt'):
    with open('balance.txt', 'r') as f:
        account_balance = f.read()
    
    #main application
    account_balance = main(account_balance)
        
    with open('balance.txt', 'w') as f:
        f.write(account_balance)
        
else:
    account_balance = '$0.00'
    main(account_balance)
    with open('balance.txt', 'w') as f:
        f.write(account_balance)