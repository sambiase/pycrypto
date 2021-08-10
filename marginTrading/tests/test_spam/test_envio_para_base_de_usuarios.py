from marginTrading.spam.enviador_de_email import Enviador
from marginTrading.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())   #sessao usada para listar usuarios buscados do BD. Eviador para enviar os emails
    enviador_de_spam.enviar_emails('andre@gmail.com.br','Teste de Email','Este é um teste enviado por email')