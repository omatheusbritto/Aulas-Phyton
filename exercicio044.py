print('')
print('________________________BEM VINDO AO SISTEMA DE PAGAMENTO_______________________')
print('| Caso o pagamento seja feito em dinheiro terá 10% de desconto                 |')
print('| Caso o pagamento seja feito no debito terá 5% de desconto                    |')
print('| Caso o pagamento em até 2X não havera desconto                               |')
print('| Caso o pagamento seja em 3X ou mais será acrescentado 20% do valor da compra |')
print('________________________________________________________________________________')
print('')
valorcompras = float (input('Qual foi o valor da compra? R$ '))
print('')
print('Para pagamento em dinheiro ou cheque digite [1]')
print('Para pagamento em debito digite             [2]')
print('Para pagamento em credito a vista digite    [3]')
print('Para parcelar a sua compra digita           {4}')
print('')
opcaodepgto = int(input('Digite uma da opções :'))
print('')
if opcaodepgto == 1:
    print('Valor da sua compra é de R${:.2f}, com desconto fica R${:.2f}'.format(valorcompras, ((valorcompras/100)*80)))
elif opcaodepgto == 2:
    print('Valor da sua compra é de R${valorcompras:.2f}, com desconto fica R${((valorcompras / 100) * 95):.2f}')
elif opcaodepgto == 3:
    print('Valor da compra é de {}'.format(valorcompras))
elif opcaodepgto == 4:
    qntparc = int (input('Quantas vezes deseja parcelar? '))
    if qntparc == 2 :
        print('Valor de sua compra é de {:.2f} parcelado em {} de {:.2f}'.format(valorcompras,qntparc,(valorcompras/qntparc)))
    else:
        print('Valor da sua compra é de R${:.2f}, com juros de R${:.2f} '.format(valorcompras, ((valorcompras / 100) * 20)))
        print('Valor mensal é de {} X R${:.2f}'.format(qntparc,((valorcompras / 100) * 120)/qntparc))
        print('Valor total da compra é de R${:.2f}'.format((valorcompras / 100) * 120))
else:
    print('Opção invalida, tente novamente mais tarde!')
