'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

from colorama import init,Fore,Style
init(autoreset=True)

casa=float(input('Qual o valor da casa que você deseja comprar? R$'))
salario= float(input('Qual é o seu salário atual? R$'))
tempo= int(input("Em quantos anos você planeja quitar a casa? "))
prestacao= casa / (tempo * 12)
minimo= (salario* 30)/100

print(Style.BRIGHT+f'\nPara pagar uma casa de R${casa} em {tempo} anos, a prestração será de {prestacao:.2f}.\n')
if minimo <= prestacao:
    print(Fore.RED +  f'Com o seu salário atual você NÃO foi aceito para a liberação do impréstimo bancário.\n') 
else:
    print(Fore.GREEN+f'Parabéns, o seu empréstimo foi aceito!!\n')


