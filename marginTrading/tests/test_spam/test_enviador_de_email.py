from marginTrading.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():       #verifica se remetente do email se encontra no conteudo do mesmo
    enviador = Enviador()
    resultado = enviador.enviar('marsamb@gmail.com','eth0.cybersec@gmail.com','Curso Python Pro','Excelente curso de Python')
    assert 'marsamb@gmail.com' in resultado
