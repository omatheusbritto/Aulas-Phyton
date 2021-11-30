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
respostacartao = str()
qtdparcela = int()
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
print(f'Cod | Nome do produto | Valor unitario |   Qtd | Valor total')
aux = len(nomeproduto)
for c in range (aux):
    valortotalproduto.append(quantidadeproduto[c] * precoproduto[c])
    print(f'{c+1:^2}  | {nomeproduto[c]:^15} | {precoproduto[c]:^15}| R${quantidadeproduto[c]:^3} | R${valortotalproduto[c]:^4}|')
    valordacompra = (valordacompra + valortotalproduto[c])
while True:
    print('')
    print(f'Valor da compra é de R${valordacompra}')
    print('')
    print('Escolha a forma de pagamento')
    print(f'[1] Para pagamento em dinheiro')
    print(f'[2] Para pagamento no cartão de Debito')
    print(f'[3] Para pagamento no cartão de credito')
    print(f'[4] Pagamento via PIX')
    print(f'[5] Para cancelamento de compras')
    formadepagamento = (str(input('')))
    if formadepagamento not in ('12345'):
        print('Opção invalida')
    elif formadepagamento == 1:
        print(f'A compra no valor de {valordacompra} será em dinheiro')
        print(f'Muito obrigado pela compra!')
        print(f'Volte sempre')
        break
    elif formadepagamento == 2:
        print(f'A compra no valor de {valordacompra} será em no cartão de Debito')
        print(f'Muito obrigado pela compra!')
        print(f'Volte sempre')
        break
    elif formadepagamento == 3:
        print(f'A compra no valor de {valordacompra} será em no cartão de Credito')
        print(f'Deseja parcelar? [S/N]')
        respostacartao = str(input(''))
        while True:
            if respostacartao not in ('SsNn'):
                print('Opção Invalida')
                break
            if respostacartao in ('Ss'):
                print('[1] Para parcelamento em 1X')
                print('[2] Para parcelamento em 2X')
                print('[3] Para parcelamento em 3X')
                print('[4] Para parcelamento em 4X')
                print('[5] Para parcelamento em 5X')
                print('[6] Para parcelamento em 6X')
                if qtdparcela not in ('123456'):
                    print('Opção invalida')
                    break
                elif qtdparcela == 1:
                    print(f'O valor de {valordacompra} ficará em {qtdparcela}X {valordacompra/qtdparcela}')
                    print(f'Muito obrigado pela compra!')
                    print(f'Volte sempre')
                    break
                elif qtdparcela == 2:
                    print(f'O valor de {valordacompra} ficará em {qtdparcela}X {valordacompra/qtdparcela}')
                    print(f'Muito obrigado pela compra!')
                    print(f'Volte sempre')
                    break
                elif qtdparcela == 3:
                    print(f'O valor de {valordacompra} ficará em {qtdparcela}X {valordacompra/qtdparcela}')
                    print(f'Muito obrigado pela compra!')
                    print(f'Volte sempre')
                    break
                elif qtdparcela == 4:
                    print(f'O valor de {valordacompra} ficará em {qtdparcela}X {valordacompra/qtdparcela}')
                    print(f'Muito obrigado pela compra!')
                    print(f'Volte sempre')
                    break
                elif qtdparcela == 5:
                    print(f'O valor de {valordacompra} ficará em {qtdparcela}X {valordacompra/qtdparcela}')
                    print(f'Muito obrigado pela compra!')
                    print(f'Volte sempre')
                    break
                elif qtdparcela == 6:
                    print(f'O valor de {valordacompra} ficará em {qtdparcela}X {valordacompra/qtdparcela}')
                    print(f'Muito obrigado pela compra!')
                    print(f'Volte sempre')
                    break
            elif respostacartao in ('Nn'):
                break
    elif formadepagamento == 4:
        print(f'Numero do PIX é (xx)xxxxx-xxxx')
        print(f'Apos confirmação de pagamento, dirija-se até o balcão para retirada de compras')
        print(f'Muito obrigado pela compra!')
        print(f'Volte sempre')
        break
    else:
        break