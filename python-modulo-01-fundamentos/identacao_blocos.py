def sacar(valor):
    saldo = 1000
    if valor > saldo:
        print("Saldo insuficiente")
    else:
        print(f"Saldo anterior: {saldo}")
        print(f"Saque: {valor}")
        saldo -= valor
        print(f"Saldo restante: {saldo}")
sacar(500)

def depositar(valor):
    saldo = 1000
    print(f"Saldo anterior: {saldo}")
    print(f"Depósito: {valor}")
    saldo += valor
    print(f"Saldo atual: {saldo}")

depositar(500)