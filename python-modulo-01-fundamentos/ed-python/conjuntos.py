numeros = set([1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 10])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set({"gol", "uno", "palio", "gol", "uno", "palio", "fusca", "brasilia"})
print(carros)

carros = set(("gol", "uno", "palio", "gol", "uno", "palio", "fusca", "brasilia"))
print(carros)


# pouco utilizado
linguagens = {"python", "java", "c", "c++", "python"}
print(linguagens)

# acessando elementos

# não é possível acessar elementos de um conjunto
# print(linguagens[0])
# TypeError: 'set' object is not subscriptable
# conjuntos não são indexáveis
# precisamos iterar sobre os elementos
for linguagem in linguagens:
    print(linguagem)

# usar list para acessar elementos(a rodem é aleatória)
print(list(linguagens)[0])

# converter conjunto para lista
linguagens = list(linguagens)
print(linguagens[0])
print(linguagens[1])
print(linguagens[2])
print(linguagens[3])


# operações com conjuntos
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# união
print(a | b)
print(a.union(b))

# interseção
print(a & b)
print(a.intersection(b))

# diferença
print(a - b)
print(a.difference(b))

# diferença simétrica
print(a ^ b)
print(a.symmetric_difference(b))

# subconjunto
print(a <= b)

# subconjunto próprio
print(a < b)

# superconjunto
print(a >= b)

# superconjunto próprio
print(a > b)

# adicionar elementos
a.add(6)
print(a)

# remover elementos
a.remove(6)
print(a)

# remover elementos
a.discard(6)
print(a)

# remover elementos
a.pop()
print(a)

# remover todos os elementos
a.clear()
print(a)

# deletar o conjunto
del a
# print(a)
# NameError: name 'a' is not defined

# conjunto vazio
a = set()
print(a)

# conjunto vazio
a = {}
print(a)

# conjunto vazio
a = set({})
print(a)


