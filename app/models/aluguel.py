#from carro import Carro
#from locadora import Locadora

class Aluguel:
    def __init__(self,id_carro,id_usuario,data_inicio,data_fim,data_devolvida='Pendente'):
        #super().__init__(marca,modelo,ano,categoria,precoPorDia,status)
        #super().__init__()
        self.id_carro = id_carro
        self.id_usuario = id_usuario
        self.data_inicio = data_inicio
        self.data_final = data_fim
        self.data_devolvida = data_devolvida

