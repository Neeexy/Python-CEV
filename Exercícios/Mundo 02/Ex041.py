'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date

birth=int(input('Informe o ano de nascimento do atleta: '))
age= date.today().year - birth

if age <= 9:
    print(f'O atleta tem: {age} anos')
    print('Classificação: MIRIM')
elif age <= 14:
    print(f'O atleta tem: {age} anos')
    print('Classificação: INFANTIL')
elif age <= 19:
    print(f'O atleta tem: {age} anos')
    print('Classificação: JÚNIOR')
elif age <= 25:
    print(f'O atleta tem: {age} anos')
    print('Classificação: SÊNIOR')
else:
    print(f'O atleta tem: {age} anos')  
    print('Classificação: MASTER')