#Perguntar a forma de pagamento
#Se for no dinheiro terá 5% de desconto
#Se for no cartão de credito, sera cobrado taxa de 1.15% no valor da compra
#Se for no pix, terá 6% de desconto
#Final, agradecer pela compra

print(f'Sistema de Pagamento')
print(f'-_-'*10)
print(f'')
valorpgto = float(input('Digite o valor da compra R$'))
print(f'')
print(f'-_-'*10)
print(f'Para pagamento em dinheiro [1]|')
print(f'Para pagamento em cartão de debito [2]|')
print(f'Para pagamento em cartão de credito [3]|')
print(f'Para pagamento em PIX [4]|')
while True:
    opcaopgto = int(input(''))
    if opcaopgto == 1:
        valorpgto = (valorpgto/100)*95
        print('Você teve 5% de desconto')
        print(f'O valor a ser pago é de R${valorpgto:.2}')
        break
    if opcaopgto == 2:
        print(f'O valor que será pago no Debito é de R${valorpgto:.2}')
        break
    if opcaopgto == 3:
        print(f'')
        print(f'-_-' * 10)
        print('Sera acrecentado 15% no valor da sua compra')
        print('Digite o numero de parcelas ')
        print('Limite de até 4 parcelas')
        while True:
            parcelacartao = int(input(''))
            if parcelacartao != (0,5):
                print('Opção invalida')
            else:
                valorpgto = valorpgto * 1.15
                valorparcela = valorpgto / parcelacartao
                print(f'Valor da compra ficará R${valorpgto}')
                print(f'{parcelacartao} X R${valorparcela:.2}')
                break
    if opcaopgto == 4:
        valorpgto = (valorpgto/100)*94
        print('Você teve 6% de desconto')
        print(f'O valor a ser pago é de R${valorpgto:.2}')
        break
    else:
        print('Opção invalida')
