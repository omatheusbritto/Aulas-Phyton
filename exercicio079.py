numeros = list()
while True:
    n = int(input('Digite um valor que deseja adicionar'))
    if n not in numeros:
        numeros.append(n)
        print(f'Valor {n}Adicionado com sucesso')
    else:
        print(f'Valor {n} duplicado, não irei adicionar!')
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'nN':
        break
numeros.sort()
print ('-_'*20)
print('Você digitou os numeros ',numeros)
