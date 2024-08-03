'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
print("Vamos fazer uma comparação entre números.\n")
number_1=int(input('Digite o 1º número: '))
number_2=int(input('Digite o 2º número: '))
if number_1 > number_2:
    print(f"O 1º número: {number_1} é MAIOR que o 2º número: {number_2}")
elif number_2 > number_1 :
    print(f"O 2º número: {number_2} é MAIOR que o 1º número: {number_1}")
else:
    print(f"Não existe número maior, ambos números ({number_1 } e {number_2}) são IGUAIS.")
