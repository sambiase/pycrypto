from marginTrading.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Andre')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)   # certifica que o usuario possui um ID e que é instancia do tipo int



def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Andre'), Usuario(nome='Flavio')]
    for usuario in usuarios:            # salvar todos os usuarios na Lista
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()  # certifica que o usuario esta na lista de usuarios
