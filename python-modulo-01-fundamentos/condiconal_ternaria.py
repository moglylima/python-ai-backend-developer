saldo = 1000
saque = 1500

status = "sucesso"  if saque <= saldo else "falha"

print(status)