class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    
    @classmethod #Método de CLASSE
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    

    @staticmethod #Método ESTÁTICO
    def e_maior_idade(idade):
        return idade >= 18
    

p = Pessoa.criar_de_data_nascimento(1988, 27, 8, "Rafael")
print(p.nome, p.idade)