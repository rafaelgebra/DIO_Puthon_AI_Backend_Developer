from _pydatetime import date, datetime, time

print("Somente Ano, Mês, Dia")
data = date(2024, 7, 1)
print(data)
print(data.today())
print()

print("Tras Ano, Mês, Dia, Hora, Minuto, Segundo, decimo_de_segundo'")
data_hora = datetime(2024, 7, 1, 10, 11, 12)
print(data_hora)
data_hora = datetime(2024, 7, 1)
print()

print("Somente Hora, minuto, segundo")
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)
hora = time()
print(hora)
