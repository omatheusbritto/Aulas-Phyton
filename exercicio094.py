galera = list()
listam = list()
dados = dict()
soma = media = 0
while True:
    dados['nome'] = str(input('Digite o seu Nome: '))
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Qual o seu sexo: [M/F]')).upper().strip()[0]
        if dados['sexo'] != 'M' and dados['sexo'] != 'F':
            print('ERRO!. Digite Apenas M ou F.')
        if dados['sexo'] == 'F':
            listam.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: ')).upper().strip()[0]
        if resp != 'S' and resp != 'N':
            print('ERRO!. Digite Apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print(f'Ao todos temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é de {soma/len(galera):.2f}')
media = soma/len(galera)
if len(listam) >=1:
    print(f'As mulheres cadastradas foram: {listam}.')
else:
    print('Não foram cadastradas mulheres na lista.')
print('Lista de pessoas acima da média:')
for i, p in enumerate(galera):
    if galera[i]['idade'] >= media:
        print(p)