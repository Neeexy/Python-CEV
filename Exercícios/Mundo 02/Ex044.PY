'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
from colorama import Fore,Back,init,Style
from time import sleep
init(autoreset=True)
print('='*15,end='')
print(f"{Fore.YELLOW} Lojas Nexy's ",end='')
print('='*15,end='\n')

valor=float(input('Digite o valor de sua compra: R$'))
print(f'''{Fore.YELLOW}
Escolha uma forma de pagamento:
[1] - À vista (Dinehiro/Cheque) - 
[2] - À vista no cartão - 
[3] - Em 2x no cartão - 
[4] - Em 3x ou mais no cartão -''',end='')
pagamento=int(input(' : '))
if pagamento == 1:
    desconto= (valor * 15)/100
    preco= valor-desconto
    print(f'''
 -Sua compra no valor de: {Style.RESET_ALL}{Fore.YELLOW}R${valor}{Style.RESET_ALL}
 -Você ganhou um desconto de 15%: {Fore.GREEN}$R{desconto}{Style.RESET_ALL}
 -O valor final de sua compra foi de: {Style.RESET_ALL}{Fore.YELLOW}R${preco}''')
elif pagamento == 2:
    desconto= (valor * 5)/100
    preco= valor-desconto
    print(f'''
 -Sua compra no valor de: {Fore.YELLOW}R${valor}{Style.RESET_ALL}
 -Você ganhou um desconto de 5%: {Fore.GREEN}$R{desconto}{Style.RESET_ALL}
 -O valor final de sua compra foi de: {Style.RESET_ALL}{Fore.YELLOW}R${preco}''')
elif pagamento == 3:
    parcela = valor/2
    print(f'''
 -Sua compra no valor de {Fore.YELLOW}R${valor}{Style.RESET_ALL}, foi parcelada em 2x.
 -Cada parcela corresponde a: {Fore.RED}R${parcela:.2f}{Style.RESET_ALL}
 -SEM JUROS o preço final é: {Style.RESET_ALL}{Fore.YELLOW}R${valor}
 ''')
elif pagamento == 4:
    parcelas= int(input('\nEm quantas vezes você deseja parcelar? '))
    if parcelas <3:
        print(f'\nVocê deve escolher um número de 3(três) parcelas ou mais.')
    else:
        preco=valor + (valor *20/100)
        parcela=preco/parcelas
        print(f'''
 -Sua compra no valor de: {Fore.YELLOW}R${valor}{Style.RESET_ALL}, foi parcelada em {Fore.LIGHTRED_EX}{parcelas}x{Style.RESET_ALL}.
 -Cada parcela corresponde a: {Fore.RED}R${parcela:.2f}{Style.RESET_ALL}
 -Com um juros de 20% por parcela, o preço final é:{Fore.YELLOW}R${preco}

''')
print('='*15,end='')
print(" Lojas Nexy's ",end='')
print('='*15,end='')