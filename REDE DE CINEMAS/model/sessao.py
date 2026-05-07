class Sessao:
    def __init__(self, filme_id, sala_id, inicio, fim, id=None):
        self.id = id
        self.filme_id = filme_id
        self.sala_id = sala_id
        self.inicio = inicio
        self.fim = fim