'''Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for", que é uma estrutura versátil e simples de entender. Por exemplo:'''

'''for a in range(1,10):
    print('Deu um passo')
print('Chegou ao fim')

for b in range(0,30):
    print('Passo')
    print('Pulo')
print('Passo')
print('Pega')'''

#Prática
'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print("\nFim")
'''
multiplicação = 1
for c in range(0,5):
    n = int(input("Digite um número inteiro: "))
    multiplicação *= n
print('Resultado da multiplicação entre os valores:', multiplicação)
print('Fim')