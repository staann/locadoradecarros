#from bottle import template,request,redirect
from bottle import Bottle, run, template, request, redirect, static_file
from app.models.carro import Carro
from app.controllers.db.banco_de_dados import *



#    Carro("Toyota", "Corolla", 2020, 'economica',150.00,True,15),
#    Carro("Honda", "Civic", 2021,'economica',125.00,False,27),
#    Carro("BWM", "W3", 2019,'luxo',345.00,False,34),
#    Carro("Audi", "XZ", 2022,'luxo',312.00,True,45)
#]

class Application():

    def __init__(self):
        self.pages = { 'carros': self.carros, 'home': self.home, 
        'cadastrar_carro': self.cadastrar_carro, 'processar_cadastro_carro': self.processar_cadastro_carro,
        'processar_exclusao_carro': self.processar_exclusao_carro
        }


    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
           return content(parameter)


    def helper(self):
        return template('app/views/html/helper')
    
    def carros(self):
        lista_carros = obtem_lista_carros()
        return template('app/views/html/carros',carros=lista_carros)
    
    
    def home(self):
        return template('app/views/html/home')


    def cadastrar_carro(self,id=None):
        print(f'O id é {id}')
        #Se id for none estamos cadastrando novo carro.    
        if id:
            carro_para_alterar = obtem_carro_por_id(id)
            print(carro_para_alterar)
            return template('app/views/html/form_cadastro_carro',carro=carro_para_alterar)
        else:
            carro=Carro(None,None,None,None,None,None,None)
            return template('app/views/html/form_cadastro_carro',carro=carro)
    
    def processar_cadastro_carro(self):

        id = request.forms.get('id')
        marca = request.forms.get('marca')
        modelo = request.forms.get('modelo')
        ano = int(request.forms.get('ano'))
        categoria = request.forms.get('categoria')
        preco_diaria = float(request.forms.get('preco_diaria'))
        disponivel = True if request.forms.get('disponivel') == 'on' else False

        if id:
            carro = Carro(id,marca,modelo,ano,categoria,preco_diaria,disponivel)
        else:
            carro = Carro(None,marca,modelo,ano,categoria,preco_diaria,disponivel)

        inserir_alterar_carro(carro)
        return redirect('/carros')
    
    def processar_exclusao_carro(self,id):
        excluir_carro(id)
        return redirect('/carros')