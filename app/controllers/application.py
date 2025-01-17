from bottle import template,request,redirect
from app.models.carro import Carro

lista_carros = [
    Carro("Toyota", "Corolla", 2020, 'economica',150.00,True),
    Carro("Honda", "Civic", 2021,'economica',125.00,False),
    Carro("BWM", "W3", 2019,'luxo',345.00,False),
    Carro("Audi", "XZ", 2022,'luxo',312.00,True)
]

class Application():

    def __init__(self):
        self.pages = { 'carros': self.carros, 'menu': self.menu, 
        'cadastrar_carro': self.cadastrar_carro, 'processar_cadastro_carro': self.processar_cadastro_carro
        }


    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()


    def helper(self):
        return template('app/views/html/helper')
    
    def carros(self):
        return template('app/views/html/carros',carros=lista_carros)
    
    def menu(self):
        return template('app/views/html/menu')


    def cadastrar_carro(self):
        return template('app/views/html/form_cadastro_carro')
    
    def processar_cadastro_carro(self):
        #id = request.forms.get('id')
        marca = request.forms.get('fabricante')
        modelo = request.forms.get('modelo')
        ano = int(request.forms.get('ano'))
        categoria = request.forms.get('categoria')
        preco_diaria = float(request.forms.get('preco_diaria'))
        disponivel = True if request.forms.get('disponivel') == 'on' else False
        
        # Adiciona o novo carro à lista
        novo_carro = Carro(marca, modelo, ano,categoria, preco_diaria, disponivel)
        lista_carros.append(novo_carro)

        return redirect('/carros')