'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = []
while sexo != 'M' or 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo != 'M' or 'F':
        print('Por favor insira seu sexo corretamente [M/F]')
if sexo == 'M':
    print(f'Seu sexo é {sexo}')
else:
    print(f'Seu sexo é {sexo}')