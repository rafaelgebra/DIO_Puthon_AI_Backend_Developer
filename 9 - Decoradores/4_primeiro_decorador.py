def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
        print()

    return envelope

def ola_troxa():
    print("Olá Troxa!")

print("Ex1: Decorador")
ola_troxa = meu_decorador(ola_troxa)
ola_troxa()

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
        print()

    return envelope

@meu_decorador
def ola_troxa():
    print("Olá Troxa!")

#ola_troxa1 = meu_decorador(ola_troxa)
print("Ex2: Decorador - AÇUCAR-SINTAX")
ola_troxa()

