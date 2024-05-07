# Criação de listas
frutas = ['banana', 'maçã', 'uva', 'morango', 'abacaxi']
print(frutas)

letras = ['a', 'b', 'c', 'd', 'e']
print(letras)

range_list = list(range(10))
print(range_list)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

# Acessando elementos da lista
print(frutas[0])
print(frutas[1])

# Acessando elementos da lista de trás para frente
print(frutas[-1])

print(frutas[-2])


# Listas aninhadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])

print(matriz[1][-1])

print(matriz[-1][-1])

# Fatias de listas
letras_alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']    

# pula os 2 primeiros elementos, e pega o restante
print(letras_alfabeto[2:])

# pega os 2 primeiros elementos
print(letras_alfabeto[:2])

# pega os elementos do 1 ao 3
print(letras_alfabeto[1:3])

# pega os elementos do 1 ao 3, pulando de 2 em 2
print(letras_alfabeto[0:3:2])


# Lista completa
print(letras_alfabeto[::])

# Invertendo a lista
print(letras_alfabeto[::-1])

# Iterando sobre listas
for fruta in frutas:
    print(fruta)

# uso do enumerate
for i, fruta in enumerate(frutas):
    print(f"Índice: {i} - Fruta: {fruta}")

# filtrando elementos - filtros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# simplificando 
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# modificando elementos(calculando o quadrado de cada elemento)
quadrados_numeros = []
for numero in numeros:
    quadrados_numeros.append(numero ** 2)

print(quadrados_numeros)

# simplificando
quadrados_numeros = [numero ** 2 for numero in numeros]
print(quadrados_numeros)

# Metodos da classe list
# Adicionando elementos
lista_nomes = ['João', 'Maria', 'José']
lista_nomes.append('Ana')
print(lista_nomes)

# Adicionando elementos em uma posição específica
lista_nomes.insert(1, 'Pedro')
print(lista_nomes)

# Removendo elementos
lista_nomes.remove('Maria')
print(lista_nomes)

# Removendo elementos pelo índice
lista_nomes.pop(1)
print(lista_nomes)

# Removendo todos os elementos
lista_nomes.clear()
print(lista_nomes)

# Contando elementos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros.count(2))

# Copiando listas
numeros_copia = numeros.copy()
print(numeros_copia)

# Contando elementos - quantas vezes um elemento aparece na lista
lista_obj = ["cadeira", "mesa", "cadeira", "sofá", "cadeira", "cadeira"]
print(lista_obj.count("cadeira"))

# Extendendo listas
numeros_impares = [1, 3, 5, 7, 9]
numeros_impares.extend([11, 13, 15, 17, 19])
print(numeros_impares)

# Index - retorna o índice do elemento
print(numeros_impares.index(5))

# Removendo elementos pelo informando elemento
numeros_impares.remove(5)
print(numeros_impares)

# Revertendo a lista
numeros_impares.reverse()
print(numeros_impares)

# Ordenando a lista
linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
linguagens.sort()
print(linguagens)

# Ordenando a lista de forma reversa
linguagens.sort(reverse=True)
print(linguagens)

# Ordenando usando key=lambda e len(x)
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# Ordenando usando key=lambda e len(x) de forma reversa
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# contando elementos
print(len(linguagens))

# uso do sorted
linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
print(sorted(linguagens))

# uso do sorted com key=lambda e len(x)
print(sorted(linguagens, key=lambda x: len(x)))

# uso do sorted com key=lambda e len(x) de forma reversa
print(sorted(linguagens, key=lambda x: len(x), reverse=True))

