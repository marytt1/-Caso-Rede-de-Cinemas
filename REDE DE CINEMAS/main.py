from db.db_config import init_db
from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
from controller.sessao_controller import SessaoController
from view.sessao_view import SessaoView

init_db()

repo = SessaoRepository()
serv = SessaoService(repo)
ctrl = SessaoController(serv)
view = SessaoView()

f_id, s_id, inicio, duracao = view.exibir_formulario()
sucesso, msg = ctrl.criar_sessao(f_id, s_id, inicio, duracao)
view.mostrar_mensagem(msg)          