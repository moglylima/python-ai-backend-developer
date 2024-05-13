# Funções Python

# Criando uma função
def hello():
    print('Hello, World!')
    
# Chamando a função
hello() # Hello, World!

# Função com parâmetro
def hello(nome):
    print(f'Hello, {nome}!')
    
# Chamando a função
hello('Python') # Hello, Python!

# def hello(nome = 'Python'):
def hello(nome = 'Python'):
    print(f'Hello, {nome}!')

hello() # Hello, Python!

# Função com retorno
def soma(a, b):
    return a + b

print(soma(2, 3)) # 5

# Função com múltiplos retornos
def potencia(a, b):
    return a ** b, b ** a

print(potencia(2, 3)) # (8, 9)

# Retorno de uma função
def par(x):
    return x % 2 == 0

print(par(2)) # True
print(par(3)) # False

# Função sem retorno
def funcao():
    print('Olá, Mundo!')
    
a = funcao() # Olá, Mundo!
print(a) # None

# Argumentos nomeados
def media(a, b):
    return (a + b) / 2

print(media(10, 8)) # 9.0
print(media(b = 8, a = 10)) # 9.0

# Função args e kwargs
def func(*args):
    return args

print(func(1, 2, 3, 4, 5)) # (1, 2, 3, 4, 5)

def func(**kwargs):
    return kwargs

print(func(a = 1, b = 2, c = 3)) # {'a': 1, 'b': 2, 'c': 3}

def exibir_msg(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    message = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print (message)

exibir_msg("2020-01-01", "Olá, Mundo!", "Python é uma linguagem excelente", autor = "Guido van Rossum", versao = "3.8.1")


# Parâmetros especiais
def func(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
    
func(1, 2, 3, 4, 5, x = 6, y = 7)

# parametros especiais por posição
def func(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    
func(1, 2, 3, 4, e = 5, f = 6)

# parametros especiais por posição e nomeados
def func(a, b, /, c, d, *args, e, f, **kwargs):
    print(a, b, c, d, args, e, f, kwargs)

func(1, 2, 3, 4, 5, 6, 7, e = 8, f = 9, x = 10, y = 11)


# Função recursiva
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# Função anônima
quadrado = lambda x: x ** 2

print(quadrado(2)) # 4

# Função map
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x ** 2, numeros)



