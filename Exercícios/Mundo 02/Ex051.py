'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
print('''
==============================
      10 TERMOS DA P.A
==============================

''')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo= primeiro + (20 - 1) * razao
for n in range (primeiro,decimo + razao,razao):
      print(f'{n}', end=' > ')
print('Fim')