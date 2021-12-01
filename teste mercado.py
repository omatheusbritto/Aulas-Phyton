#Criar um sistema de mercado
#Lista de produto
#Lista de preço
#Quantas unidade do produto
#Mostrar produto com seu preço unitario
#Mostrar valor total de cada produto qtd X Valor
#Mostrar valor total da vendas

nomeproduto = []
quantidadeproduto = []
precoproduto = []
valortotalproduto = []
formadepagamento = str()
valordacompra = float()
print(f'-#'*20)
print(f'{"Programa para Mercado":^40}')
print(f'-#'*20)
while True:
    print(f'Digite o nome do produto: ')
    nomeproduto.append(str(input()))
    print(f'Digite o valor do produto R$')
    precoproduto.append(float(input()))
    print(f'Digite a quantidade')
    quantidadeproduto.append(float(input()))
    print(f'deseja continuar? [S/N]')
    resposta = str (input())
    if resposta in ('nN'):
        break
print(f'Cod | Nome do produto | Valor unitario |   Qtd | Valor total|')
aux = len(nomeproduto)
for c in range (aux):
    valortotalproduto.append(quantidadeproduto[c] * precoproduto[c])
    print(f'{c+1:^2}  | {nomeproduto[c]:^15} | R${precoproduto[c]:^12.2f}| {quantidadeproduto[c]:^5.0f} | R${valortotalproduto[c]:^9.2f}|')
    valordacompra = (valordacompra + valortotalproduto[c])
print('')
print(f'O valor da sua compra é de R${valordacompra:.2f}')
print(f'Muito obrigado pela compra')
print(f'Volte sempre!')
