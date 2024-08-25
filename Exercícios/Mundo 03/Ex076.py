'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos =('Caneta', 2,
'Lápis', 1.50, 'Borracha', 0.50,
'Corretivo', 3.75, 'Calculadora', 7.50,
'Caderno', 20.99, 'Estojo', 12.50,
'Post-it', 10.40, 'Lápis de Cor', 5.50,
'Folha A4', 7.50, 'Tesoura', 4.70,
'Marca Texto', 5.99)

print('-='*20)
print(f'{"PAPELARIA":^37}')
print('-='*20,'\n')
for item in range(0, len(produtos)):

    if item  %2 == 0: # Produtos nas posições pares e preços nas posições ímpares
        print(f"{produtos[item]:.<30}",end='') # Exibe os Produtos
    else:
        print(f'R${produtos[item]:>7.2f}') # Exibe os Preços

print('-='*20,'\n')