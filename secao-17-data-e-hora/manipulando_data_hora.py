"""
MANIPULANDO DATA E HORA

Python tem um módulo buit-in para se trabalhar com data e hora chamado datetime
"""
import datetime
print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2020-02-06 20:49:15.144012  BR 06/02/2020

# datetime.datetime.(year, month, day, hour, minute, second, microsecond
print(repr(datetime.datetime.now()))

# replace() para fazer ajuste da data/hora
inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 secundos, 0 microsegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

evento = datetime.datetime(2021, 1, 1, 0)

print(type(evento))

print(evento)

# Recebendo dados do usuário e convertendo para data
nasc = input('Informe sua data de nascimento(dd/mm/yyyy): ')

print(type(nasc))
print(nasc)

nasc = nasc.split('/')
print(type(nasc))
print(nasc)

nasc = datetime.datetime(int(nasc[2]), int(nasc[1]), int(nasc[0]))

print(type(nasc))
print(nasc)

# Acesso individual dos elementos data/hora
agora = datetime.datetime.now()

print(agora.year)
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.second)
print(agora.microsecond)
