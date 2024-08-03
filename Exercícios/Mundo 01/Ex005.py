#Faça um programa que leia um número inteiro e mostre no terminal o seu sucessor e antecessor.

numero = float(input(f'Digite um número qualquer:'))
antecessor = numero - 1
sucessor = numero + 1
print (f'O Antecessor do número escolhido é: \n | {antecessor:-^20} | ')
print (f'O Sucessor do número escolhido é: \n | {sucessor:-^20} | ')