'''Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

extenso=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco')
cont= 0
while True:
    while True:
        try:
            numero = int(input('Digite um número entre 0 e 25: '))
            if 0 <= numero <= 25:
                break
        except ValueError:
            print('Tente novamente.',end=' ')
    cont+=1
    print('='*45)
    print('{:^40}'.format(f'O número que você digitou é {extenso[numero]}'))
    print('='*45)
    sair = str(input('Você deseja adicionar mais algum número? [S/N] ')).upper().strip()[0]
    if sair not in 'S':
        break
if cont > 1 :
    print(f'\nVocê digitou {cont} números, até a próxima!')
else :
    print('\nVocê digitou apenas um número, até mais!')
