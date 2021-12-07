from time import sleep

jogadores = {}
partidas = []
jogadores['Nome'] = str(input('Digite o nome do jogador : '))
total = int(input(f'Quantas partidas {jogadores["Nome"]} fez : '))
for cont in range(0, total):
    partidas.append(int(input(f'Quantos Gols {jogadores["Nome"]} fez na {cont+1}º Partida? ')))
jogadores['Gols'] = partidas[:]
jogadores['TotalDeGols'] = sum(jogadores['Gols'])
print('-=_-=_'*10)
print(jogadores)
print('-=_-=_'*10)
for k,v in jogadores.items():
    print(f'{k} : {v}')
print('-=_-=_'*10)
print(f'O jogador {jogadores["Nome"]} fez {jogadores["TotalDeGols"]} Gols em {len(jogadores["Gols"])} Partidas')
print('')
for k,v in enumerate(jogadores['Gols']):
    print(f'Em sua {k+1}ª partida fez {v} Gols')
print('-=_-=_'*10)

