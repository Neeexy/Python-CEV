#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor_m=float(input(f'Digite um valor em metros: '))
valor_cen = valor_m * 100
valor_mil = valor_m * 1000

print(f'Aqui está o valor em: \n Centímetros > |{valor_cen:.2f}| \n Milímetros > |{valor_mil:.2f}|')