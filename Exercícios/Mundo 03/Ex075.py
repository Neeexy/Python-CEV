'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi inserido o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('Digite um número: ')),int(input('Digite mais um número: ')),int(input('Digite mais um número: ')),int(input('Digite um último número: ')),)
print(f'Você digitou os valores: {numeros}')
if 9 in numeros:
    if numeros.count(9) > 1:
        print(f'O número "9" apareceu {numeros.count(9)} vezes.')
    else:
        print(f'O número "9" apareceu {numeros.count(9)} vez.')
else:
    print('O número "9" não foi inserido!')

if 3 in numeros:
    print(f'O número "3" apareceu na posição {numeros.index(3)+1}º.')
else:
    print('O número "3" não foi inserido!')

print(f'Os valores pares inseridos são: ',end='')
print('|',end='')
for n in numeros:
    if n %2 == 0:
        print(f'{n},',end='')
print('|')