import sqlite3
from pathlib import Path
from app.models.carro import Carro
from app.models.usuario import Usuario
from app.models.aluguel import Aluguel

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'carros'



# SQL

#cursor.execute('DELETE FROM usuarios WHERE id = ?',(6,))

#cursor.close()
#connection.commit()
#connection.close()
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS historico")



cursor.execute(
    f'CREATE TABLE IF NOT EXISTS carros'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'marca TEXT,'
    'modelo TEXT,'
    'ano INTEGER,'
    'categoria TEXT,'
    'diaria REAL,'
    'status BOOLEAN'
    ')'
)

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS usuarios'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'login TEXT,'
    'nome TEXT,'
    'cpf TEXT,'
    'telefone TEXT,'
    'email TEXT,'
    'admin BOOLEAN,'
    'senha TEXT'
    ')'
)



cursor.execute(
    f'CREATE TABLE IF NOT EXISTS historico'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'id_carro INTEGER,'
    'id_usuario INTEGER,'
    'data_inicio TEXT,'
    'data_final TEXT,'
    'data_devolvida TEXT'
    ')'
)

connection.commit()

cursor.close()
connection.close()



def inserir_alterar_carro(carro: Carro):
  
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (carro.marca, carro.modelo, carro.ano, carro.categoria, carro.preco_por_dia, carro.status)
    print(carro.id)

    #Se tiver id entao trata-se de uma alteracao
    if carro.id != None: 
        #sql = f'UPDATE carros set marca=?, modelo=?, ano=?,categoria=?, diaria=?, status=? WHERE id=?',(*params,carro.id)
        sql = f'update carros set marca=?, modelo=?, ano=?,categoria=?, diaria=?, status=? Where id='+carro.id, params
        print(sql)
    else:
        #sql = f'INSERT INTO carros (marca, modelo, ano,categoria, diaria, status) VALUES (?, ?, ?, ?, ?, ?)', (*params,)
        sql =  f'INSERT INTO carros (marca, modelo, ano,categoria, diaria, status) VALUES (?, ?, ?, ?, ?, ?)', params
        print(sql)
            
    cursor.execute(*sql)

    connection.commit()
    
    #cursor.execute('SELECT MAX(id) FROM carros')
    #max_id = cursor.fetchone()[0]
    #carro_novo.id = max_id
    #print(f'id:{carro_novo.id}, marca:{carro_novo.marca}')

    cursor.close()
    connection.close()

def listar_carros():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute('SELECT id,marca, modelo, ano,categoria, diaria, status FROM carros')
    linhas_db=cursor.fetchall()
#    for linha in linhas_db:
#        print(linha)
    cursor.close()
    connection.close()
    lista_carros=[Carro(*linha) for linha in linhas_db]

 #   for carro in lista_carros:
 #       print(*carro.marca)

    #print(lista_carros)
    return lista_carros

def excluir_carro(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    print(f'o id he {{id}}')
    cursor.execute('DELETE FROM carros WHERE id='+id)

    connection.commit()

    cursor.close()
    connection.close()


def obtem_carro_por_id(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute('SELECT id,marca, modelo, ano,categoria, diaria, status FROM carros Where id ='+id)
    linhas_db=cursor.fetchall()
#    for linha in linhas_db:
#        print(linha)
    cursor.close()
    connection.close()

    #linhas_db so retornara uma linha pois o id é unico.
    lista_carros=[Carro(*linha) for linha in linhas_db]

 #   for carro in lista_carros:
 #       print(*carro.marca)

    #retornamos o unico registro obtido.
    return lista_carros[0]


def logar_usuario(login, senha):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(f'SELECT id,login, nome, cpf, telefone, email, senha, admin FROM usuarios Where login = "{login}" and senha = "{senha}"')
    resultado=cursor.fetchone()
    cursor.close()
    connection.close()

    #se o resultado for valido criamos um objeto Usuario com ele. Caso contrario ficara com valor None.
    if resultado:
        usuario=Usuario(*resultado)
    else:
        usuario=None
        

    #retornamos o unico registro obtido. 
    #Caso nao encontre resultado entao usuario ou senha foram invalidos e o valor retornado sera None.
    return usuario


def inserir_usuario(dados : Usuario):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (dados.login,dados.email,dados.nome, dados.cpf,dados.telefone,dados.admin,dados.senha)
    sql = f'INSERT INTO usuarios (login, email, nome, cpf, telefone, admin ,senha) VALUES (?, ?, ?, ?, ?, ?, ?)', params
    cursor.execute(*sql)

    connection.commit()
    cursor.close()
    connection.close()

def comparar_usuario(usuario):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (usuario)
    sql = f'SELECT login FROM usuarios WHERE login = "{usuario}"'
    cursor.execute(sql)
    resultado = cursor.fetchone()
    cursor.close()
    connection.close()
    if resultado == None:
        return True
    
    else:
        return False
    
def comparar_email(email):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (email)
    sql = f'SELECT email FROM usuarios WHERE email = "{email}"'
    cursor.execute(sql)
    resultado = cursor.fetchone()
    cursor.close()
    connection.close()
    if resultado == None:
        return True
    
    else:
        return False
    
def alugar_carro(aluguel : Aluguel):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (aluguel.id_carro,aluguel.id_usuario,aluguel.data_inicio,aluguel.data_final,aluguel.data_devolvida)
    sql = f'INSERT INTO historico (id_carro,id_usuario,data_inicio,data_final,data_devolvida) VALUES (?, ?, ?, ?,?)', params
    cursor.execute(*sql)
    connection.commit()
    cursor.close()
    connection.close()

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    #params2 = (False)
    sql2 = "UPDATE carros SET status = ? WHERE id = ?"
    cursor.execute(sql2, (False, aluguel.id_carro))
    #sql2 = f'update carros set status=? WHERE id='+aluguel.id_carro, False
    #cursor.execute(*sql2)
    connection.commit()

    cursor.close()
    connection.close()


def listar_historico(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (id)
    sql = f'SELECT id_carro,id_usuario,data_inicio,data_final,data_devolvida FROM historico WHERE id_carro = "{id}"'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    connection.close()

    lista_historico=[Aluguel(*linha) for linha in resultado]
    return lista_historico
    #return resultado
    

def devolver(id,data_atual):

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    sql = "UPDATE carros SET status = ? WHERE id = ?"
    cursor.execute(sql, (True, id))
    sql2 = "UPDATE historico SET data_devolvida = ? WHERE id_carro = ? AND data_devolvida = 'Pendente' "
    cursor.execute(sql2, (data_atual, id))
    connection.commit()
    cursor.close()
    connection.close()

'''def altera_data(data,id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    sql = "UPDATE historico SET data_devolvida = ? WHERE id = ? "
    cursor.execute(sql, (data, id))
    connection.commit()
    cursor.close()
    connection.close()
'''


'''
def devolver(id):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    sql = (f'SELECT id_usuario FROM historico WHERE id_usuario = "{id}" ORDER BY ROWID DESC LIMIT 1') 
    cursor.execute(sql)

    
--------------------
    cursor.execute('SELECT id,marca, modelo, ano,categoria, diaria, status FROM carros')
    linhas_db=cursor.fetchall()
#    for linha in linhas_db:
#        print(linha)
    cursor.close()
    connection.close()
    lista_carros=[Carro(*linha) for linha in linhas_db]

 #   for carro in lista_carros:
 #       print(*carro.marca)

    #print(lista_carros)
    return lista_carros

'''