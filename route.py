from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response
import sqlite3


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Suas rotas aqui:
@app.route('/')
def menu(info=None):
    return ctl.render('menu')

@app.route('/carros')
def carros(info= None):
    return ctl.render('carros')

@app.route('/cadastrar_carro')
def mostra_form_cadastro_carros(info=None):
    return ctl.render('cadastrar_carro')

@app.route('/processar_cadastro_carro', method='POST')
def processar_cadastro(info=None):
    return ctl.render('processar_cadastro_carro')


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
