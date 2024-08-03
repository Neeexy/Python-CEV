#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco= float(input('Digite o valor do produto: '))
desconto = preco - (preco * 0.05)
print(f"Este é o valor do produto com 5% de desconto: {desconto}")