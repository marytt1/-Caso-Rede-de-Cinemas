from datetime import datetime, timedelta

class SessaoService:
    def __init__(self, repository):
        self.repo = repository

    def agendar(self, filme_id, sala_id, data_hora_str, duracao):
        try:
            inicio = datetime.strptime(data_hora_str, "%d-%m-%Y %H:%M")
        except ValueError:
            return False, "Erro: Formato de data inválido! Use DD-MM-AAAA HH:MM"

        fim = inicio + timedelta(minutes=duracao)
        intervalo = timedelta(minutes=20) 

        sessoes_existentes = self.repo.buscar_conflitos(sala_id)

        for s_ini_str, s_fim_str in sessoes_existentes:
            existente_ini = datetime.fromisoformat(s_ini_str)
            existente_fim = datetime.fromisoformat(s_fim_str)

            if not (fim + intervalo <= existente_ini or inicio >= existente_fim + intervalo):
                return False, f"Erro: Conflito! Sala ocupada até {existente_fim.strftime('%H:%M')} + 20min limpeza."

        from model.sessao import Sessao
        nova_sessao = Sessao(filme_id, sala_id, inicio, fim)
        self.repo.salvar(nova_sessao)
        return True, "Sessão agendada com sucesso!"