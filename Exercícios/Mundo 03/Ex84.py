'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dados = []
pessoas = []
ma = me = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        ma = me = dados[1]
    else:
        if dados[1] > ma:
            ma = dados[1]
        if dados[1] < me:
            me = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if continuar == 'N':
        break
print('=-=' *20)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print('O mais pesados foram :',end='')
for p in pessoas:
    if p[1] == ma:
        print(f'{p[0]},',end=' ')
print(f'Pesando: {ma}Kg')
print('Os mais leves foram: ',end='')
for p in pessoas:
    if p[1] == me:
        print(f'{p[0]},',end=' ')
print(f'Pesando: {me}Kg')
