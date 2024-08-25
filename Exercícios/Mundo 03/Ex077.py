'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ("BENZEDOR", "AMANTEIGADO", "CARNALIDADE", "ESCAMOTEADO", "ENOJADO", "LUME", "DISPARADO", "FUNGICIDA", "ERA", "RUPTURA")

for palavra in palavras:
    print()
    print(f'Na palavra {palavra}, temos as vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')