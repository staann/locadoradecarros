from app.controllers.db import banco_de_dados as db

class Locadora:

    def __init__(self):
        ...

    @staticmethod
    def cadastrar_carro(carro):
        db.inserir_alterar_carro(carro)

    @staticmethod
    def excluir_carro(id):
        db.excluir_carro(id)

    @staticmethod
    def obtem_carro_por_id(id):
        carro = db.obtem_carro_por_id(id)
        return carro

    @staticmethod
    def listar_carros():
        lista_carros = db.listar_carros()
        return lista_carros

    @staticmethod
    def cadastrar_usuario(usuario):
        ...

    @staticmethod
    def logar_usuario(login, senha):
        usuario = db.logar_usuario(login, senha)
        return usuario


