'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
import os
def limpar():
    os.system('cls')
def valor(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('=-= '*20)
            print('Opção inválida. Por favor, insira um número inteiro.')
            print('=-= '*20)

valor_1 = valor('Digite um primeiro valor: ')
valor_2 = valor('Digite um segundo valor: ')
op = 0
while op != 5:
    limpar()
    print(f'\nOs valores são: |{valor_1}| e |{valor_2}|')
    print('''\nSelecione uma das opções abaixo
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Inserir novos números
        [ 5 ] Sair do Programa''')
    try:
        op = int(input('Selecione sua opção: '))
    except ValueError:
        print('=-= '*20)
        print('Opção inválida. Por favor, insira um número inteiro.')
        print('=-= '*20)
        input("\nPressione ENTER para continuar...")
        continue
    if op == 1:
        soma = valor_1 + valor_2
        print(f'\nA soma dos valores inseridos é: {soma}. ')
    elif op == 2:
        mul = valor_1 * valor_2
        print(f'\nO resultado da multiplicação dos valores inseridos é: {mul}. ')
    elif op == 3:
        maior = max(valor_1,valor_2)
        print(f'O maior valor entre os inseridos é: [{maior}]')
    elif op == 4:
        valor_2 = valor('Digite um novo primeiro valor: ')
        valor_2 = valor('Digite um novo segundo valor: ')
    elif op == 5:
        limpar()
        print('=-= '*20)
        print('\nObrigado, até mais!')
        print('=-= '*20)
        break
    else:
        print('=-= '*20)
        print('Opção inválida, tente novamente.')
        print('=-= '*20)
    input("\nPressione ENTER para continuar...")