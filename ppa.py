'''def print_animado(msg,time=0.03):
    for letra in msg:
        print(letra,end='',flush=True)
        sleep(time)
from time import sleep'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

for numero in range(0,6,2):
    print(numeros[numero:numero+2]) # no primeiro loop numero-1 = 0, numero-2 = 2

# loop 1º [0:2] = 1,2,3 (3 = ele-2 não aparece) loop 2º [2:4] = 3,4,5 (5 = ele-4 não aparece)...
print('='*20)

print(numeros[0:2])
print(numeros[2:4])
print(numeros[4:6])
print('='*20)
for numero in range(0,6,2):
    print(numeros[numero:numero+2])

print('='*20)

print(numeros[0:2])
print(numeros[2:4]) # +2
print(numeros[4:6]) # +2