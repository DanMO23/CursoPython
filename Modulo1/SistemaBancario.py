import os



menu = """
MEU BANQUINHO

[d] - depositar
[s] - sacar
[e] - extrato

[sair] - sair
=> """
saldo = 0
operações = []
qt_saques = 0
LIMITE_SAQUE = 3
while True:
    
    #limpar tela
    os.system("clear")
    opcao = input(menu)



    if opcao == 'd':
        valor = float(input('valor: '))
        if(valor <= 0):
            print('valor invalido')
            continue
        saldo += valor
        operações.append(['deposito', f"R${valor:.2f}"])
        print('deposito realizado com sucesso')




    elif opcao == 's' and qt_saques <= LIMITE_SAQUE:
        valor = float(input('valor: '))
        if(valor <= 0):
            print('valor invalido')
            continue
        if(valor > saldo):
            
            print('saldo insuficiente')
            continue
        if(valor >500):
            print('valor maximo por saque é de 500 reais')
            input('pressione enter para continuar...')
            continue
        saldo -= valor
        operações.append(['saque', f"R${valor:.2f}"])
        print('saque realizado com sucesso')
        qt_saques += 1
        



    elif opcao == 'e':
        for operação in operações:
            print(operação[0], operação[1])




    elif opcao == 'sair':
        break
    



    else:
        print('opcao invalida')

    
    input('pressione enter para continuar...')