'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

idade18 = f = m = fn = pessoa =0
msg = 'CADASTRE UMA PESSOA'
while True:
    print('-'*35)
    print(f'{msg:^33}',f' [{pessoa}]')
    print('-'*35)

    idade = int(input('Idade: '))
    if idade >= 18:
        idade18 += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().strip() [0]

        if sexo == 'M':
            m += 1

        if sexo == 'F':
            f += 1
            if idade < 20:
                fn += 1

            print('Sexo inválido.')
    
    pessoa += 1

    confirmação = ' '

    while confirmação not in 'SN':
        confirmação = str(input('Quer continuar? [S/N]\n')).upper().strip() [0]
    if confirmação in 'Nn':
        break
print('-'*35)
print(f'Total de pessoas cadastradas : {pessoa}')
print(f'Total de homens cadastrados: {m}')
print(f'Total de pessoas com mais de 18 anos: {idade18}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {fn}')
print('-'*35)