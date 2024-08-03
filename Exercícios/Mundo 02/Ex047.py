'''Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

for pares in range(2,51, 2):
    print('.', end=" ")
    if pares % 2 == 0:
        print(pares, end=' ')