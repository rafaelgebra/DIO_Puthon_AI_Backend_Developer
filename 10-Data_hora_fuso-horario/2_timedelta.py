from _pydatetime import datetime, timedelta, date, time

data_atual = datetime.now()
tipo_carro = "P" #P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"Carro chegou: {data_atual} e ficará pronto às {data_estimada}") 
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"Carro chegou: {data_atual} e ficará pronto às {data_estimada}") 
else:
    data_estimada = data_atual - timedelta(minutes=tempo_grande)
    print(f"Carro chegou: {data_atual} e ficará pronto às {data_estimada}") 

print(date.today() - timedelta(days=1))

resultado = data_atual - timedelta(hours=1)
print(resultado.time())
print(resultado.date())