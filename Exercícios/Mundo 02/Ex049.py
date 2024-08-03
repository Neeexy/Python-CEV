'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for'''
def print_animado(msg,time=0.03):
    for letra in msg:
        print(letra,end='',flush=True)
        sleep(time)
from time import sleep
while True:
    print_animado('Digite o número que você deseja ver a tabuada:')
    try:
        num= int(input(''))
        break
    except ValueError:
        print_animado('\nEntrada inválida! Digite apenas números inteiros.\n')     

print_animado('Preparando sua tabuada... \n')
sleep (1)
for n in range(0,101):
    resultado = num * n
    print_animado(f"|{num} X {n}| = {resultado} \n")