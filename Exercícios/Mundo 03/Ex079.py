'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''
import os
numeros = []
while True:
    numero = int(input('Informe um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print(f'Numero {numero} adicionado à lista.')
    else:
        print(f'Numero {numero} já existe na lista.')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':

        break
print(f'Números inseridos à lista foram: {sorted(numeros)}')
print('\nCódigo Finalizado')