''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
from colorama import Fore, init, Style,Back
init(autoreset=True)
seguimentos=print("\nDigite três comprimentos.")
print(Fore.YELLOW +'=-='*20)
reta1=float(input("Reta 1: "))
reta2=float(input("Reta 2: "))
reta3=float(input("Reta 3: "))
print(Fore.YELLOW+"-=-"*20)
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print(f'\nOs seguimentos acima {Fore.GREEN}PODEM{Style.RESET_ALL} formar um triângulo.\n')
else:
    print(f'\nOs seguimentos acima {Fore.RED}NÃO PODEM{Style.RESET_ALL} formar um triângulo.\n')
    
    
    
print(Fore.YELLOW+"-=-"*20)
print(Fore.YELLOW+f"ÚLTIMO EXERCÍCIO DO MUNDO 1")

print(Fore.YELLOW+"-=-"*20)
