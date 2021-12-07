listateste = []
mai = 0
men = 0
for c in range (0 , 5):
    listateste.append(int (input(f'Digite o {c+1}º valor: ')))
    if c == 0:
        mai = men = listateste[c]
    else:
        if listateste[c] > mai:
            mai = listateste[c]
        if listateste[c] < men:
            men = listateste[c]
print('=-'*18)
print(f'Os valores difitados foram {listateste}')
print('=-'*18)
print(f'Maior valor digitado foi {mai}, na posição: ', end='')
for i, v in enumerate(listateste):
    if v == mai:
        print(f'{i+1}.. ', end='')
print()
print('=-'*18)
print(f'Menor valor digitado foi {men}, na posição: ', end='')
for i, v in enumerate(listateste):
    if v == men:
        print(f'{i+1}.. ', end='')
print()