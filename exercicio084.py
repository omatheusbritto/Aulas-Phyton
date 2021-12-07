principal = []
temporaria = []
maior = menor = 0
while True:
    temporaria.append(str(input('Digite o nome')))
    temporaria.append(float(input('Digite o peso')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in ('Nn'):
        break
print('-_-'*20)
print(f'Os dados coletados foram{len(principal)} pessoas')
print(f'O maior peso é de {maior:.2}Kg que foram', end='')
for c in principal:
    if c[1] == maior:
        print(f'{principal[0]}')
print(f'O menor peso é de {menor:.2}Kg', end='')
for c in principal:
    if c[1] == menor:
        print((f'{principal[0]}'))
