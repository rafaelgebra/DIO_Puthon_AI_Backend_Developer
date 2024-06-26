class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim plim... ")

    def parar(self):
        print("Parando")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummmmmm...")

    def get_cor(self):
        return self.cor

    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 170)
b2.buzinar()
print(b2.get_cor())
print(b2.cor)
print(b2)

