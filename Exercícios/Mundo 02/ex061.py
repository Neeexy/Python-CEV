print('Gerador P.A')
print('=-='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Informe a razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    cont +=1
print('Fim!')