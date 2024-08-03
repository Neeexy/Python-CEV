'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

from colorama import Fore,init,Style,Back
init(autoreset=True)

seguimentos= print('Digite três comprimentos.')
print(Fore.YELLOW + '-=-'*20)
reta1= float(input('Reta 1: '))
reta2= float(input('Reta 2: '))
reta3= float(input('Reta 3: '))
print(Fore.YELLOW + '-=-'*20)
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print(f'\nOs seguimentos acima {Fore.GREEN}PODEM{Style.RESET_ALL} formar um triângulo: ',end='')
    if reta1== reta2 == reta3:
        print(f'EQUILÁTERO\n')
    elif reta1 != reta2 != reta3 and reta1 != reta3:
        print('ESCALENO')
    else:
        print('ISÓSCELES\n')
else:
    print(f'\nOs seguimentos acima {Fore.RED}NÃO PODEM{Style.RESET_ALL} formar um triângulo.\n')

print(Fore.YELLOW+"-=-"*20)