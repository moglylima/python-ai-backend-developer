saldo = 200 
saque = 200
limite = 150

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True


print(saldo >= saque and saldo >= limite) # True

print(saldo >= saque or saldo >= limite) # True

print(not saldo >= saque) # False

print(not saldo >= limite) # False

print(not saldo >= saque and not saldo >= limite) # False
