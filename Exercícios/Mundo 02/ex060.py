'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
from math import factorial as fa
from tkinter import *
from random import randint as rd
def calcular_fatorial():
    try:    
        numero = rd(1,40)
        
        num_fac = fa(numero)
        resultado.config(text =f'O fatorial de {numero} é > {num_fac}')
    except ValueError:
        resultado.config(text=f'Por favor, insira um número inteiro válido!')

# Criar janela
window = Tk()
window.title('Calculadora de Fatorial')

azul_real = '#4169E1'
window.configure(bg=azul_real)

# Widgets
label_numero = Label(window, text='Digite um número inteiro: ',bg=azul_real, fg='white')
label_numero.pack(pady=10)


calc_bnt = Button(window, text='Calcular!', command=calcular_fatorial)
calc_bnt.pack(pady=5)

resultado  = Label(window, text='Resultado aqui!', bg=azul_real, fg='lightgray')
resultado.pack(pady=10)

window.mainloop()