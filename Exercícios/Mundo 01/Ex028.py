''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
'''from random import randint
from time import sleep
numero= randint(0,100)
tentativas = 0
limit_tentativas = 5
print('-=-'*20)
print("Vou pensar em um número entre 0 e 100!!")
print('-=-'*20)
print(numero)
def print_com_animacao(mensagem, tempo_espera=0.05):
    for letra in mensagem:
        print(letra, end='', flush=True)
        sleep(tempo_espera)
    print()
while tentativas < limit_tentativas:
    tentativa=int(input('Tente advinhar o número que estou pensando: '))
    tentativas +=1
    
    if tentativa == numero:
        sleep(1.5)
        print('Parabéns, você acertou o número')
        break
    else:
        if tentativa < numero:
            sleep(1.5)
            print("Que pena você errou, tente um número maior\n")
        else:
            sleep(1.5)
            print("Que pena você errou, tente um número menor\n")
        if tentativas ==  limit_tentativas:
            sleep(1)
            print(f'Que pena você chegou ao limite de  tentativas, o número era {numero}')
            break'''
    


from random import randint
from time import sleep

numero = randint(0, 100)
tentativas = 0
limit_tentativas = 5
def print_com_animacao(mensagem, tempo_espera=0.03):
    for letra in mensagem:
        print(letra, end='', flush=True)
        sleep(tempo_espera)
    print()
print_com_animacao('-=-' * 20)
print_com_animacao("Vou pensar em um número entre 0 e 100!!")
print_com_animacao('-=-' * 20)
#print(numero)



while tentativas < limit_tentativas:
    sleep(0.05)
    print_com_animacao('Tente adivinhar o número que estou pensando: ')
    tentativa = int(input())
    tentativas += 1

    if tentativa == numero:
        print_com_animacao('Parabéns, você acertou o número!')
        break
    else:
        if tentativa < numero:
            print_com_animacao("Que pena você errou, tente um número maior\n")
        else:
            print_com_animacao("Que pena você errou, tente um número menor\n")

        if tentativas == limit_tentativas:
            print_com_animacao(f'Que pena você chegou ao limite de tentativas, o número era {numero}')
            break

