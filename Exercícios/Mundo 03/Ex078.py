'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = []

for v in range (5):
    v = int(input(f'Informe o {v+1}° valor: '))
    valores.append(v)

print('-='*30)
print('Você digitou os valores: ',end='')

print('| ',end='')
for v in valores:
    print(f'{v} ',end='')
print('|')

max_valor = max(valores)
pos_max = [v + 1 for v, x in enumerate(valores) if x == max_valor]


min_valor = min(valores)
pos_min = [v + 1 for v,x in enumerate(valores) if x == min_valor]

print(f'\nO maior valor digitado foi | {max_valor} | nas posições: {', '.join(map(str,pos_max))}.')

print(f'O maior valor digitado foi | {min_valor} | nas posições: {', '.join(map(str,pos_min))}.')