num = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE',
       'OITO','NOVE','DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE',
       'DEZESSEIS','DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    print('Entre com um numero entre 0 e 20')
    aux = int(input(''))
    if 0 <= aux <= 20:
        print('O valor digitado é {}'.format(num[aux]))
        conf = str (input('Deseja continuar? [S/N]'))

        if conf == 'N':
            break
    else:
        print('Valor invalido, tente novamente')
