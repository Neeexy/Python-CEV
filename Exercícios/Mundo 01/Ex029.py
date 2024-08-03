'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite'''
#cores
from colorama import init,Fore,Back,Style
init(autoreset=True)

vel=float(input('Informe a velocidade atual do carro: '))
limite=80
multa= (vel-limite)*7
if vel <= limite:
    print(Fore.GREEN + f"Você está num ótimo ritmo, tenha uma boa viagem!")
    
else:
    print(Fore.RED+ f"""Você está acima do limite permitido de 80Km/h.
Deverá pagar uma multa de:R${Fore.WHITE}{Style.BRIGHT}{multa:.2f}{Style.RESET_ALL}{Fore.RED}
Dirija com segurança!!!
""")