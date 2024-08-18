print('Gerador P.A')
print('=-='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Informe a razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razão
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'A progressão finalizou com {total} exibidos.')