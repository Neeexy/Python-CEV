#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario= float(input('Informe seu salário atual: '))
aumento=  salario *0.15
nv_salario = salario+aumento
print(f" Seu  aumento de 15% corresponde a: {aumento:.2f}. \n E seu salário atual é {nv_salario}")