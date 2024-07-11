def meu_gerador(numeros: list[int]):
    #contador += 1
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3, 4,]):
    print(i)