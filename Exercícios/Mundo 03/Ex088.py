'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint as rd
from time import sleep
numeros = []
print('⩵'*50)
print(F"{'JOGUE NA MEGA SENA':^47}")
print('⩵'*50)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-='*7,end='')
print(f'  SORTEANDO {jogos} JOGOS  ',end='')
print('-='*7)

for r in range(jogos):
    sleep(0.8)
    print(f'Jogo {r+1} : ',end='')
    while len(numeros) < 6:
        number = rd(1,60)
        if number not in numeros:
            numeros.append(number)
    print(f'{sorted(numeros)}')
    numeros.clear()

print('-='*7,end='')
print(f'  < BOA SORTE! >  ',end='')
print('-='*7)