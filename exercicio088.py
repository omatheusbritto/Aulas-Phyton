from random import sample
from time import sleep
sorteados = []
num = int(input('Quantos jogos: '))
for x in range(0, num):
    sorteados.append(sample(range(1, 61), 6))
for n, l in enumerate(sorteados):
    print(f'Jogo {n+1}: {sorted(l)}')
    sleep(1)