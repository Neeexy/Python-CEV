'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('='*30)
print('{:^30}'.format('BANCO NEXY'))
print('='*30)

valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cédula = 100
total_cédula =0

while True:
    if total >= cédula:
        total -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de {cédula}')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédula = 0
        if total == 0:
            break