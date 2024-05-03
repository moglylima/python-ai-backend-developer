opcao = -1

while opcao != 0:
    opcao = int(input(' [1] - Sacar;\n [2] - Depositar;\n [3] - Transferir;\n [0] - Sair; \nDigite a opção desejada:  '))
    if opcao == 1:
        print('Sacar')
    elif opcao == 2:
        print('Depositar')
    elif opcao == 3:
        print('Transferir')
    elif opcao == 0:
        print('Sair')
    else:
        print('Opção inválida')
else:
    print('Fim do programa')