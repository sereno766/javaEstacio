import sqlite3
from sqlite3 import Error

def criar_conexao(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão com SQLite estabelecida: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    
    return conn

def criar_tabelas(conn):
    try:
        c = conn.cursor()
        
        # Tabela de livros
        c.execute('''CREATE TABLE IF NOT EXISTS livros (
                     id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     preco REAL NOT NULL,
                     estoque INTEGER NOT NULL
                     )''')
        
        # Tabela de clientes
        c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                     id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                     nome TEXT NOT NULL,
                     email TEXT UNIQUE NOT NULL,
                     telefone TEXT
                     )''')
        
        # Tabela de pedidos
        c.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                     id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                     id_cliente INTEGER NOT NULL,
                     id_livro INTEGER NOT NULL,
                     quantidade INTEGER NOT NULL,
                     data_pedido TEXT DEFAULT CURRENT_TIMESTAMP,
                     FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
                     FOREIGN KEY (id_livro) REFERENCES livros (id_livro)
                     )''')
        
        print("Tabelas criadas com sucesso!")
    except Error as e:
        print(e)

def inserir_livro(conn, livro):
    sql = '''INSERT INTO livros(titulo, autor, preco, estoque)
             VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, livro)
    conn.commit()
    return cur.lastrowid

def inserir_cliente(conn, cliente):
    sql = '''INSERT INTO clientes(nome, email, telefone)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, cliente)
    conn.commit()
    return cur.lastrowid

def inserir_pedido(conn, pedido):
    sql = '''INSERT INTO pedidos(id_cliente, id_livro, quantidade)
             VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, pedido)
    conn.commit()
    
    atualizar_estoque(conn, (pedido[1], pedido[2]))
    
    return cur.lastrowid

def atualizar_estoque(conn, dados):
    sql = '''UPDATE livros SET estoque = estoque - ? 
             WHERE id_livro = ?'''
    cur = conn.cursor()
    cur.execute(sql, (dados[1], dados[0]))
    conn.commit()

def selecionar_todos_livros(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM livros")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

def selecionar_todos_clientes(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

def selecionar_todos_pedidos(conn):
    cur = conn.cursor()
    cur.execute('''SELECT p.id_pedido, c.nome, l.titulo, p.quantidade, p.data_pedido 
                   FROM pedidos p
                   JOIN clientes c ON p.id_cliente = c.id_cliente
                   JOIN livros l ON p.id_livro = l.id_livro''')
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

def main():
    database = "biblioteca.db"
    
    conn = criar_conexao(database)
    
    if conn is not None:
        criar_tabelas(conn)
        '''
        # Livros
        livro1 = ("Dom Casmurro", "Machado de Assis", 29.90, 10)
        livro2 = ("1984", "George Orwell", 35.50, 15)
        livro3 = ("O Senhor dos Anéis", "J.R.R. Tolkien", 89.90, 5)
        
        inserir_livro(conn, livro1)
        inserir_livro(conn, livro2)
        inserir_livro(conn, livro3)
        
        # Clientes
        cliente1 = ("João Silva", "joao@email.com", "(11) 99999-9999")
        cliente2 = ("Maria Souza", "maria@email.com", "(21) 98888-8888")
        
        inserir_cliente(conn, cliente1)
        inserir_cliente(conn, cliente2)
        
        # Pedidos
        pedido1 = (1, 1, 2)  # cliente 1, livro 1, quantidade 2
        pedido2 = (2, 2, 1)  # cliente 2, livro 2, quantidade 1
        pedido3 = (1, 3, 1)  # cliente 1, livro 3, quantidade 1
        
        inserir_pedido(conn, pedido1)
        inserir_pedido(conn, pedido2)
        inserir_pedido(conn, pedido3)
    
        '''
        # Consultar dados
        print("\nLivros:")
        selecionar_todos_livros(conn)
        
        print("\nClientes:")
        selecionar_todos_clientes(conn)
        
        print("\nPedidos:")
        selecionar_todos_pedidos(conn)
        
        conn.close()
    else:
        print("Erro! Não foi possível criar a conexão com o banco de dados.")

if __name__ == '__main__':
    main()