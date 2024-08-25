'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

# Passos
# 0 - Importar biblioteca (random)
# 1 - Criar uma tupla vazia
# 2 - Adicionar 5 números aleatórios à tupla (randint)
# 3 - Verificar maior e menor valor da tupla (max,min)
# 4 - Exibir resultado

from random import randint as rd

numeros = (rd(1,58),rd(1,58),rd(1,58),rd(1,58),rd(1,58))
print('Os números sorteados foram: ',end='')
for n in numeros:
    print(n,end=' ')
print(f'\nO maior número foi: {max(numeros)}')
print(f'O menor número foi: {min(numeros)}')