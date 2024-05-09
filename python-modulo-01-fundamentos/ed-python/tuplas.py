# tuplas
frutas = ("laranja", "banana", "uva", "melancia", "abacaxi",)
print(frutas)

letras = ("a", "b", "c", "d", "e",)
print(letras)

matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9),)

#acessando elementos da tupla
print(frutas[0])
print(frutas[1])

#tuplas aninhadas
print(matriz[0][0])
print(matriz[0][1])

#fatias de tuplas
letras_alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",)

#pula os 2 primeiros elementos, e pega o restante
print(letras_alfabeto[2:])

#pega os 2 primeiros elementos
print(letras_alfabeto[:2])

#pega os elementos do 1 ao 3
print(letras_alfabeto[1:3])

#pega os elementos do 1 ao 3, pulando de 2 em 2
print(letras_alfabeto[0:3:2])

#tupla completa
print(letras_alfabeto[::])

#invertendo a tupla
print(letras_alfabeto[::-1])

#iterando sobre tuplas
for fruta in frutas:
    print(fruta)

#tentando alterar um elemento da tupla
#frutas[0] = "morango"
#TypeError: 'tuple' object does not support item assignment
#tuplas são imutáveis

#tentando deletar um elemento da tupla
#del frutas[0]
#TypeError: 'tuple' object doesn't support item deletion
#tuplas são imutáveis

#tentando adicionar um elemento na tupla
#frutas.append("morango")
#AttributeError: 'tuple' object has no attribute 'append'
#tuplas são imutáveis

#tentando remover um elemento da tupla
#frutas.remove("laranja")
#AttributeError: 'tuple' object has no attribute 'remove'
#tuplas são imutáveis

#tentando adicionar uma tupla em outra
#frutas += ("morango",)
#TypeError: can only concatenate tuple (not "str") to tuple
#tuplas são imutáveis

#tentando remover um elemento da tupla
#frutas.pop()
#AttributeError: 'tuple' object has no attribute 'pop'
#tuplas são imutáveis

