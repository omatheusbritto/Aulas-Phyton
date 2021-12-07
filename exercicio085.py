numeros = [[], []]
for c in range(7):
    aux = int(input(f'Digite o {c+1}º numero: '))
    if aux % 2 == 0:
        numeros[0].append(aux)
    else:
        numeros[1].append(aux)
print('-_-'*15)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares digitados foram{numeros[0]}')
print(f'Os numeros impares digitados foram {numeros[1]}')
