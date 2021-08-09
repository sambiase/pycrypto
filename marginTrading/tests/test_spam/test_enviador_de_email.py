import pytest as pytest

from marginTrading.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize('remetente', ['marsamb@gmail.com', 'exemplo@gmail.com'])
def test_remetente(remetente):  # verifica se remetente do email se encontra no conteudo do mesmo
    enviador = Enviador()
    resultado = enviador.enviar(remetente, 'eth0.cybersec@gmail.com', 'Curso Python Pro',
                                'Excelente curso de Python')
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['','marsamb'])
def test_remetente_invalido(remetente):  # verifica se remetente do email se encontra no conteudo do mesmo
    enviador = Enviador()
    with pytest.raises(EmailInvalido):   #criacao de excecao no PyTest. Verifica de o @ se encontra no email
        enviador.enviar(remetente, 'eth0.cybersec@gmail.com', 'Curso Python Pro', 'Excelente curso de Python')
