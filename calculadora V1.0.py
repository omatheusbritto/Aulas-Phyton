def somar(a, b):
    print(f'{a} + {b} = {(a+b):.2f}')


def subtrair(a, b):
    print(f'{a} - {b} = {(a-b):.2f}')


def dividir(a, b):
    print(f'{a} / {b} = {(a/b):.2f}')


def mulltiplicar(a, b):
    print(f'{a} X {b} = {(a*b):.2f}')


print('Calculadora V1.0')
print('')
a = float(input('Entre com o primeiro valor: '))
b = float(input('Entre com o segundo valor: '))
print('')
print('[+] Para somar')
print('[-] Para subtrair')
print('[X ou *] Para multiplicar')
print('[/] Para Dividir')
operador = str(input('')).strip().upper(0)
while operador not in '+-*/x':
    print('ERRO! - Operador invalido')
    print('[+] Para somar')
    print('[-] Para subtrair')
    print('[X] Para multiplicar')
    print('[/] Para Dividir')
    operador = str(input('')).strip().upper(0)
if operador == '+':
    somar(a, b)
elif operador == '-':
    subtrair(a, b)
elif operador == ('X'):
    mulltiplicar(a, b)
elif operador == '/':
    dividir(a, b)
