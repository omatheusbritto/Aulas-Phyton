time = []
jogadores = {}
partidas = []
def mostralinha():
    print('')
    print('=-|-'*12)
    print('')


while True:
    jogadores.clear()
    jogadores['Nome'] = str(input('Digite o nome do jogador : '))
    total = int(input(f'Quantas partidas {jogadores["Nome"]} fez : '))
    partidas.clear()
    for cont in range(0, total):
        partidas.append(int(input(f'Quantos Gols {jogadores["Nome"]} fez na {cont+1}º Partida? ')))
    jogadores['Gols'] = partidas[:]
    jogadores['TotalDeGols'] = sum(jogadores['Gols'])
    jogadores.copy()
    time.append(jogadores)
    mostralinha()
    print(jogadores)
    mostralinha()
    for k,v in jogadores.items():
        print(f'{k} : {v}')
    mostralinha()
    print(f'O jogador {jogadores["Nome"]} fez {jogadores["TotalDeGols"]} Gols em {len(jogadores["Gols"])} Partidas')
    mostralinha()
    for k,v in enumerate(jogadores['Gols']):
        print(f'Em sua {k+1}ª partida fez {v} Gols')
    mostralinha()
    while True:
        continuar = str(input('Deseja continuar? [S/N]'))
        if continuar in 'SsnN':
            break
        print('Opção invalida apenas [S/N]')
    if continuar in ('Nn'):
        break
mostralinha()
print('')
c = len(time)
for m in range(c):
    print(time[m])
    print('')