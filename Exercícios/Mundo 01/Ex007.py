#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
aluno= input('Digite o nome do Aluno:')
nota1= float(input(f'Digite a 1ª nota do {aluno}: '))
nota2= float(input(f'Digite a 2ª nota do {aluno}: '))
media=( nota1 + nota1 ) / 2
print(f'Esta é a média do aluno {aluno}: |{ media :=^15.2f}|')