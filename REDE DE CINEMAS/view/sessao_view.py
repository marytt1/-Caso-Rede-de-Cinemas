class SessaoView:
    def exibir_formulario(self):
        print("\n" + "="*30)
        print("   PROGRAMAR NOVA SESSÃO")
        print("="*30)
        f_id = int(input("ID do Filme: "))
        s_id = int(input("ID da Sala: "))
        data_hora = input("Data e Hora (DD-MM-AAAA HH:MM): ")
        duracao = int(input("Duração do Filme (min): "))
        return f_id, s_id, data_hora, duracao

    def mostrar_mensagem(self, mensagem):
        print(f"\n[SISTEMA]: {mensagem}")