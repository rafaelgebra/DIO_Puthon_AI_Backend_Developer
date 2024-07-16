
arquivo = open("C:/Users/Rafael/Documents/GitHub/DIO_Puthon_AI_Backend_Developer/11-Manipulação/lorem.txt", "r")
print(arquivo.read()) # todo o conteudo
print()
print(arquivo.readline()) # linha a linha
print()
print(arquivo.readlines()) # retorna uma lista

# tip
#while len(linha := arquivo.readline()):
#    print(linha)
arquivo.close()
