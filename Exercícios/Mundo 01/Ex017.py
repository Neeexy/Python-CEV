'''
Faça um programa que leia o comprimento cateto adjacente de um triângulo retângulo, caulcule e mostre o comprimento da hipotenusa.
'''
from math import hypot#Resolução--
'''cateto_op=float(input('Comprimento do cateto oposto: '))
cateto_ad=float(input('Comprimento do cateto adjacente: '))
hipotenusa= (cateto_op **2 +cateto_ad** 2)**(1/2)
print(f'A hipotenusa vale {hipotenusa:.2f}')'''

cateto_op=float(input('Comprimento do cateto oposto: '))
cateto_ad=float(input('Comprimento do cateto adjacente: '))
hipotenusa=hypot(cateto_op,cateto_ad)
print(f'A hipotenusa vale {hipotenusa:.2f}')
