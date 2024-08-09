'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
# Passo 1 - Importar Bibliotecas ( random )
# Passo 2 - Gerar Números do computador
# Passo 3 - Inicializar um contador de tentativar
# Passo 4 - Loop
# ------
from random import randint as rd
print('-------- Vamos jogar um jogo de advinhação! Vou pensar num número aleatório entre 0 e 50. --------')

num_pc = rd(0, 50)
tentativas = 0
max = 6
while True:
    call = int(input('\nTente advinhar um número aleatório: '))
    tentativas += 1
    if call == num_pc:
        print(f'\nParabéns, você acertou com {tentativas} tentativas.')
        break
    elif call > num_pc:
        print(f'Um pouco menos, tente novamente! Você usou {tentativas} tentativas de {max}.')
    else:
        print(f'Um pouco mais, tente novamente! Você usou {tentativas} tentativas de {max}.')
    if tentativas == max:
        print(f'\nInfelizmente você não acertou o número que eu pensei, ele era o {num_pc}.')
        break