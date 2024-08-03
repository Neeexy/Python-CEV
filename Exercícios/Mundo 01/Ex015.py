#Escreva um progama que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias peloas quais ele foi alugado, Calcule o preço a pagar, sebendo que o carro custa $R60 por dia e $R00.15 por Km rodado.

#Informes

dias= int(input('Informe por quantos dias você alugou o carro: '))
km= float(input('Informe quantos quilometros você percorreu com o carro: '))

#Preços
preco_dias= dias*60
preco_km= km*0.15
total= preco_dias+preco_km

#Saída
print(f'\nValor cobrado pelos {dias} que você alugou o carro: R${preco_dias:.2f}')
print(f"Valor cobrado pelos {km}Km's que você percorreu com o carro: R${preco_km:.2f}")
print('-'*30)
print(f"O valor total de sua conta ficou em: R${total:.2f}\n")
