def escreva(msg):
    tamanho = len(msg)+6
    print('~'*(tamanho))
    print(f'   {msg}')
    print('~'*(tamanho))

msg = str(input('Digite uma mensagem: '))
escreva(msg)

