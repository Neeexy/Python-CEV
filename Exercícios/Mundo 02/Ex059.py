'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
import os
from time import sleep

def print_animado(msg, time=0.10):
    linhas = msg.split('\n')
    for linha in linhas:
        palavras = linha.split()  # Divide a linha atual em palavras
        for palavra in palavras:
            print(palavra, end=' ', flush=True)
            sleep(time)
        print()  # Move para a próxima linha

valor_1 = float(input('Digite um primeiro valor: '))
valor_2 = float(input('Digite um segundo valor: '))
while True:
    os.system('cls')

    print(f'\nOs valores são: |{valor_1}| e |{valor_2}|')
    menu = '''
    Selecione uma das opções abaixo:

        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Inserir novos números
        [ 5 ] Sair do Programa

    '''
    print_animado(menu)
    op = str(input('Selecione sua opção: '))
    if op == '1':
        soma = valor_1 + valor_2
        print(f'\nA soma dos valores inseridos é: {soma}. ')
    elif op == '2':
        mul = valor_1 * valor_2
        print(f'\nO resultado da multiplicação dos valores inseridos é: {mul}. ')
    elif op == '3':
        maior = max(valor_1, valor_2)
        print(f'O maior valor entre os inseridos é: [{maior}]')
    elif op == '4':
        valor_1 = float(input('Digite o novo primeiro valor: '))
        valor_2 = float(input('Digite o novo segundo valor: '))
    elif op == '5':
        os.system('cls')
        print('\nObrigado, até mais!')
        break
    else:
        print('\nOpção inválida, tente novamente.')
    input("\nPressione ENTER para continuar...")
