from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response



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
    return ctl.render('home')

@app.route('/carros')
def carros(info= None):
    return ctl.render('carros')

@app.route('/mostra_form_cadastro_carros/<id>', methods=['POST', 'GET'])
@app.route('/mostra_form_cadastro_carros')
def mostra_form_cadastro_carros(id=None):
    #Se id for none, estamos vindo da tela de cadastro de carro novo.
    #Se houver id, estamos vindo da tela de altercao
    if id:
        return ctl.render('cadastrar_carro',id)
    else:
        return ctl.render('cadastrar_carro')

@app.route('/processar_cadastro_carro', method='POST')
def processar_cadastro_carro():
    return ctl.render('processar_cadastro_carro')
        
    

@app.route('/processar_exclusao_carro/<id>', methods=['POST', 'GET'])
def processar_exclusao_carro(id):
    print(f'o id eh:{id}')
    return ctl.render('processar_exclusao_carro',id)


@app.route('/login_page')
def login():
    return ctl.render('login_page')

@app.route('/paginaCadastro')
def login():
    return ctl.render('paginaCadastro')

@app.route('/paginaEsqueceuSenha')
def login():
    return ctl.render('paginaEsqueceuSenha')


#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
