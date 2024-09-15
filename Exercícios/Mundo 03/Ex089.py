'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
import os
alunos = []

while True:
    os.system ('cls')
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    md = (n1+n2) // 2
    alunos.append([nome,[n1,n2],md])
    sair = str(input('Quer continuar? [S/N] ')).split()[0]
    if sair in 'Nn':
        break
os.system ('cls')
print('=-'*30)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>8}')
print('-'*25)
for i,a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<12}{a[2]:>8}')
while True:
    print('-'*25)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(alunos) -1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')