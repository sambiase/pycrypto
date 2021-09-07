from unittest.mock import Mock

import pytest as pytest

from marginTrading.spam.enviador_de_email import Enviador
from marginTrading.spam.main import EnviadorDeSpam
from marginTrading.spam.modelos import Usuario

'''
    Codigo de Testes de Envio de Spam
'''


@pytest.mark.parametrize('usuarios',
                         [
                             [
                                 Usuario(nome='Andre', email='andreteste@gmail.com'),
                                 Usuario(nome='Flavio', email='flavioeste@gmail.com')
                             ],
                             [
                                 Usuario(nome='Andre', email='andreteste@gmail.com'),
                             ]
                         ])
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)  # sessao usada para listar usuarios buscados do BD.
    # Eviador para enviar os emails
    enviador_de_spam.enviar_emails('andre@gmail.com.br', 'Teste de Email', 'Este é um teste enviado por email')
    assert len(usuarios) == enviador.enviar.call_count  # se certificar do numero de emails enviados


def test_parametros_de_spam(sessao):  # conferir todos os dados enviados no envio do email
    usuario = Usuario(nome='Andre', email='andreteste@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)  # sessao usada para listar usuarios buscados do BD.
    # Eviador para enviar os emails
    enviador_de_spam.enviar_emails('flavio@gmail.com.br', 'Teste de Email', 'Este é um teste enviado por email')
    enviador.enviar.assert_called_once_with('flavio@gmail.com.br', 'andreteste@gmail.com', 'Teste de Email',
                                            'Este é um teste enviado por email')  # se certificar do numero de emails enviados
