from app.controllers.application import Application
from flask import *
from flask import Flask
from flask_socketio import SocketIO, send,emit
import os
import random
from app.models.locadora import Locadora



app = Flask(__name__,template_folder='app/views/html',static_folder='app/static')
app.secret_key = "chave_secreta"
socketio = SocketIO(app)
ctl = Application()
connected_users = {}


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

@app.route('/obter_modelos/<int:id_fabricante>', methods=['GET'])
def obter_modelos(id_fabricante):
    return ctl.render('obter_modelos',id_fabricante)

@app.route('/upload_imagem/<id_carro>', methods=['GET','POST'])
def upload_imagem(id_carro):
    return ctl.render('upload_imagem',id_carro)


@app.route('/image/<int:image_id>')
def get_image(image_id):
    image = Locadora.mostrar_blob(image_id)

    if image:
        return Response(image['imagemblob'], content_type='image/jpeg')  # Se a imagem for JPEG
    else:
        return "Imagem não encontrada", 404
    

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


@app.route('/processa_cadastro', methods=['POST'])
def efetua_cadastro():
    return ctl.render('processar_cadastro_carro')


    '''
    usuario = request.form.get('username')
    email = request.form.get('email')
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')
    senha = request.form.get('senha')
    confirma_senha = request.form.get('confirmaSenha')

    if senha != confirma_senha:
        flash('a senha tem que ser a mesma !','danger')
        return redirect(url_for('cadastro'))
    
    else:
        cadastro = Usuario(None,usuario,nome,cpf,telefone,email,False,senha)
        #return redirect(url_for('menu'))
    '''


@app.route('/paginaCadastro')
def cadastro():
    return ctl.render('paginaCadastro')

#pagina de cadastro do aluguel
@app.route('/pagina_aluguel/<id>')
def aluguel_carro(id):
    return ctl.render('pagina_aluguel',id)

@app.route('/processar_aluguel', methods=['POST'])
def processar_aluguel():
    return ctl.render('processar_aluguel')

@app.route('/lista_historico/<id>', methods=['POST', 'GET'])
def lista_historico(id):
   return ctl.render('lista_historico',id)

@app.route('/processar_devolucao/<id>')
def processar_devolucao(id):
    print(f'id = {id}')
    return ctl.render('processar_devolucao',id)

@app.route('/perfil')
def perfil():
    return ctl.render('perfil')

@app.route('/alterar_informacoes_usuario/<id>', methods = ['GET'])
def alterar_informacoes(id):
    return ctl.render('alterar_informacoes_usuario',id)

@app.route('/processar_alteracao_informacoes_usuario', methods = ['POST'])
def processar_alteracao_informacoes_usuario():
    return ctl.render('processar_alteracao_informacoes_usuario')


@app.route('/cadastrar_novo_fabricante')
def cadastrar_novo_fabricante():
    return ctl.render('cadastrar_novo_fabricante')

@app.route('/processar_cadastro_novo_fabricante', methods=['POST'])
def processar_cadastro_novo_fabricante():
    return ctl.render('processar_cadastro_novo_fabricante')


@app.route('/cadastrar_novo_modelo')
def cadastrar_novo_modelo():
    return ctl.render('cadastrar_novo_modelo')

@app.route('/processar_cadastro_novo_modelo', methods = ['POST'])
def processar_cadastro_novo_modelo():
    return ctl.render('processar_cadastro_novo_modelo')


@app.route('/buscar_modelos', methods=['POST'])
def buscar_modelos():
    return ctl.render('buscar_modelos')


'''
@app.route('/agradecimento')
def agradecimento():
    # Obter a data_inicio da URL
    data_inicio = request.args.get('data_inicio')


@app.route('/paginaEsqueceuSenha')
def esqu():
    return ctl.render('paginaEsqueceuSenha')
'''
#-----------------------------------------------------------------------------


if __name__ == '__main__':
    socketio.run(app, debug=True)
    #app.run(host='0.0.0.0', port=8080, debug=True)
