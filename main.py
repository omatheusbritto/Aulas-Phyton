# Sistema bancário
''' 
Crie um sistema de banco que faça entrada e saida de valores de valores,
com opções de Saque, Depósito e extratos.
na opção saque não pode ser menor do que o saldo atual existente,
limitato á 3 saque por dias e com o valor maxímo de R$500 por saque
o depósito não pode ser valor negativo,
o extrato deve-se mostrar todas as transações realizada 
'''
def linha():
    print(f'-'*31)
def saque():
    global saldo    
    global limite_de_saque
    global registro
    saque = float(input('Valor a ser sacado R$'))
    if saque > 500:
        print('ERRO - valor não permitido')
    elif saque < saldo and limite_de_saque < 3:
        saldo -= saque
        limite_de_saque += 1
        if limite_de_saque == 3:
            print(f'Limite de saque diário atingido')
        registro = {'Saque R$': saque, 'Saldo R$': saldo}
        extrato.append(registro)
    else:
        print('ERRO!!! Valor de saque menor que saldo')
def mostrar_saldo():
    global saldo
    print(f'Saldo atual em conta é de R${saldo:.2f}')
def deposito():
    global saldo
    global registro
    deposito = float(input('Valor a ser depósitado R$').replace(',','.'))
    if deposito < 0:
        print('Valor inválido!!!')
        while deposito < 0:
            deposito = float(input('Valor a ser depósitado').replace(',','.'))
    registro = {'Saldo R$': saldo, 'Depósito R$': deposito}
    extrato.append(registro)
    saldo += deposito 
def mostrar_extrato():
    global extrato
    for aux in extrato:
        for keys, value in aux.items():
            print(f'{keys} {value:.2f}')
        print('')
            


def menu():
    print('''| Para saque              [1] |
| Para depósito           [2] |
| Para saldo              [3] |
| Para Extrato            [4] |''')
    linha()

saldo = 0
extrato = []
registro = {}
limite_de_saque = 0

sair = ''
while sair != 's':
    print(f'-'*10,'Bem vindo','-'*10)
    menu()

    opcao = int(input(''))
    while (opcao < 1) and (opcao > 4):
        print(f'ERRO!!! --- Opção inválida --- ')
        menu()
    if opcao == 1:
        saque()
    elif opcao == 2:
        deposito()
    elif opcao == 3:
        mostrar_saldo()
    elif opcao == 4:
        mostrar_extrato()
    else:
        print('Opção inválida!!!')
        menu()
    sair = input('Deseja sair? [S/N] ').lower()
fechar = input('Aperte tecla ENTER para fechar')
