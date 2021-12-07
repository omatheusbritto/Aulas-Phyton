from datetime import datetime
cadastrotrabalhadores = {}

cadastrotrabalhadores['Nome'] = str(input('Digite o seu nome: '))
cadastrotrabalhadores['Ano de nascimento'] = int(input('Qual ano você nasceu? '))
cadastrotrabalhadores['Carteira de trabalho'] = str(input('possui carteira de trabalho? [S/N] '))
print('')
print(f'Olá, seu nome é {cadastrotrabalhadores["Nome"]}')
print(f'Sua ano de nascimento é {cadastrotrabalhadores["Ano de nascimento"]},')
cadastrotrabalhadores['Idade'] = datetime.now().year - cadastrotrabalhadores['Ano de nascimento']
print(f'Sua idade é {cadastrotrabalhadores["Idade"]}')
if cadastrotrabalhadores['Carteira de trabalho'] in ('Nn'):
    print(f'Você não possui carteira de trabalho')
else:
    print('')
    cadastrotrabalhadores['Numero CTPS'] = int(input('Digite o numero do CTPS: '))
    cadastrotrabalhadores['Tempo de contribuição'] = int(input('Quanto tempo de contribuição você tem? '))
    cadastrotrabalhadores['Ultimo salario'] = float(input('Qual foi o seu ultimo salario? R$'))
    aposentadoria = 30 - cadastrotrabalhadores['Tempo de contribuição']
    print(f'Numero CTPS é {cadastrotrabalhadores["Numero CTPS"]}')
    print(f'Seu tempo de contribuição é de {cadastrotrabalhadores["Tempo de contribuição"]}, faltam {aposentadoria} anos para sua aposentadoria')
    print(f'Seu ultimo salario foi de R${cadastrotrabalhadores["Ultimo salario"]:.2f}')