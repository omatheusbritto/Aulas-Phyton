sexo = str(input('Digite o  seu sexo [F/M]')).strip().upper()
while sexo not in 'FfMm':
    print('Opção invalida')
    print('[F] para feminino')
    print('[M] para Masculino')
    sexo = str(input('Digite o  seu sexo [F/M]')).strip().upper()
if sexo == 'F':
    print(f'Você digitou {sexo}, de Feminino')
else:
    print(f'Você digitou {sexo}, de Masculino')
