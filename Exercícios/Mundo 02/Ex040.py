'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
from colorama import Fore,init,Style,Back
from time import sleep
init(autoreset=True)
student= str(input('Digite o nome do aluno: '))
note1= float(input(f'Informe a 1º nota do aluno {student}: '))
note2= float(input(f'Informe a 2º nota do aluno {student}: '))
mean= (note1+note2)/2
exceed=f'\nA média({mean}) do aluno {student} ultrapassou o número máximo (10), por favor revise suas notas.\n'.upper()
sleep(0.5)
print(Style.BRIGHT+'Calculando Média')
sleep(0.3)
print('-=-'*20)
sleep(0.6)

if mean > 10:
    print(Fore.RED + exceed +Style.RESET_ALL )
elif mean >= 7:
    print(f'Parabéns ao aluno {student}, ele foi {Fore.GREEN}APROVADO{Style.RESET_ALL} com média: {mean}')
elif mean >5 <6.9:
    print(f'Informe ao aluno {student} que ele entrou em {Fore.YELLOW}RECUPERAÇÃO{Style.RESET_ALL} com média: {mean}')
elif mean <5:
    print(f'Informe ao aluno {student} que ele não atingiu a nota suficiente e foi {Fore.RED}REPROVADO{Style.RESET_ALL} com média: {mean}')

sleep(0.3)
print('-=-'*20)