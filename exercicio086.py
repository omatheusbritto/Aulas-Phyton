matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o um valor[[{linha}]|[{coluna}]] : '))
print('_-_'*15)
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
