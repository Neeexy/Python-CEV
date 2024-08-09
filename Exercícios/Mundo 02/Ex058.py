'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

# Passo 1 - Importar Bibliotecas ( random )
# Passo 2 - Gerar Números do computador
# Passo 3 - Inicializar um contador de tentativar
# Passo 4 - Loop

# ------
print('Vamos jogar um jogo de advinhação!\n')
from random import randint as rd

num_pc = rd(0, 10)
tentativas = 0
print(num_pc)
while True:
    call = int(input('Tente advinhar um número aleatório: '))
    tentativas += 1
    if call == num_pc:
        print(f'Parabéns, você acertou com {tentativas} tentativas.')
        break
    else:
        if call > num_pc:
            print('Um pouco menos, tente novamente!')
        else:
            print('Um pouco mais, tente novamente!')