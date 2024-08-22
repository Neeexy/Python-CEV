'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint as rd
print('=-='*20)
print('VAMOS JIGAR PAR OU ÍMPAR')
print('=-='*20)
jogada = 0
wins = 0
while True:
    jogada = int(input('Diga um valor: '))
    comp = rd(0, 10)
    print(comp)
    tipo = ' '
    while tipo not in 'IiPp':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip() [0]
    rodada =  comp + jogada
    print(f'Você jogou {jogada} e o computador jogou {comp}. Total de {rodada} ', end='')
    print('DEU PAR' if rodada %2 ==0 else 'DEU IMPAR')
    if tipo == 'P':
        if rodada %2 == 0:
            print('Você VENCEU!!')
            wins+=1
        else:
            print('Você PERDEU!!')
            break
    if tipo == 'I':
        if rodada %2 == 1:
            print('Você VENCEU!!')
            wins+=1
        else:
            print('Você PERDEU!!')
            break
                
print(f'GAME OVER! Você venceu {wins} vezes.')