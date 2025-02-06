from flask import *
from app.models.carro import Carro
from app.models.locadora import Locadora
from app.models.usuario import Usuario


#    Carro("Toyota", "Corolla", 2020, 'economica',150.00,True,15),
#    Carro("Honda", "Civic", 2021,'economica',125.00,False,27),
#    Carro("BWM", "W3", 2019,'luxo',345.00,False,34),
#    Carro("Audi", "XZ", 2022,'luxo',312.00,True,45)
#]

class Application():

    def __init__(self):
        self.pages = { 'carros': self.carros, 'home': self.home, 
        'cadastrar_carro': self.cadastrar_carro, 'processar_cadastro_carro': self.processar_cadastro_carro,
        'processar_exclusao_carro': self.processar_exclusao_carro, 'login_page': self.login_page,
        'paginaCadastro': self.paginaCadastro, 'paginaEsqueceuSenha' : self.paginaEsqueceuSenha,
        'processar_cadastro' : self.processar_cadastro_usuario
        }


    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
           return content(parameter)


    def helper(self):
        return render_template('helper.html')
    
    def carros(self):
        lista_carros = Locadora.listar_carros()
        return render_template('carros.html',carros=lista_carros)
    
    
    def home(self):
        return render_template('home.html')


    def cadastrar_carro(self,id=None):
        print(f'O id é {id}')
        #Se id for none estamos cadastrando novo carro.    
        if id:
            carro_para_alterar = Locadora.obtem_carro_por_id(id)
            print(carro_para_alterar)
            return render_template('form_cadastro_carro.html',carro=carro_para_alterar)
        else:
            carro=Carro(0,"","","","",0.0,True)
            return render_template('form_cadastro_carro.html',carro=carro)
    
    def processar_cadastro_carro(self):

        id = request.form.get('id')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        ano = int(request.form.get('ano'))
        categoria = request.form.get('categoria')
        preco_diaria = float(request.form.get('preco_diaria'))
        disponivel = True if request.form.get('disponivel') == 'on' else False

        if id !="0":
            carro = Carro(id,marca,modelo,ano,categoria,preco_diaria,disponivel)
        else:
            carro = Carro(None,marca,modelo,ano,categoria,preco_diaria,disponivel)
 
        Locadora.cadastrar_carro(carro)
        return redirect('/carros')
    
    def processar_exclusao_carro(self,id):
        Locadora.excluir_carro(id)
        return redirect('/carros')
    
    def login_page(self):
        return render_template('login_page.html')
    
    def paginaCadastro(self):
        return render_template('paginaCadastro.html')
    
    def processar_cadastro_usuario(self):
        usuario = request.form.get('username')
        email = request.form.get('email')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirmaSenha')

        if Locadora.comparar_usuario(usuario) == False:
            flash('escolha outro nome de usuario !','danger')
            return redirect(url_for('cadastro'))
        
        elif Locadora.comparar_email(email) == False:
            flash('email já em uso !','danger')
            return redirect(url_for('cadastro'))

        elif senha != confirma_senha:
            flash('a senha tem que ser a mesma !','danger')
            return redirect(url_for('cadastro'))
        
        else:
            cadastro = Usuario(None,usuario,nome,cpf,telefone,email,senha,False)
            Locadora.cadastrar_usuario(cadastro)
            return redirect(url_for('menu'))
    
    def paginaEsqueceuSenha(self):
        return render_template('paginaEsqueceuSenha.html')