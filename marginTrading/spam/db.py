from time import sleep


class Sessao:
    contador_de_id = 0                  # contador de ID para objetos criados
    usuarios = []                       # lista de usuarios

    def salvar(self, usuario):
        Sessao.contador_de_id += 1
        usuario.id = Sessao.contador_de_id
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def roll_back(self):        # limpa o BD depois dos testes terem sido realizados
        self.usuarios.clear()

    def fechar(self):
        pass


class Conexao:

    def __init__(self):
        sleep(1)               #espera 10 segs para rodar a conexao com o BD

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass