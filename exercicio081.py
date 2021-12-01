valores = []
while True:
    valores.append(int(input('Digite valores')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in ('Nn'):
        break
print('-_-'*20)
print(f'Você digitou {len(valores)} numeros')
valores.sort(reverse=True)
print(f'Os valores na ordem decrescente são{valores}')
if 5 in valores:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não foi digitado')
