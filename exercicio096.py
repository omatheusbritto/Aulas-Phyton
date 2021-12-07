from time import sleep
def area():
    a = float(input('Entre com a largura em metros: '))
    b = float(input('Entre com o comprimento em metros: '))
    mq = (a * b)
    print(f'largura: {a}m | comprimento: {b}m| Total: {mq:.2f}m²')


print('Programa de medição')
area()
sleep(5)