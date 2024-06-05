def depositar(saldo, extrato, valor):
    """Realiza um depósito na conta."""
    if valor > 0:
        extrato.append(f'Deposito R$ + {valor:.2f}')
        saldo += valor
        print(f'Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
    else:
        print('Valor de depósito inválido! Tente novamente.')
    return saldo, extrato

def sacar(saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES):
    """Realiza um saque da conta."""
    if numero_saques < LIMITE_SAQUES:
        if valor > 0 and saldo + limite >= valor:
            extrato.append(f'Saque R$ - {valor:.2f}')
            saldo -= valor
            numero_saques += 1
            print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
        elif valor > 0 and saldo + limite < valor:
            print('Saldo insuficiente!')
        else:
            print('Valor de saque inválido! Tente novamente.')
    else:
        print('Limite de saques atingido!')
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato, limite, numero_saques, numero_depositos):
    """Exibe o extrato da conta."""
    print('Extrato bancário')
    print('----------------')
    for operacao in extrato:
        print(operacao)
    print(f'Saldo atual: R$ {saldo:.2f}')
    print(f'Limite: R$ {limite:.2f}')
    print(f'Número de saques realizados: {numero_saques}')
    print(f'Número de depósitos realizados: {numero_depositos}')
    print('----------------')

def main():
    saldo = 0
    limite = 500
    numero_saques = 0
    numero_depositos = 0
    LIMITE_SAQUES = 3
    extrato = []

    menu = """
    [d] - Depositar;
    [s] - Sacar;
    [e] - Extrato;
    [q] - Sair;

    Escolha uma opção: """

    while True:
        opcao = input(menu)
        
        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, extrato, valor)
            numero_depositos += 1
        
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_saques = sacar(saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES)
        
        elif opcao == 'e':
            exibir_extrato(saldo, extrato, limite, numero_saques, numero_depositos)
        
        elif opcao == 'q':
            print('Sistema encerrado.')
            break
        
        else:
            print('Opção inválida! Tente novamente.')

if __name__ == "__main__":
    main()
