'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

#Passo 1 - Receber dados
#Passo 2 - Limpar informação
#Passo 3 - Inverter frase
#Passo 4 - Comparar e exibir resultado

#---------------------

#Passo 1 -
frase = str(input('Digite uma frase: '))
f= frase[::-1]
print(f)

'''#Passo 2 -
frase_clean = frase.lower().replace(' ', '')

#Passo 3 - 
frase_rev = frase_clean[::-1]

#Passo 4 - 
if frase_rev == frase_clean:
    print(f'A frase {frase} é um palíndromos')
else:
    print(f'A frase {frase} não é um palíndromos')'''