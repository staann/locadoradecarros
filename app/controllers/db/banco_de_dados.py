import sqlite3
from pathlib import Path
from app.models.carro import Carro


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'carros'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
# SQL

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

'''
cursor.execute("""
#   CREATE TABLE IF NOT EXISTS aluguel
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_carro INTEGER, 
    id_cliente INTEGER,
    data_inicial date,
    data_final date,
    valor_total REAL,
    FOREIGN KEY (id_carro) REFERENCES carros (id)
    )
""")
'''
connection.commit()

cursor.close()
connection.close()

def inserir_alterar_carro(carro: Carro):
  
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    params = (carro.marca, carro.modelo, carro.ano, carro.categoria, carro.preco_por_dia, carro.status)

    #Se tiver id entao trata-se de uma alteracao
    if carro.id: 
        cursor.execute(
            f'update carros set marca=?, modelo=?, ano=?,categoria=?, diaria=?, status=? Where id='+carro.id, params
        )
    else:
        cursor.execute(
            f'INSERT INTO carros (marca, modelo, ano,categoria, diaria, status) VALUES (?, ?, ?, ?, ?, ?)', params
        )


    connection.commit()
    
    #cursor.execute('SELECT MAX(id) FROM carros')
    #max_id = cursor.fetchone()[0]
    #carro_novo.id = max_id
    #print(f'id:{carro_novo.id}, marca:{carro_novo.marca}')

    cursor.close()
    connection.close()

def obtem_lista_carros():
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




'''
marca,modelo,ano,categoria,precoPorDia,status'''