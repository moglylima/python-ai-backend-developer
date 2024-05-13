# Conhecendo class string

# Criando uma string
curso = 'Programação em Python: Essencial'

# Acessando os caracteres de uma string
print(curso[0]) # P
print(curso[1]) # r
print(curso[2]) # o

# Fatiamento
print(curso[0:11]) # Programação
print(curso[12:14]) # em
print(curso[15:]) # Python: Essencial
print(curso[:14]) # Programação em

# Concatenação
curso = curso + ' com Django'
print(curso) # Programação em Python: Essencial com Django

# Funções built-in
# Tamnho da string
print(len(curso)) # 42

# Contagem
print(curso.count('P')) # 2

# Deixa a string em maiúsculo
print(curso.upper()) # PROGRAMAÇÃO EM PYTHON: ESSENCIAL COM DJANGO

# Deixa a string em minúsculo
print(curso.lower()) # programação em python: essencial com django

# Primeira letra maiúscula
print(curso.capitalize()) # Programação em python: essencial com django

# Substituição
print(curso.replace('P', 'J')) # Jrogramação em Jython: Essencial com Django

# Verifica se a string inicia com determinado texto
print(curso.startswith('Programação')) # True

# Verifica se a string termina com determinado texto
print(curso.endswith('Django')) # True

# Separa a string
print(curso.split()) # ['Programação', 'em', 'Python:', 'Essencial', 'com', 'Django']

# Atribuição múltipla
frase = 'Python é uma linguagem excelente'
palavra1, palavra2, palavra3, palavra4, palavra5 = frase.split()

print(palavra1) # Python
print(palavra2) # é
print(palavra3) # uma
print(palavra4) # linguagem

# Junção
curso = ' '.join(['Programação', 'em', 'Python:', 'Essencial', 'com', 'Django'])
print(curso) # Programação em Python: Essencial com Django

# Formatação
nome, idade = 'Ana', 30

# Uso do %
print('Nome: %s, Idade: %d anos' % (nome, idade)) # Nome: Ana, Idade: 30 anos

#uso de format
print('Nome: {0}, Idade: {1} anos'.format(nome, idade)) # Nome: Ana, Idade: 30 anos

#uso de f-string
print(f'Nome: {nome}, Idade: {idade} anos') # Nome: Ana, Idade: 30 anos

# Caracter de escape
texto = 'texto entre aspas simples'
print(texto) # texto entre aspas simples
texto = "texto entre aspas duplas"
print(texto) # texto entre aspas duplas
texto = 'Texto com "aspas duplas"'
print(texto) # Texto com "aspas duplas"
texto = "Texto com 'aspas simples'"

# Quebra de linha
texto = 'Texto com quebra de linha\nSegunda linha'
print(texto) # Texto com quebra de linha
             # Segunda linha
             
# Tabulação
texto = 'Texto com tabulação\tTabulação'
print(texto) # Texto com tabulação    Tabulação

# Barra invertida
texto = 'Texto com barra invertida\\Barra invertida'
print(texto) # Texto com barra invertida\Barra invertida

# Caracteres Unicode
texto = 'Texto com caracteres unicode: \u00c1'
print(texto) # Texto com caracteres unicode: Á

# Raw string
texto = r'Texto com \n que não será interpretado'
print(texto) # Texto com \n que não será interpretado

# Exemplo usp strip
nome = '    Ana    '
print(nome) #     Ana
print(nome.strip()) # Ana

# Exemplo lstrip
nome = '    Ana'
print(nome) #     Ana
print(nome.lstrip()) # Ana

# Exemplo rstrip
nome = 'Ana    '
print(nome) # Ana
print(nome.rstrip()) # Ana

# Exemplo center
nome = 'Ana'
print(nome.center(10, '*')) # ***Ana****

# Exemplo ljust
nome = 'Ana'
print(nome.ljust(10, '*')) # Ana*******

# Exemplo rjust 
nome = 'Ana'
print(nome.rjust(10, '*')) # *******Ana

# Exemplo zfill preenche a string com zeros
numero = '123'
print(numero.zfill(5)) # 00123

# Exemplo isdigit verifica se a string contém apenas dígitos
numero = '123'
print(numero.isdigit()) # True

# Exemplo isalpha verifica se a string contém apenas letras
texto = 'Ana'
print(texto.isalpha()) # True

# Exemplo isalnum verifica se a string contém apenas letras e números
texto = 'Ana123'
print(texto.isalnum()) # True

# Exemplo islower verifica se a string contém apenas letras minúsculas
texto = 'ana'
print(texto.islower()) # True

# Exemplo isupper verifica se a string contém apenas letras maiúsculas
texto = 'ANA'
print(texto.isupper()) # True

# Exemplo format
nome = 'Ana'
idade = 30
print('Nome: {0}, Idade: {1}'.format(nome, idade)) # Nome: Ana, Idade: 30

# Exemplo format com nome
nome = 'Ana'
idade = 30
print('Nome: {n}, Idade: {i}'.format(n=nome, i=idade)) # Nome: Ana, Idade: 30



# Fim
print('Fim')


