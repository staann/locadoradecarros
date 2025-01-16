from bottle import template
from app.models.carro import Carro

lista_carros = [
    Carro("Toyota", "Corolla", 2020, 'ABC-123','economica',150.00,True),
    Carro("Honda", "Civic", 2021,'EFG-456','economica',125.00,False),
    Carro("BWM", "W3", 2019,'DYU-816','luxo',345.00,False),
    Carro("Audi", "XZ", 2022,'JKL-444','luxo',312.00,True)
]

class Application():

    def __init__(self):
        self.pages = { 'carros': self.carros, 'menu': self.menu
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
