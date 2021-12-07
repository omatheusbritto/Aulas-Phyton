print('Qual a velocidade que você esta?')
x1 = float(input(''))
if x1 < 80:
    print('Você esta a baixo da velocidade permitida')
if x1 == 80:
    print('Você esta na velocidade permitida')
if x1 > 80:
    print('Você esta acima da velocidade permitida')
    print('Valor da multa que você receberá é de {} R${:.2f} {}' .format('\033[7;30;41m', ((x1-80)*7),'\033[m'))
