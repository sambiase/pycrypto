import pytest as pytest

from marginTrading.spam.db import Conexao


@pytest.fixture (scope='session')           #roda a fixture apenas durante a sessao e com isso nao precisa abrir varias
def conexao():                              # conexoes com o BD
    #fase de Setuo da Conexao
    conexao_obj = Conexao()                 # serve para conectar com o DB
    yield conexao_obj                       # yield retorna o valor de conexao que seja injetado nos Testes
    #etapa de Tear Down , ou seja, fechamento
    conexao_obj.fechar()                    # fecha a conexao com o BD


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao() # serve para salvar no DB
    yield sessao_obj
    sessao_obj.roll_back()                  # desfaz todas as operacoes realizadas no teste
    sessao_obj.fechar()                     # fecha a sessao