MAIOR_IDADE = 18

IDADE_ESPECIAL = 12

idade = int(input('Digite sua idade: '))

print('Condição 01 - if,esle')
if idade >= MAIOR_IDADE:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')


print('Condição 02 - if, elif, else')
if idade >= MAIOR_IDADE:
    print('Você é maior de idade, pode tirar CNH')

elif idade > IDADE_ESPECIAL:
    print('Você é menor de idade, pode ter aulas teóricas, mas não pode ter as praticas!')
else:
    print('Você é menor de idade, não pode tirar CNH')