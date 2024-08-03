nome= str(input("Digite o seu nome: "))
if nome=='Gustavo':
    print('Que nome feio, troque')
elif nome == "Gabriel" or nome=='Pedro' or nome== 'George':
    print('Lindo nome!!')
elif nome in 'Ana Claudia Jessica Juliana': 
    print("Belo nome feminino")
print(f"Tenha um bom dia {nome}!!")