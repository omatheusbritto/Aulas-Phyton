fichadealunos = []

while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: '))
    medianota = (nota1+nota2) / 2
    fichadealunos.append([nome, [nota1, nota2],medianota])
    continuarcadastro = str(input('Deseja continuar [S/N] '))
    if continuarcadastro in 'Nn':
        break
print('-_='*15)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('_'*44)
for i, a in enumerate (fichadealunos):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('_=-'*15)
    mostraraluno = int(input('Qual aluno deseja ver a nota? (9999 para interromper) '))
    if mostraraluno == 9999:
        print('Finalizando programa')
        break
    if mostraraluno <= len(fichadealunos)-1:
        print(f'Notas do aluno: {fichadealunos[mostraraluno][0]} são {fichadealunos[mostraraluno][1]}')
        print('Obrigado!')
