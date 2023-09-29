import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#Importando os modulos da biblioteca PIL para fazar a conversão de tipo da imagem


Tela = tk.Tk()
# Criando a varial que vai controlar a tela 

Tela.title("Sistema de Cadastro de Clientes")
# Definindo o titulo da janela criada 
Tela.config(bg="#2D5161")
# Definindo cor de fundo do sistema


Largura =Tela.winfo_screenwidth()
Altura = Tela.winfo_screenheight()

''' 
Imagem =tk.Canvas(width=Largura, height=Altura)
Imagem.pack()
# Configuração do widget Canvas

imagem_pillow = Image.open("Pizzaria-4.jpg")
# Definindo a variavel que vai abrigar a imagem.

imagem_pillow = imagem_pillow.resize((Largura,Altura),Image.ANTIALIAS)
# Definindo que a imagem dentro da variavel vai ser redimensionada para caber no tamanho da janela

imagem_tk=ImageTk.PhotoImage(imagem_pillow)
# variavel que vai ser responsavel pela conversão da imagem no tamanho suportavel pelo python

Imagem.create_image(0,0, anchor="nw", image=imagem_tk)
#Imagem sendo desenhada pelo Canvas
'''

Tela.geometry("800x450")
# Definindo o tamanho da janela
Tela.resizable(width=False, height=False)
# Definindo que a janela criada permanecera nesse estado 

Titulo = tk.Label(Tela,text="Dados Cadastrais", bg="#2D5161",fg="#000000", font=("Italic", 15, "bold")).place(x=150,y=80)

# Definindo o titulo no meio do programa
Titulo2= tk.Label(Tela,text="Funções",fg="#000000", bg="#2D5161", font=("Italic",15,"bold" )).place(x=650, y=80)

Entrada_Codigo = tk.Entry(Tela, width="10").place(x=168, y=150)
Texto_Codigo = tk.Label(Tela, text="Código:", bg="#2D5161",font="bold").place(x=100, y= 147)
# Entrada_Codigo é a caixa de texto utilizada para capturar o Código, Texto_Codigo é a mensagem simbolizando o pedido do cliente.

Entrada_Nome = tk.Entry(Tela,width="57").place(x=168, y=175)
Texto_Nome = tk.Label(Tela, text="Nome:", bg="#2D5161",font="bold").place(x=110, y= 173)
# Entrada_Nome é a caixa de texto utilizada para capturar o nome, Texto_Nome é a mensagem simbolizando o pedido do cliente.

Entrada_Endereco = tk.Entry(Tela, width="57").place(x=168, y=200)
Texto_Endereco = tk.Label(Tela, text="Endereço:", bg="#2D5161",font="bold").place(x=85, y= 197)
# Entrada_Endereco é a caixa de texto utilizada para capturar endereco, Texto_Endereco é a mensagem simbolizando o pedido do cliente.

Entrada_Cep = tk.Entry(Tela, width="12").place(x=168, y=225)
Texto_Cep = tk.Label(Tela, text="Cep:", bg="#2D5161",font="bold").place(x=122, y= 222)
# Entrada_Cep é a caixa de texto utilizada para capturar Cep, Texto_Endereco é a mensagem simbolizando o pedido do cliente.


Entrada_Telefone = tk.Entry(Tela, width="25").place(x=168, y=250)
Texto_Telefone = tk.Label(Tela, text="Telefone:", bg="#2D5161", font="bold").place(x=92, y= 247)
# Entrada_Telefone é a caixa de texto utilizada para capturar o Telefone Texto_Telefone é a mensagem simbolizando o pedido do cliente.


Entrada_Pedido = tk.Text(Tela, width="30",height="3").place(x=168, y=275)
Texto_Pedido = tk.Label(Tela, text="Pedido:", bg="#2D5161" ,font="bold").place(x=100, y= 275)
# Entrada_Pedido é a caixa de texto utilizada para capturar o Pedido, Texto_Pedido é a mensagem simbolizando o pedido do cliente.


Botao_Confirmar_Salvar= tk.Button(Tela,text = "Confirmar e Salvar", padx=9).place(x=640, y = 130)
# Botão para confirmar um pedido e salvar as informações do cliente e do pedido no banco
Botao_Alterar= tk.Button(Tela,text = "Alterar Pedido", padx=20).place(x=640, y = 160)
# Botão para alterar o pedido.
Botao_Relatorio= tk.Button(Tela,text = "Relatório do Pedido", padx=6).place(x=640, y = 190)
# Botão parar gerar um relatório pelo código do pedido.
Botao_Cancelar= tk.Button(Tela,text = "Cancelar Pedido", padx=15).place(x=640, y = 220)
# Botão para cancelar o pedido do cliente.
Botao_Deletar= tk.Button(Tela,text = "Deletar Cliente", padx=20).place(x=640, y = 250)
# Botão para deletar um cliente do sistema


tk.mainloop()