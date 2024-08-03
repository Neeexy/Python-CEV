'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.-
'''
from math import sin,cos,tan,radians

angulo=float(input('Digite um ângulo qualquer: '))
radi= radians(angulo)
seno=sin(radi)
cose=cos(radi)
tang=tan(radi)
print(f'Aqui estão os valores de seu angulo em: \n Seno:{seno:.4f}\n Cosseno:{cose:.4f}\n Tangente:{tang:.4f}')