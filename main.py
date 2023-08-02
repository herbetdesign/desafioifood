menu = (f"""
Banco Digital Innovation One

############ MENU ############

       Digite a opção:
       
    s - Sacar
    d - Depósito
    e - Extrato
    q - Sair
    
##############################
""")

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "s":
        valor = float(input('Qual valor que deseja sacar? '))
        
        if valor > saldo:
            print('Sem saldo suficiente')
        elif valor > limite:
            print('O valor ultrapassa o limite')
        elif numero_saque >= limite_saque:
            print('Quantidade de saques excedido')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor}\n'
            numero_saque += 1
            print(f'Valor atual da conta: R$ {saldo:.2f}')
        else:
            print('Número informado é inválido')
           
        
    elif opcao == "d":
        valor = float(input('Qual valor que deseja depositar? '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor}\n'
            print(f'Valor atual da conta: R$ {saldo:.2f}')
        else:
            print('O seu valor é inválido')
        
    elif opcao == "e":
        print('\n########### EXTRATO ###########')
        print('Não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('#################################')
    
    elif opcao == "q":
        print('Usuário deslogado')
        break
    
    else:
        print('Opção inválida. Selecione novamente')
        
