def principal():
    print("executando a função Principal")

    def funcao_interna():
        print("executando a função interna")

    def funcao_2():
        print("executando a função2")

    funcao_interna()
    funcao_2()

principal()