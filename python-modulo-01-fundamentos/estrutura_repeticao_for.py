texto = input('Digite um texto: ')

# interable
for letra in texto:
    if letra.upper() in 'AEIOU':
        print(letra, end=' ')
print('\nFim\n')
