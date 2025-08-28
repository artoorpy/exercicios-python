import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()  
cursor.execute('''
CREATE TABLE IF NOT EXISTS contatos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
               email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                )
''')
dados_exemplo = [
    ('Alice', 'alice@gmai.com', '123456789'),
    ('Bob', 'bob@gmail.com', '987654321'),
    ('Charlie', 'charlie@gmail.com', '555666777'),
]

cursor.executemany('INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()

####LEITURA E EXIBIÇÃO DOS DADOS####
cursor.execute('SELECT * FROM contatos')    
contatos = cursor.fetchall()
print("Contatos na base de dados:")
for contato in contatos:
    print(contato)

    ###############atualização de dados###############

novo_telefone ='111222333'
contato_id = 2 
cursor.execute('UPDATE contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()