menu = """
    [d] - Depositar;
    [s] - Sacar;
    [e] - Extrato;
    [q] - Sair;

    Escolha uma opção: """

saldo = 0
limite = 500
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3
extrato = []

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            extrato.append(f'Deposito R$ + {valor:.2f}')
            saldo += valor
            numero_depositos += 1
            print(f'Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
        else:
            print('Valor de depósito inválido! Tente novamente.')
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor = float(input('Informe o valor do saque: '))
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
    elif opcao == 'e':
        print('Extrato bancário')
        print('----------------')
        for operacao in extrato:
            print(operacao)
        print(f'Saldo atual: R$ {saldo:.2f}')
        print(f'Limite: R$ {limite:.2f}')
        print(f'Número de saques realizados: {numero_saques}')
        print(f'Número de depósitos realizados: {numero_depositos}')
        print('----------------')
        
    elif opcao == 'q':
        print('Sistema encerrado.')
        break
    else:
        print('Opção inválida! Tente novamente.')
        
            
        
        

    