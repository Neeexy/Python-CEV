'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

# Passos
# 1 - Encontrar os 20 colocados
# 2 - Colocalos numa tupla em ordem
# 3 - Mostar os 5 primeiros e 4 ultimos times da tupla 
# 4 - Mostrar todos os times em ordem alfabética (sorted)
# 5 - Mostrar a colocação da Chapecoense (ele não está nos 20 primeiros)

# ---
times = ('Botafogo','Fortaleza','Palmeiras','Flamengo',
        'Bahia','Sao Paulo','Cruzeiro','Atletico-mg','Atletico-pr',
        'Vasco','Juventude','Red Bull Bragantino','Internacional',
        'Criciuma','Gremio','Fluminense','Vitoria','Corinthians',
        'Cuiaba','Atletico-go')

times_exibição = ('BOTAFOGO', 'FORTALEZA', 'CHAPECOENSE', 'FLAMENGO',
'BAHIA', 'SAO PAULO', 'CRUZEIRO', 'ATLETICO-MG', 'ATLETICO-PR',
'VASCO', 'JUVENTUDE', 'RED BULL BRAGANTINO', 'INTERNACIONAL',
'CRICIÚMA', 'GREMIO', 'FLUMINENSE', 'VITORIA', 'CORINTHIANS',
'CUIABA', 'ATLETICO-GO')

print('='*45)
print('{:^40}'.format('CLASSIFICADOS BRASILEIRÃO'))
print('='*45)
print('\n→ OS 5 PRIMEIROS COLOCADOS: ',', '.join(times_exibição[0:5]),end='\n') # (A)
print('\n→ OS 4 ULTIMOS COLOCADOS: ',', '.join(times_exibição[-4:]),end='\n') # (B)'''
print('\n→ TODOS OS TIMES EM ORDEM ALFABÉTICA ⇩⇩⇩⇩⇩⇩\n') # (C)

times_alfabetizados = sorted(times_exibição)

for t in range (0,len(times_alfabetizados),1): # (C)
    print('→',''.join(times_alfabetizados[t:t+1]))

'''chap = times.index('CHAPECOENSE') + 1
print(f'\nO time CHAPECOENSE está na {chap}° posição da tabela\n')'''

while True: # (D)
    time = str(input('\nQuer saber a posição de qual time? ')).capitalize()
    if time in times:
        posição = times.index(time) + 1
        print(f'\nO time {time} está na {posição}° posição da tabela.')
        print('='*45)
        break
    else:
        print(f'\nO time {time} não está dentre os 20 primeiros colocados.')
        print('-'*15)