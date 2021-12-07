from random import randint
numeros = (randint(1,10),randint(1,10), randint(1,10),
           randint(1,10), randint(1,10))
print(f'Os numeros sorteados entre 0 e 10 foram {numeros}')
print(f'O maior numero sorteado foi {max(numeros)}')
print(f'O menor numero sorteado foi {min(numeros)}')