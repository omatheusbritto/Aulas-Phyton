valores = []
numinpar = []
numpar = []

while True:
    valores.append(int(input('Digite valores')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in ('Nn'):
        break
aux = len(valores)
for c in range (aux):
    if valores[c] % 2 == 0:
        numpar.append(c)
    else:
        numinpar.append(c)
print(f'Os numeros digitados foram{valores}')
print('-_-'*15)
print(f'Os numeros impares foram{numinpar}')
print('-_-'*15)
print(f'Os numeros pares foram{numpar}')
print('-_-'*15)
