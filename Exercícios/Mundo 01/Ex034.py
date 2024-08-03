'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario= float(input("Digite o salário do funcionário: $R"))
if salario > 1250:
    aumento= (salario * 10) / 100
elif salario <=1250:
    aumento= (salario * 15) /100

s_a = salario+aumento

print(f"Seu aumento é de {aumento}, seu salário atual é {s_a}.")
