grupo01 = []
dadospessoais = []
for c in range(3):
    dadospessoais.append(str(input('Digite seu nome completo:')))
    dadospessoais.append(str(input('Digite sua data de nascimento: ')))
    dadospessoais.append(str(input('Digite seu telefone: ')))
    print('')
    grupo01.append(dadospessoais[:])
    dadospessoais.clear()
for c in grupo01:
    print(f'nome completo: {c[0]}')
    print(f'Data de nascimento é {c[1]}')
    print(f'Telefone para contato é {c[2]}')
    print('')

