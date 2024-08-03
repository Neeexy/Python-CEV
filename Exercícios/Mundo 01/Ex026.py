'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase= str(input('Digite uma frase: ')).strip().lower()
qtn_a= frase.count('a')
pos=frase.find('a')
pos_=frase.rfind('a')
print(f'A letra "A" aparece {qtn_a} vezes na frase.')
print(f'A primeira letra "A" apareceu pela 1º vez na posição: {pos}')
print(f'A última letra "A" apareceu pela 1º vez na posição: {pos_}')