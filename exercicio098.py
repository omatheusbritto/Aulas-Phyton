from time import sleep
def br():
    print('')
    print('_'*35)


def contador(inicio, fim, passo):
    print(f'Contagem de  {inicio}, até {fim} em {passo} a {passo}')
    cont = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.5)
    elif inicio > fim:
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.5)
    br()


contador(1, 10, 1)
contador(10, 1, 2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
br()

contador(inicio, fim, passo)

