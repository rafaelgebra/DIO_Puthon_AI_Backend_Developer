# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(opcao):
  


  # TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
  if opcao < 10:
    # TODO: Retorne o plano de internet adequado:
    return "Plano Essencial Fibra - 50Mbps"
    
  elif opcao < 20:
    # TODO: Retorne o plano de internet adequado:
    return "Plano Prata Fibra - 100Mbps"
    
  else:
    # TODO: Retorne o plano de internet adequado:
    return "Plano Premium Fibra - 300Mbps"
  

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Qual o seu consumo médio mensal de dados"))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
