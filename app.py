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
        print("Withdraw")
    elif opcao == "e" or opcao == "E":
        print("Extract")
    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("Invalid transaction, please select your transaction again")
