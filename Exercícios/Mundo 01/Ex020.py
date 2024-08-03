'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
'''
n1= input('Nome do aluno: ')
n2= input('Nome do aluno: ')
n3= input('Nome do aluno: ')
n4= input('Nome do aluno: ')
lista= [n1,n2,n3,n4]
random.shuffle(lista)
print(f"A ordem de apresentação será:\n {lista}")'''

#Com For e Range

alunos=[]
for a in range(5):
    nomes=input('Digite o nome dos alunos: ')
    alunos.append(nomes)
    random.shuffle(alunos)
print("A ordem de apresentação será: ")
for i, aluno in enumerate(alunos):
    print(f"{i+1}º {aluno}")
