class SessaoController:
    def __init__(self, service):
        self.service = service

    def criar_sessao(self, filme_id, sala_id, inicio, duracao):
        return self.service.agendar(filme_id, sala_id, inicio, duracao)