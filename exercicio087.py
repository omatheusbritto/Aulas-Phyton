matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = numeropar = maior = int(0)
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o um valor[linha[{linha+1}]|coluna [{coluna+1}]] : '))
print('_-'*25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^15}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            numeropar += matriz[linha][coluna]
        if coluna == 2:
            soma += matriz[linha][coluna]
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
    print('')
print('-_'*25)
print(f'A soma dos numeros pares digitado é {numeropar}')
print(f'A soma dos numeros da coluna 3 é de {soma}')
print(f'O maior numero da linha 2 é de {maior}')
