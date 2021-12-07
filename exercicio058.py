aux = int (1)
while aux != 0 :
    print('Qual o seu sexo [M/F]?')
    sexo = str (input(''))
    if sexo not in ('MmFf'):
        print ('Opção invalida, tente novamente:')
        aux = 1
    elif sexo in ('Mm'):
        print ('Seu sexo é Masculino')
        aux = 0
    elif sexo  in ('Ff'):
        print ('Seu sexo é Feminino')
        aux = 0
