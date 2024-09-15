'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
sm = 0
for row in range(0,3):
    for col in range (0,3):
        numero = int(input(f'Digite um valor para [{row} {col}]: '))
        if numero % 2 == 0:
            pares.append(numero)
        matriz[row][col] = numero
        
print('=-'*30)

for row in range (0,3):
    for col in range (0,3):
        print(f'[{matriz[row][col]:^5}]',end='')
    print()

print('-='*30)
# A)
print(f'Soma dos valores pares : {sum(pares)}.')

# B) Pegar o último valor de cada linha parece ser a resposta
for row in range(0,3):
    sm += matriz [row][2]
print(f'Soma dos valores da terceira coluna: {sm}' )

# C)
print(f'Maior valor da segunda linha: {max(matriz[1])}')