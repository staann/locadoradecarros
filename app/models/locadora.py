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
    def listar_historico(id_carro):  #pelo id do carro
        historico = db.listar_historico(id_carro)
        return historico

    @staticmethod
    def devolver(id,data_atual):
        db.devolver(id,data_atual)
        #db.altera_data(data_atual,id)

    @staticmethod
    def obtem_informacoes_usuario(id):
        info = db.obtem_informacoes_usuario(id)
        return info
    
    @staticmethod
    def alterar_informacoes_usuario(usuario):
        db.alterar_informacoes_usuario(usuario)



    @staticmethod
    def listar_historico_usuario(id_usuario):  #pelo id do usuario
        historico = db.listar_historico_usuario(id_usuario)
        return historico
    
    @staticmethod
    def inserir_imagem(id_carro,imagem,nome_imagem):
        db.inserir_imagem(id_carro,imagem,nome_imagem)

    @staticmethod
    def mostrar_imagens(id_carro):
        x=db.mostrar_imagens(id_carro)
        return x
    
    @staticmethod
    def mostrar_blob(id_imagem):
        x=db.mostrar_blob(id_imagem)
        return x
    
    @staticmethod
    def cadastrar_fabricante(nome_fabricante):
        db.cadastrar_fabricante(nome_fabricante)

    @staticmethod
    def selecionar_fabricantes():
        return db.selecionar_fabricantes()
    

    @staticmethod
    def cadastrar_novo_modelo(id_fabricante,modelo):
        db.cadastrar_novo_modelo(id_fabricante,modelo)


    @staticmethod
    def obter_modelos_por_fabricante(id_fabricante):
        return db.obter_modelos_por_fabricante(id_fabricante)
    