print ('Qual o valor do Imovel que deseja comprar?')
imovelvalor = float(input('R$'))
print ('em quantos anos você deseja pagar esse imovel?')
tempoimovel = int(input(''))
print ('Qual o seu salario mensal?')
salario = float(input('R$'))
valormensal = (imovelvalor/(tempoimovel*12))
porcsalario = ((salario/100)*30)
print('Valor do imovel é de R${:.2f}, com a parcela de R${:.2f} durante o periodo de {} anos'.format(imovelvalor, valormensal, tempoimovel))
if porcsalario <= valormensal:
    print ('Podemos financiar seu imovel por R${:.2f} mensal'.format(valormensal))
else:
    print ('Não podemos financiar seu imovel, valor mensa da parcela é de R${:.2f}, maior que 30% do seu salario'.format(valormensal))
