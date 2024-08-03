''' Crie um programa que faça o computadorutador jogar Jokenpô com você.'''
from random import choice,randint
from colorama import Fore,init,Style
from time import sleep
init(autoreset=True)
formas=['inv','Pedra','Papel','Tesoura']
computador= randint(1,3)

def print_animado(mensagem, tempo_espera=0.03):
    for letra in mensagem:
        print(letra,end='', flush=True)
        sleep(tempo_espera)
    print()
print()
print_animado('''          Vamos jogar JOKENPO!''')
print_animado('-='*20)
print_animado('''              -- JOGADAS --
              [1] - PEDRA
              [2] - PAPEL
              [3] - TESOURA''')
print_animado('-='*20)
sleep(0.5)
jogada=int(input('Faça sua jogada: '))

if computador == 1:
    if jogada ==1:
        print(Fore.BLUE+f'EMPATE2')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()
    
    elif jogada ==2:
        print(Fore.GREEN+f'VITÓRIA')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()
    elif jogada == 3:
        print(Fore.RED+f'DERROTA')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()
    else:
        print(Fore.RED+f'Jogada inválida!!')       
elif computador == 3:
    if jogada ==1:
        print(Fore.RED+f'DERROTA')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()

    elif jogada ==3:
        print(Fore.BLUE+f'EMPATE2')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()
    elif jogada ==2: 
        print(Fore.GREEN+f'VITÓRIA')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
    else:
        print(Fore.RED+f'Jogada inválida!!')
elif computador ==2:
    if jogada ==3:
        print(Fore.GREEN+f'VITÓRIA')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
    elif jogada ==1:
        print(Fore.RED+f'DERROTA')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()
    elif jogada ==2: 
        print(Fore.BLUE+f'EMPATE2')
        print_animado(f'''
        -A máquina escolheu: {(formas[computador])}
        -O jogador escolheu: {(formas[jogada])}''')
        print()
    else:
        print(Fore.RED+f'Jogada inválida!!')
sleep(0.5)
print('\nBom jogo!!')