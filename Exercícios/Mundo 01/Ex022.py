"""Crie um programa que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiúsculas
O nome com todas as letrs minúsculas
Quantas letras ao todo ( sem considerar espaços)
Quntas letras tem o 1ºnome
"""

nome=str(input('Digite seu nome completo: '))
maior=(nome.upper())
menor=(nome.lower())
no_space=(nome.split())
qnt=(len(nome)-nome.count(' '))
primeiro=(len(no_space[1]))

#Saída
print(f"""
O seu nome em letras maiúsculas é: {maior}
O seu nome em letras minúsculas é: {menor}
A quantidade de letras no seu nome completo é: {qnt}
A quantidade de letras do seu primeiro nome é: {primeiro}
""")
