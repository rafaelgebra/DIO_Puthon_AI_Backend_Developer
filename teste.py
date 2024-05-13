saldo = 1000
saque = 100
limite = 100

total = saldo >= saque and saque <= limite
if total == True:
    print("Saque aprovado")
    print(f"Valor sacado {saque} Saldo atual {saldo - saque}")


