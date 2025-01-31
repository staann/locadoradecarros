class Usuario:

    def __init__(self,id,login,nome,cpf,telefone,email,senha,admin=False):
        self.id = id
        self.login = login
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.admin = admin
        self.senha = senha


    # Retorna um dicionário JSON-friendly
    def to_dict(self):
        return {"id" : self.id, "login": self.login, "nome": self.nome,
                "cpf" : self.cpf, "telefone": self.telefone, "email": self.email, 
                "admin": self.admin, "senha": self.senha}  
