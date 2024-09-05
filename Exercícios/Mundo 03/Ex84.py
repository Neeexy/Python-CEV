'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista_temporaria = []
lista_principal = []

while True:
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso: ')))
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()
    continuar = input('Quer continuar? [S/N]').upper().split()[0]
    if continuar == 'N':
        break

print(f'Os dados foram {lista_principal}')