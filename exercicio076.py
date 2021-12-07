listamercado = (str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')),
                str(input('Digite o produto: ')), float(input('Valor R$ ')))
valortotal = float()
contaitens = int()

print(f'-#'*20)
print(f'{"Lista de mercadoria":^40}')
print(f'-#'*20)
for pos in range(0, len(listamercado)):
    if pos % 2 == 0:
        print(f'{listamercado[pos]: <30}', end='')
        contaitens += 1
    if pos % 2 == 1:
        print(f'{listamercado[pos]: >10.2f}')
        valortotal = valortotal + listamercado[pos]

print(f'-#'*20)
print(f'Foram comprado {contaitens} com o valor de R${valortotal:.2f}')
