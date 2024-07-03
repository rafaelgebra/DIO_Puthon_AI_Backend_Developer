class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas #self.nro_patas é o atributo, nro_patas é a atribuição

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)



class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass



class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__) #mostra a instancia da resolução para encontrar os metodos
        print()

gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Vermelhor", cor_bico="Laranja")
print(ornitorrinco)