# Dicionarios
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa)

estudante = dict(nome='Pedro', idade=22, cursos=['React', 'Python'])
print(estudante)

# Modificando valores
estudante['idade'] = 23
print(estudante)

# Acessando elementos
print(estudante['nome'])

# Acessando elementos com get
print(estudante.get('idade'))

# Dicionários aninhados
contatos = {
    'fabio@gmail.com':{'nome': 'Fabio', 'telefone': '99999-9999'},
    'ana@gmail.com':{'nome': 'Ana', 'telefone': '99999-9998'},
    'mario@gmail.com':{'nome': 'Mario', 'telefone': '99999-9997', "extra": {'a': 1, 'b': 2}},
}

# Acessando elementos
print(contatos['mario@gmail.com']['extra']['b'])

# Iterando sobre dicionários
for chave in contatos:
    print(chave)

# Iterando sobre dicionários uso do items
for chave, valor in contatos.items():
    print(chave, valor)

# Metodos da classe dict

dicionario = {'a': 1, 'b': 2, 'c': 3}

# copiando dicionario
copia = dicionario.copy()
print(copia)

# fromkeys - cria um dicionario com as chaves e valores passados
novas_chaves = ['a', 'b', 'c', 'd']
novo_dicionario = dict.fromkeys(novas_chaves, 'valor')

# get - retorna o valor da chave passada
print(novo_dicionario.get('a'))

# items - retorna uma lista de tuplas com chave e valor
print(novo_dicionario.items())

# keys - retorna uma lista com as chaves
print(novo_dicionario.keys())

# pop - remove um elemento do dicionario
novo_dicionario.pop('d')
print(novo_dicionario)

# popitem - remove o ultimo elemento do dicionario
novo_dicionario.popitem()
print(novo_dicionario)

# setdefault - retorna o valor da chave passada, se não existir, adiciona a chave com o valor passado
print(novo_dicionario.setdefault('d', 4))
print(novo_dicionario)

# update - atualiza o dicionario com os valores passados
novo_dicionario.update({'d': 4})
print(novo_dicionario)

# values - retorna uma lista com os valores
print(novo_dicionario.values())

# limpando dicionario
copia.clear()
print(copia)

# setdefault - retorna o valor da chave passada, se não existir, adiciona a chave com o valor passado
new_dict = {"nome": "Alberto", "idade": 43}
new_dict.setdefault("idade", 44)
print(new_dict)

new_dict.setdefault("cidade", "São Paulo")
print(new_dict)

# uso do in
print("nome" in new_dict)
print("cidade" in new_dict)
print("São Paulo" in new_dict)

# Delete - remove um elemento do dicionario - del remove o dicionario inteiro tbm
del new_dict["cidade"]
print(new_dict)