'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
name=str(input('Informe seu nome: '))
birth=int(input('Informe seu ano de nascimento: '))
gender=int(input('''Informe seu sexo:
[1] Masculino
[2] Feminino
> '''))
current= date.today().year
age= current-birth

if gender == 2:
    print(f'\nOlá {name}, o alistamento não é obrigatório para mulheres.\n')s
else:
    if age > int(18):
        time= (age - 18)
        year =  current - time
        print(f'Olá {name}, você já deveria ter se alistado há {time} anos.')
        print(f'Seu alistamento foi em: {year}.')
    
    elif age == int(18):
        print(f'Olá {name}, você deve se alistar imediatamente')
    else:
        time= (age - 18)
        year = time + current
        print(f'Olá {name}, você ainda é jovem para se alistar. Faltam {time} para o alistamento.')
        print(f'Você deverá se alistar no ano: {year}.')
    