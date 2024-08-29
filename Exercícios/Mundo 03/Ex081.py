'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
import os
numeros = []
while True:
    numero = int(input('Informe um número: '))
    numeros.append(numero)
    sair = str(input('Deseja adicionar outro número? [S/N] ')).upper().strip()[0]
    if sair in 'N':
        os.system('cls')
        break
    else:
        os.system('cls')
        print(f'O número {numero} foi adicionado à lista.')

print('=-'*30)
print(f'A lista tem os seguintes {len(numeros)} valores: {sorted(numeros,reverse=True)}')
if 5 in numeros:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
print('=-'*30)
print('\n')
for p in sorted(numeros,reverse=True):
    print('Buscando o 5',end=' ')
    if p == 5:
        print('Achei')
        break