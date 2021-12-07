aluno = {}
aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['média'] > 7:
    aluno['situação'] = 'aprovado'
    print(f'O aluno {aluno["nome"]}, teve a média {aluno["média"]:.2f}, esta {aluno["situação"]}')
elif aluno['média'] >= 5 < 6.99:
    aluno['situação'] = 'em recuperação'
    print(f'O aluno {aluno["nome"]}, teve a média {aluno["média"]:.2f}, esta {aluno["situação"]}')
else:
    aluno['situação'] = 'reprovado'
    print(f'O aluno {aluno["nome"]}, teve a média {aluno["média"]:.2f}, esta {aluno["situação"]}')
