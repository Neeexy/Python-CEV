'''Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

cont = sum = 0

while True:
    num = int(input('Digite um valor [999 para sair]: '))
    if num == 999:
        break
    cont += 1
    sum += num
print('\n','=-='*20)
print(f' Foram inseridos: {cont} valores e a soma entre eles é: {sum}.')
print('=-='*20)