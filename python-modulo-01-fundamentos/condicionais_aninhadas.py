conta_normal = True

conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 499

if conta_normal:
    if saque > saldo:
        if saque - saldo <= cheque_especial:
            print("Saque autorizado")
        else:
            print("Saldo insuficiente")
            print(f"Cheque especial: {cheque_especial}, valor necessário: {saque - saldo}")
    else:
        print("Saque autorizado")
