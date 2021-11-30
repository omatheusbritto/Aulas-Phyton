numeros = []
for c in range(0, 5):
    n = int ( input('Digite um valor'))
    if c == 0:
        numeros.append(n)
        print(f'Valor {n} foi adicionado ao inicio da lista')
    elif n > numeros[len(numeros)-1]:
        numeros.append(n)
        print(f'O valor {n} foi adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao, n)
                print(f'O valor {n} foi adicionado {posicao + 1}º lugar ')
                break
            posicao += 1
print('-_'*20)
print(f'Os valores digitados foram {numeros}')

