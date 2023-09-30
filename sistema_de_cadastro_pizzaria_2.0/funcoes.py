import os
import sqlite3
from CRUD import *
from CRUD import Entrada_Telefone

# criando o banco de dados

def criar_banco():
    db_filename = 'bancoPizza.db'
    if not os.path.isfile(db_filename):
        
        # O arquivo não existe, então o criaremos
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT,
                telefone INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    else:
        # O arquivo já existe, então apenas fazemos a conexão
        conn = sqlite3.connect(db_filename)
        
def inserir_dados():
    conn = sqlite3.connect('bancoPizza.db')
    cursor = conn.cursor()
    nome = Entrada_Nome.get()
    telefone = Entrada_Telefone.get()
    cursor.execute('INSERT INTO clientes (nome, telefone) VALUES (?, ?)', (nome, telefone))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso.')

def mostrar_dados():
    conn = sqlite3.connect('bancoPizza.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    dados = cursor.fetchall()
    conn.close()

    # Limpe a lista de exibição de dados
    for row in visualizarDados.get_children():
        visualizarDados.delete(row)

    # Preencha a lista de exibição de dados
    for row in dados:
        visualizarDados.insert("", "end", values=row)