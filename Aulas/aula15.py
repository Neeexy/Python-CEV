# Aula - 15 Interrompendo Estruturas de Repetição While
num = s =0

while True:
    num = int(input('Digite um número: '))
    leave = str(input('Deseja adicionar outro número? [S/N] ')).upper().strip() [0]
    s += num
    if leave in 'N':
        break
    else:
        continue
print(f'A soma vale : {s}')