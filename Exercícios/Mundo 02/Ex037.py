'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
from colorama import init,Fore
init(autoreset=True)
valor=int(input('Digite um valor de números inteiros: '))

bina= bin(valor)[2:]
octa= oct(valor)[2:]
hexa= hex(valor)[2:]
print('-=-'*20)
escolha=(input('''Escolha uma das conversões abaixo:

[1] - Binário
[2] - Octal
[3] - Hexadecimal 
> '''))
print('-=-'*20)
if escolha == '1':
    print(f'\nO seu número em Binário é: {bina}\n')
elif escolha == '2':
    print(f'\nO seu número em Octal é: {octa}\n')
    
elif escolha == '3':
    print(f'\nO seu número em Hexadecimal é: {hexa}\n')
    
elif not escolha.isnumeric() or int(escolha) not in [1, 2, 3]:
    print(Fore.RED+f'''\nA opção escolhida não é válida. Aqui está o valor em todas as conversões:
[1] Binário - {bina}
[2] Octal - {octa}
[3] Hexadecial - {hexa}''')