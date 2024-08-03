'''
Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random

nome1 = input('Nome do Aluno: ')
nome2 = input('Nome do Aluno: ')
nome3 = input('Nome do Aluno: ')
nome4 = input('Nome do Aluno: ')
lista= [nome1,nome2,nome3,nome4]
escolhido=random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

#Com For e Lista
'''alunos=[]
for n in range(4):
    nomes=input("Informe o nome do aluno: ")
    alunos.append(nomes)
escolhido=random.choice(alunos)
print(f'O aluno escolhido para apagar a lousa foi o {escolhido}.')'''