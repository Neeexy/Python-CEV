'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[],[]]

for n in range (1,8):
    while True:
        try:
            numero = int(input(f'Digite o {n}º valor: '))
            break
        except:
            print('Número inválido inserido.')
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('=-'*30)
print(f'Os valores páres inseridos foram {sorted(lista[0])}')
print(f'Os valores ímpares inseridos foram {sorted(lista[1])}')