#Operadores Aritméticos


'''nome = input(f"Qual é seu nome? ")
print(f" Prazer em te conhecer {nome:=^20}!")'''

n1 = int(input('Um valor: '))
n2 = int(input('Um outro valor: '))

# Operações
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2

print(f"{'Resultado de diversas operações com estes valores':|<12}")

print(f"{'Soma:':<20} {s}")
print(f"{'Multiplicação:':<20} {m}")
print(f"{'Divisão:':<20} {d:.4f}")
print(f"{'Divisão Inteira:':<20} {di}")
print(f"{'Exponenciação:':<20} {ex}")


