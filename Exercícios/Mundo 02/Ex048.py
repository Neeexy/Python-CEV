'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500'''
from playsound import playsound
soma = 0
counter = 0
for count in range(1,501,2):
    if count % 3 ==0:
        soma += count
        counter += 1
print(f'A soma de todos os {counter} valores solicitados é: {soma}') 
playsound('Fireworks.mp3')