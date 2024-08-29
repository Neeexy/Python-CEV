'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

valores = []

for contador in range (1, 6):
    numero = int(input('Informe um valor: '))
    if contador == 1 or numero > valores[-1]:
        valores.append(numero)
        print('Número adicionado ao fim da lista')
    else:
        posição = 0
        while posição < len(valores):
            if numero <= valores[posição]:
                valores.insert(posição,numero)
                print(f'Numero inserido na posição {posição+1 }')
                break
            posição +=1
print(f'\n{valores}')