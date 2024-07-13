from _pydatetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-07-12 19:13"
mascara_ptbr = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y-%m-%d %H: %M"

print(data_hora_atual.strftime(mascara_ptbr))
print(type(data_hora_str))


print("strptime, Não esta funcioando")
#data_convertida = datetime.strptime(data_hora_str, mascara_en)
#print(data_convertida)
#print(type(data_convertida))