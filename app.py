menu = """
[d] Deposit
[s] Withdraw
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

    if opcao == "d":
        print("Deposit")
    elif opcao == "s":
        print("Withdraw")
    elif opcao == "e":
        print("Extract")
    elif opcao == "q" | "Q":
        break
    else:
        print("Invalid transaction, please select your transaction again")
