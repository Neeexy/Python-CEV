'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

numeros= print("Digite 3 números aleatórios.")
num1=int(input("1º Número: "))
num2=int(input("2º Número: "))
num3=int(input("3º Número: "))
menor=num1
if num2<num1 and num2<num3:
    menor= num2
if num3<num1 and num3<num2:
    menor = num3
'''-----------'''
maior=num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3 >num2:
    maior = num3

print(f"Aqui está o número de maior valor: {maior}")
print(f"Aqui está o número de menor valor: {menor}")
