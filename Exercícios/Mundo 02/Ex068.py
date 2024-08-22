'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint as rd
print('=-='*20)
print('VAMOS JIGAR PAR OU ÍMPAR')
print('=-='*20)

while True:
    jogada = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Ímpar? [P/I] ')).upper().strip() [0]
    if par_impar == 'P':
        jogada