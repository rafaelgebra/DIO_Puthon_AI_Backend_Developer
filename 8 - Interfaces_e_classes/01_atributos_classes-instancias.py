class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
            self.nome = nome
            self.matricula = matricula


    def __str__(self):
          return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
      for obj in objs:
            print(obj)    


aluno_1 = Estudante("Rafael", 1)
aluno_2 = Estudante("Thatiane", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" #Variável de CLASS, modifica toda a class
aluno_2.escola = "DIO" #Variável da INSTANCIA.
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)