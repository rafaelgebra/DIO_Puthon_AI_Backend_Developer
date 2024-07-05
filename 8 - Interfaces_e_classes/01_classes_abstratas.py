from abc import ABC, abstractmethod, abstractproperty 


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass 
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a Tv... ")
        print("Ligada!")

    def desligar(self):
        print("Desligando a Tv... ")
        print("Desligada")

    @property
    def marca(self):
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado... ")
        print("Desligado! ")

    def desligar(self):
        print("Desligando o Ar Condicionado... ")
        print("Desligando! ")

    @property
    def marca(self):
        return "LG"


remoto = ControleTv()
remoto.ligar()
remoto.desligar()
print(remoto.marca)

remoto = ControleArCondicionado()
remoto.ligar()
remoto.desligar()
print(remoto.marca)