valor = mais1 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1

    valor+=preço

    if preço >1000:
        mais1 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja adicionar um novo produto? [S/N] ')).upper().strip()[0]
    if resposta =='N':
        break

print('{:-^35}'.format('FIM DO PROGRAMA'))
print(f'O valor total da compra foi: R${valor:.2f}')
print(f'Temos {mais1} custando mais de R$1000 reais')
print(f'O produto mais barato foi {barato} e custou: R${menor:.2f}')