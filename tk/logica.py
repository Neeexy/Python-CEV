import tkinter as tk
from tkinter import messagebox

# Cores
azul_real = '#4169E1'
azul_real_claro = '#1E90FF'
teal = '#008080'
verde_floresta = '#228B22'

def somar():
    try:
        valor_1 = int(entry1.get())
        valor_2 = int(entry2.get())
        resultado = valor_1 + valor_2
        label_resultado.config(text=f"A soma dos valores inseridos é: {resultado}", bg=teal, fg="white")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

def multiplicar():
    try:
        valor_1 = int(entry1.get())
        valor_2 = int(entry2.get())
        resultado = valor_1 * valor_2
        label_resultado.config(text=f"O resultado da multiplicação é: {resultado}", bg=teal, fg="white")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

def maior():
    try:
        valor_1 = int(entry1.get())
        valor_2 = int(entry2.get())
        resultado = max(valor_1, valor_2)
        label_resultado.config(text=f"O maior valor entre os inseridos é: {resultado}", bg=teal, fg="white")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

def inserir_novos():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_resultado.config(text="", bg=teal)

def sair():
    root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Tkinter")
root.geometry("400x300")
root.configure(bg=azul_real)

# Widgets
label1 = tk.Label(root, text="Digite o primeiro valor:", bg=azul_real_claro, fg="white")
label1.pack(pady=5)

entry1 = tk.Entry(root, bg="white", fg="black")
entry1.pack(pady=5)

label2 = tk.Label(root, text="Digite o segundo valor:", bg=azul_real_claro, fg="white")
label2.pack(pady=5)

entry2 = tk.Entry(root, bg="white", fg="black")
entry2.pack(pady=5)

button_somar = tk.Button(root, text="Somar", command=somar, bg=verde_floresta, fg="white")
button_somar.pack(pady=5)

button_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar, bg=verde_floresta, fg="white")
button_multiplicar.pack(pady=5)

button_maior = tk.Button(root, text="Maior", command=maior, bg=verde_floresta, fg="white")
button_maior.pack(pady=5)

button_novos = tk.Button(root, text="Inserir Novos Números", command=inserir_novos, bg=verde_floresta, fg="white")
button_novos.pack(pady=5)

button_sair = tk.Button(root, text="Sair", command=sair, bg=teal, fg="white")
button_sair.pack(pady=5)

label_resultado = tk.Label(root, text="", bg=teal, fg="white")
label_resultado.pack(pady=5)

root.mainloop()
