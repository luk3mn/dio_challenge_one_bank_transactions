menu = """
[d] Deposit
[w] Withdraw
[e] Extract
[q] Quit

=> """

balance: float = 0
limit: float = 500
extract: str = ""
withdraw_quantity: int = 0
WITHDRAW_LIMIT = 3

while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        print("Deposit")
    elif opcao == "w" or opcao == "W":
        temp_balance: float = 0
        temp_withdraw_quantity: int = 0
        withdraw_value = float(input("Set your withdraw value: "))
        if withdraw_value <= limit and withdraw_quantity <= WITHDRAW_LIMIT:
            temp_balance = balance + withdraw_value # save a balance temporary
            temp_withdraw_quantity = withdraw_quantity + 1 # create a count temporary

            if temp_balance <= limit and temp_withdraw_quantity <= WITHDRAW_LIMIT: # test limit balace and withdraw quantity
                balance += withdraw_value # count balance
                withdraw_quantity += 1 # count withdraw
                print(f"${withdraw_value} has been withdraw")
                print(f"""
                        Balance: {balance}
                        Withdraw limit: {withdraw_quantity}
                    """)
            else:
                print(f"The withdraw limit of R$500 has been reached or {WITHDRAW_LIMIT} withdraw has been reached")
        else:
            print("The withdraw limit of R$500 has been reached")
    elif opcao == "e" or opcao == "E":
        print("Extract")
    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("Invalid transaction, please select your transaction again")
