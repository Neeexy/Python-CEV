"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""
from colorama import init,Fore,Style
from time import sleep
init(autoreset=True)

numero= int(input(Fore.WHITE + "Digite um número inteiro: "))
sleep(0.7)
print(Fore.YELLOW +"Analisando número...")
sleep(1)
if numero %2 == 0:
    print(Fore.WHITE+f"O número: {Fore.GREEN}{numero}{Style.RESET_ALL} é {Fore.GREEN}PAR")
else:
    print(Fore.WHITE+f"O número: {Fore.RED}{numero}{Style.RESET_ALL} é {Fore.RED}ÍMPAR")
    