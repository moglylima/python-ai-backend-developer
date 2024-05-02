nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(nome, idade)

print(type(nome), type(idade) )

print(nome, idade, sep=",") # sep= separador

print(nome, idade, sep=",", end="!") # end= finalizador

print(nome, idade, sep=",", end="\n!...\n") # end= finalizador

print(nome, idade, sep=",", end="!\n") # end= finalizador