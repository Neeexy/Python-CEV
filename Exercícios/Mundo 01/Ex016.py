'''Crie um progrma que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. 
Ex: Digite um número: 6.127 
O número 6.127 tem a parte inteira: 6.'''

#--Resolução

import math

numero = float(input('Digite um número extenso:'))
inteira= math.trunc(numero)

print (f'O número {numero} tem a parte inteira: {inteira}')
#--
