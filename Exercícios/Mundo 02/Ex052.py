'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
#Passo 1 - Ler o número
#Passo 2 - Verificar se é primo
#O resto é estilo
from colorama import Fore,init,Style,Back
init(autoreset=False)
#-----------------------
max = 10000
while True:
    try:
        número = int(input(f'Digite um número {Fore.RED}(MÁXIMO {max}){Style.RESET_ALL}: '))
        if número >= max+1:
            print(f'O número é muito extenso, tente não exceder o valor máximo!')
        else:    
            break
    except ValueError:
        print('O elemento inserido deve ser um número inteiro!') 
total = 0

print('|...',end='')
for contador in range (1,número +1 ):
    if número % contador ==0:
        print(f'{Fore.GREEN}',end=' ')
        total += 1 
    else:    
        print(f'{Fore.RED}',end=' ')
    print(f'{contador}', end='') 
print(Style.RESET_ALL +' ...|',end='')
print(Style.RESET_ALL + f'\n\nO número {número} é divisível {total} vezes!') 
if total >=2:
    print(f'\nO número {Fore.GREEN}{número}{Style.RESET_ALL} é primo!\n')
else:
    print(f'\nO número {Fore.RED}{número} {Style.RESET_ALL}é composto!\n')