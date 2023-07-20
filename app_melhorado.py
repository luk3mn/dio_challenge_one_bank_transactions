import re
import random

def menu():
    """user menu"""
    return """
    [cu] Create User
    [ca] Create Account
    [d]  Deposit
    [w]  Withdraw
    [e]  Extract
    [q]  Quit
    => """

def create_account(cpf, users, account, id):
    AGENCY = "0001"
    for user in users:
        if cpf == user[2]:
            # id = 1
            user.append(id)
            user.append(AGENCY)
            account.append(user)
    # print(account)
    return id

def create_user(name, birthday, cpf, street, number, neighborhood, city, state, users, cpfs):
    address = f"{street}, {number} - {neighborhood} - {city}/{state}"
    user = [name, birthday, cpf, address]

    if cpf in cpfs:
        print("Ja existe")
    else:
        users.append(user)
        cpfs.append(cpf)
    print(users)

def deposit(value, balance, extract, deposits):
    if value > 0:
        balance += value
        extract = "available"
        deposits.append(value)
    return balance, extract, deposits

def make_withdraw(value, balance, withdraw, withdraw_quantity, extract, withdraws):

    temp_withdraw: float = 0
    temp_withdraw_quantity: int = 0

    if value <= limit:
        if value <= balance:
            temp_withdraw = withdraw + value # save a balance temporary
            temp_withdraw_quantity = withdraw_quantity + 1 # create a count temporary

            if temp_withdraw <= limit and temp_withdraw_quantity <= WITHDRAW_LIMIT: # test limit balace and withdraw quantity
                withdraw += value # count balance
                withdraw_quantity += 1 # count withdraw
                balance -= value
                withdraws.append(value)
                print(f"${value} has been withdraw")
                extract = "available"
            else:
                print(f"The withdraw limit of R$500 has been reached or {WITHDRAW_LIMIT} withdraw has been reached")
        else:
            print("Balance is not enough")
    else:
        print("The withdraw limit of R$500 has been reached")
    return balance, withdraw, withdraw_quantity, extract, withdraws

def show_extract(extract, withdraws, deposits, withdraw_quantity, balance):
    if extract == "":
        print("No transactions have been made on the account")
    else:
        print(f"""
            All withdrawals: {withdraws}
            All deposits: {deposits}
            Withdraws today: {withdraw_quantity}
            Current balance is R${balance:.2f}
        """)


balance: float = 300
limit: float = 500
extract: str = ""
withdraw: float = 0
withdraw_quantity: int = 0
WITHDRAW_LIMIT = 3

deposits = []
withdraws = []
users = [['Luke', '30/01/1998', '123', 'anywhere'],['Ren', '29/02/1998', '456', 'nowhere']]
cpfs = []
account = []
id_user: int = 1
while True:

    option = input(menu())

    if option == "d" or option == "D":
        value = float(input("Set your deposit value: "))
        balance, extract, deposits = deposit(value, balance, extract, deposits)
    elif option == "w" or option == "W":
        value = float(input("Set your withdraw value: "))
        balance, withdraw, withdraw_quantity, extract, withdraws = make_withdraw(value, balance, withdraw, withdraw_quantity, extract, withdraws)
    elif option == "e" or option == "E":
        show_extract(extract, withdraws, deposits, withdraw_quantity, balance)
    elif option == "cu" or option == "CU" or option == "Cu" or option == "cU":
        print('Put your information below: ')
        name = input('Name: ')
        cpf = input('CPF: ')
        birthday = input('Birthday: ')
        street = input("Street: ")
        number = input("Number: ")
        neighborhood = input('Neighborhood: ')
        city = input('City: ')
        state = input('State: ')

        create_user(name, birthday, cpf, street, number, neighborhood, city, state, users,cpfs)
    elif option == "ca" or option == "CA" or option == "Ca" or option == "cA":
        cpf = input('Put your cpf: ')
        id_user = create_account(cpf, users, account, id_user)
        id_user += 1
        print(id_user)
        print(account)
    elif option == "q" or option == "Q":
        break
    else:
        print("Invalid transaction, please select your transaction again")
