# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []
cont = 0
# TODO: Crie um loop para solicita os itens ao usuário:
while cont <= 2:
  
# TODO: Solicite o item e armazena na variável "item":
  item = str(input("Quais os itens? "))
# TODO: Adicione o item à lista "itens":
  itens.append(item)
  cont += 1

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
