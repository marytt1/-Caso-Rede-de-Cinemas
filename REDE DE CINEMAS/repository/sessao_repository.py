import sqlite3
from datetime import datetime

class SessaoRepository:
    def buscar_conflitos(self, sala_id):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute("SELECT horario_inicio, horario_fim FROM sessoes WHERE sala_id = ?", (sala_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def salvar(self, sessao):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sessoes (filme_id, sala_id, horario_inicio, horario_fim) VALUES (?, ?, ?, ?)",
                       (sessao.filme_id, sessao.sala_id, sessao.inicio.isoformat(), sessao.fim.isoformat()))
        conn.commit()
        conn.close()