from app.controllers.application import Application
from flask import *
from flask import Flask
import os
from app.models.locadora import Locadora



app = Flask(__name__,template_folder='app/views/html',static_folder='app/static')
app.secret_key = "chave_secreta"
ctl = Application()



#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<path:filepath>')
def serve_static(filepath):
    return send_from_directory(os.path.join(app.root_path, 'static'), filepath)

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

@app.route('/processar_cadastro_carro', methods=['POST'])
def processar_cadastro_carro():
    return ctl.render('processar_cadastro_carro')
        
    

@app.route('/processar_exclusao_carro/<id>', methods=['POST', 'GET'])
def processar_exclusao_carro(id):
    print(f'o id eh:{id}')
    return ctl.render('processar_exclusao_carro',id)


@app.route('/login_page')
def login():
    return ctl.render('login_page')

@app.route('/efetua_login', methods=['POST'])
def efetua_login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    usuario = Locadora.logar_usuario(login, senha)

    if usuario:
        session['usuario_logado'] = usuario.to_dict()
        return redirect(url_for('menu'))
    else:
        flash('Usuário ou senha inválidos !!','danger')
        return redirect(url_for('login'))
    
@app.route("/logout")
def logout():
    session.pop("usuario_logado", None)  # Removendo o usuário da sessão
    return redirect(url_for('menu'))

'''
@app.route('/paginaCadastro')
def login():
    return ctl.render('paginaCadastro')

@app.route('/paginaEsqueceuSenha')
def login():
    return ctl.render('paginaEsqueceuSenha')
'''

#-----------------------------------------------------------------------------


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)
