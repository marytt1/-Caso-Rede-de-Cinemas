import sqlite3

def init_db():
    conn = sqlite3.connect('cinema.db')
    cursor = conn.cursor()
    # Filmes
    cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT,
                        duracao INTEGER,
                        em_cartaz INTEGER)''')
    
    # Sessões
    cursor.execute('''CREATE TABLE IF NOT EXISTS sessoes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        filme_id INTEGER,
                        sala_id INTEGER,
                        horario_inicio DATETIME,
                        horario_fim DATETIME,
                        FOREIGN KEY(filme_id) REFERENCES filmes(id))''')
    