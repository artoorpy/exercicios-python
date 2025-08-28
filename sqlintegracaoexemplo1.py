import sqlite3 #########CRIEI O BANCO DE DADOS E A TABELA#########


conn = sqlite3.connect('example.db')
cursor = conn.cursor()

create_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
'''

cursor.execute(create_table)

conn.commit()

conn.close()    


#########INSERI UM NOVO PRODUTO#########

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

novo_produto = ('Caneta', 1.50, 100)
inserir_produto = "INSERT INTO products (name, preco, estoque) VALUES (?, ?, ?);"
cursor.execute(inserir_produto, novo_produto)
conn.commit()
conn.close()


#########CONSULTEI TODOS OS PRODUTOS#########

conn = sqlite3.connect('example.db')
cursor = conn.cursor()     
consulta_todos = "SELECT * FROM products;"
cursor.execute(consulta_todos)
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
conn.close()

###########ATUALIZEI UM PRODUTO#########
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()  
novo_preco = 2.00
produto_id = 1  
atualizar_produto = "UPDATE products SET preco = ? WHERE id = ?;"
cursor.execute(atualizar_produto, (novo_preco, produto_id))
conn.commit()
conn.close()