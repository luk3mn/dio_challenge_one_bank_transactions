menu = """
[d] Deposit
[w] Withdraw
[e] Extract
[q] Quit

=> """

balance: float = 300
limit: float = 500
extract: str = ""
withdraw: float = 0
withdraw_quantity: int = 0
WITHDRAW_LIMIT = 3

deposits = []
withdraws = []
while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        deposit = float(input("Set your deposit value: "))
        if deposit > 0:
            balance += deposit
            deposits.append(deposit)
    elif opcao == "w" or opcao == "W":
        temp_withdraw: float = 0
        temp_withdraw_quantity: int = 0
        withdraw_value = float(input("Set your withdraw value: "))
        if withdraw_value <= limit:
            if withdraw_value <= balance:
                temp_withdraw = withdraw + withdraw_value # save a balance temporary
                temp_withdraw_quantity = withdraw_quantity + 1 # create a count temporary

                if temp_withdraw <= limit and temp_withdraw_quantity <= WITHDRAW_LIMIT: # test limit balace and withdraw quantity
                    withdraw += withdraw_value # count balance
                    withdraw_quantity += 1 # count withdraw
                    balance -= withdraw_value
                    withdraws.append(withdraw_value)
                    print(f"${withdraw_value} has been withdraw")
                else:
                    print(f"The withdraw limit of R$500 has been reached or {WITHDRAW_LIMIT} withdraw has been reached")
            else:
                print("Balance is not enough")
        else:
            print("The withdraw limit of R$500 has been reached")
    elif opcao == "e" or opcao == "E":
        print("Extract")
    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("Invalid transaction, please select your transaction again")
