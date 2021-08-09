class Sessao:
    contador_de_id = 0                  # contador de ID para objetos criados
    usuarios = []                       # lista de usuarios

    def salvar(self, usuario):
        Sessao.contador_de_id += 1
        usuario.id = Sessao.contador_de_id

    def listar(self,usuarios):
        pass


class Conexao:
    def gerar_sessao(self):
        return Sessao()


class Usuario():
    def __init__(self,nome):
        self.nome = nome
        self.id = None                  # ID inicial do Obj criado no BD



def test_salvar_usuario():
    conexao = Conexao()                 # serve para conectar com o DB
    sessao = conexao.gerar_sessao()     # serve para salvar no DB
    usuario = Usuario(nome='Andre') 
    sessao.salvar(usuario) 
    assert isinstance(usuario.id,int)   # certifica que o usuario possui um ID e que é instancia do tipo int
    sessao.roll_back()                  # desfaz todas as operacoes realizadas no teste
    sessao.fechar()                     # fecha a sessao
    conexao.fechar()                    # fecha a conexao com o BD


def test_listar_usuario():
    conexao = Conexao()                 # serve para conectar com o DB
    sessao = conexao.gerar_sessao()     # serve para salvar no DB
    usuarios = [Usuario(nome='Andre'),Usuario(nome='Flavio')]
    for usuario in usuarios:            # salvar todos os usuarios na Lista
        sessao.salvar(usuarios)
    assert usuario == sessao.listar()   # certifica que o usuario esta na lista de usuarios
    sessao.roll_back()                  # desfaz todas as operacoes realizadas no teste
    sessao.fechar()                     # fecha a sessao
    conexao.fechar()                    # fecha a conexao com o BD
