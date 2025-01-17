class Carro:
    def __init__(self,marca,modelo,ano,categoria,precoPorDia,status,historicoAluguel=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        #self.placa = placa
        self.categoria = categoria
        self.preco_por_dia= precoPorDia
        self.status = status
        #self.historico_aluguel = []

    def listar_historico(self):
        return(self.historico_aluguel)