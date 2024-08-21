# Aula - 15 Interrompendo Estruturas de Repetição While
from colorama import init, Back, Style, Fore
init(autoreset=True)
'''num = s =0

while True:
    num = int(input('Digite um número: '))
    leave = str(input('Deseja adicionar outro número? [S/N] ')).upper().strip() [0]
    s += num
    if leave in 'N':
        break
    else:
        continue
print(f'A soma vale : {s}')'''

#Segunda versão

num = sum = cont = 0

while True:
    num = str(input(f'Digite o {cont+1}° valor ["Sair" para sair]: ')).upper()

    if num == 'SAIR':
        break
    
    if not num.isdigit():
        print(Fore.RED+ f'\nEntrada inválida, tente novamente.{Style.RESET_ALL}', end='\n') # Se o usuário digitar  qualquer palavra que não seja 'Sair', o código
        continue
    
    num = int(num)
    sum += num
    cont += 1
if cont <= 0:
    print()
    print(f'{Fore.YELLOW}{Style.DIM}Você não inseriu nenhum valor! Até mais.{Style.RESET_ALL}')
    print()
else:
    print()
    print('=-='*20)
    print(f' Foram inseridos: {cont} valores e a soma entre eles é: {sum}.')
    print('=-='*20)