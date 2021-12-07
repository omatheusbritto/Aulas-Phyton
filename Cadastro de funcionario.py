from time import sleep
empresa = []
cadastro = {}
aux = int()
validar = int()
def quebralinda():
    print('')
    print('___' * 25)
    print('')


def cadastrarfuncionario():
    cadastro.clear()
    cadastro['Nome'] = str(input('Digite o seu nome: '))
    cadastro['RG'] = int(input('Digite seu RG (apenas numeros): '))
    cadastro['CPF'] = int(input('Digite o seu CPF (apenas numeros): '))
    cadastro['Data De Nascimento'] = str(input('Digite a data de  nascimento (Dia/Mês/Ano): '))
    cadastro['Setor'] = str(input('Setor: '))
    cadastro['Funcao'] = str(input('Função: '))
    cadastro['Data de Admissão'] = str(input('Data de admissão (Dia/Mês/Ano): '))
    cadastro['E-mail'] = str(input('E-mail: '))
    cadastro['Telefone'] = str(input('Digite seu numero de celular (apenas numeros) '))
    print('')
    empresa.append(cadastro.copy())
    quebralinda()

print('Bem vindo ao cadastro digital da empresa')
quebralinda()
while True:
    cadastrarfuncionario()
    quebralinda()
    validar = str(input('Deseja continuar: [S/N]')).strip().upper()
    if validar not in 'SN':
        print('ERRO! Digite Apenas S ou N.')
        validar = str(input('Deseja continuar: [S/N]')).strip().upper()
    elif validar == 'N':
            break

print(empresa)
sleep(5)