from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 01': randint(1, 6),
        'Jogador 02': randint(1, 6),
        'Jogador 03': randint(1, 6),
        'Jogador 04': randint(1, 6)}
ranking = {}
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} teve o numero {v} sorteado')
    sleep(1)
print('=-_'*12)
print(f'  ==> RANKING DOS JOGADORES <==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate (ranking):
    print(f'{k+1}º lugar {v[0]} | com o numero {v[1]}')
    sleep(1)

