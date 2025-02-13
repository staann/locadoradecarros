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
        db.inserir_usuario(usuario)

    @staticmethod
    def logar_usuario(login, senha):
        usuario = db.logar_usuario(login, senha)
        return usuario
    
    @staticmethod
    def comparar_usuario(nome_usuario):
        resultado = db.comparar_usuario(nome_usuario)
        return resultado
    
    @staticmethod
    def comparar_email(email):
        resultado = db.comparar_email(email)
        return resultado


    @staticmethod
    def alugar(aluguel):
        db.alugar_carro(aluguel)


    @staticmethod
    def listar_historico(id_carro):
        historico = db.listar_historico(id_carro)
        return historico

    @staticmethod
    def devolver(id,data_atual):
        db.devolver(id,data_atual)
        #db.altera_data(data_atual,id)
