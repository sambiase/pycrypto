class EnviadorDeSpam:
    def __init__(self,sessao, enviador):
        self.enviador = enviador
        self.sessao = sessao

    def enviar_emails(self, remetente, assunto, corpo):
        for usuario in self.sessao.listar():             #para cada usuario no BD
            self.enviador.enviar(remetente,usuario.email,assunto,corpo)