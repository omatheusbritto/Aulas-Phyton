num = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
print(f'Você digitou os seguntes valores: {num}')
print(f'O numero nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero tres apareceu em {num.index(3)+1}ª')
else:
    print('f O numero tres não foi digitado')
print ('Os numeros digitado pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')

