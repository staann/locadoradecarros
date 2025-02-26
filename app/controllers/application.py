from flask import *
from app.models.carro import Carro
from app.models.locadora import Locadora
from app.models.usuario import Usuario
from app.models.aluguel import Aluguel
from datetime import datetime


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
        'processar_cadastro' : self.processar_cadastro_usuario, 'pagina_aluguel' : self.pagina_aluguel,
        'processar_aluguel' : self.processar_aluguel, 'lista_historico': self.lista_historico,
        'processar_devolucao' : self.processar_devolucao, 'perfil': self.perfil,
        'alterar_informacoes_usuario' : self.alterar_informacoes_usuario, 
        'processar_alteracao_informacoes_usuario' : self.processar_alteracao_informacoes_usuario

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
    
    def pagina_aluguel(self,id_carro):
        carro_para_alugar = Locadora.obtem_carro_por_id(id_carro)
        return render_template('pagina_aluguel.html',carro=carro_para_alugar)
    
    def processar_aluguel(self):
        id_carro = request.form.get('id')
        #id_usuario = request.form.get()
        data_inicio = request.form.get('data_inicio')
        data_final = request.form.get('data_final')

        id_usuario = session['usuario_logado']['id']
        aluguel = Aluguel(id_carro,id_usuario,data_inicio,data_final,'Pendente')
        Locadora.alugar(aluguel)

        return render_template('agradecimento.html',data_inicio=data_inicio)
    

    def lista_historico(self,id_carro):
        resultado = Locadora.listar_historico(id_carro)
        carro_para_alugar = Locadora.obtem_carro_por_id(id_carro)
        print(resultado)
        return render_template('historico.html',carro=carro_para_alugar, historico=resultado)

    
    def processar_devolucao(self,id):
        #id_carro=Locadora.obtem_carro_por_id(id)
        data_atual = datetime.today().strftime('%Y-%m-%d')
        print(data_atual)
        Locadora.devolver(id,data_atual)
        print(f'id = {id}')
        return redirect(url_for('carros'))
    
    def perfil(self):
        id_usuario = session['usuario_logado']['id']
        info = Locadora.obtem_informacoes_usuario(id_usuario)
        historico = Locadora.listar_historico_usuario(id_usuario)
        lista_tupla = []
        lista_objeto = []
        for i in historico:
            if isinstance(i,tuple):
                lista_tupla.append(i)
            else:
                lista_objeto.append(i)
        #print(lista_objeto)
        print(lista_tupla[0][0])
        #print(lista_tupla[0])
        #print(historico[0])
        return render_template('perfil.html', informacoes_usuario = info, historico_usuario = lista_objeto, historico_usuario_pt2 = lista_tupla)


    def alterar_informacoes_usuario(self,id):
        print(id)
        info = Locadora.obtem_informacoes_usuario(id)
        return render_template('alterar_informacoes_perfil.html', informacoes_usuario = info)
    
    def processar_alteracao_informacoes_usuario(self):
        id = request.form.get('id')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        cpf = request.form.get('cpf')
        usuario = Usuario(id,'',nome,cpf,telefone,email,0,'')
        Locadora.alterar_informacoes_usuario(usuario)
        return redirect(url_for('perfil'))