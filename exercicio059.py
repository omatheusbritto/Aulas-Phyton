conf = str ()
op = int ()
while op != (9):
    print ('Entre com o primeiro valor')
    x1 = int (input(''))
    print ('Entre com o segundo valor')
    x2 = int (input(''))
    print ('O que você deseja fazer com esses valores|')
    print ('Para adição (+) Digita                [1]|')
    print ('Para subtração (-) digite             [2]|')
    print ('Para multiplicação (X) digite         [3]|')
    print ('Para Divisão (/) digite               [4]|')
    print ('Para novos valores Digite             [5]|')
    print ('Caso deseja sair do programa digite   [6]|')
    op = int (input(''))
    print('')
    if op == 1 :
        print ('A soma de {} e {} é igual a {}'.format(x1,x2,(x1+x2)))
        op = 9
    if op == 2 :
        print ('A subtração de {} e {} é igual a {}'.format(x1,x2,(x1-x2)))
        op = 9
    if op == 3 :
        print ('A multiplicação de {} por {} é igual a {}'.format(x1,x2,(x1*x2)))
        op = 9
    if op == 4 :
        print ('A divisão de {} por {} é igual a {}'.format(x1,x2,(x1/x2)))
        op = 9
    if op == 5 :
        print('Voltamos ao inicio')
    if op == 6 :
        print('Tem certeza que deseja sair? [S/N]')
        conf = str(input(''))
        while conf !=  ('s','S','n','N'):
            print ('Opção invalida')
            conf = str (input(''))
        if conf == ('S' or 's'):
            break
        if conf == ('N' or 'n'):
            op = 0
print ('estamos fechando seu programa')
