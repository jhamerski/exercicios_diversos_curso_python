"""
MÉTODOS DE DATAS E HORAS

Documentação
https://docs.python.org/3/library/datetime.html

import datetime

# Com now() podemos especificar o timezone (fuso horário)
agora = datetime.datetime.now()

print(agora)
print(type(agora))
print(repr(agora))


hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo as 00:00, utilizando o método combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(f'O sistema vai ser atualizado às {manutencao}')
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana com weekday(), os dias da semana desse método começam em 0 (segunda-feira)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

nascimento = input('Qual seu dia de nascimento? dd/mm/yyyy: ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))
if nascimento.weekday() == 0:
    print('Você nasceu em uma Segunda-Feira')
elif nascimento.weekday() == 1:
    print('Você nasceu em uma Terça-Feira')
elif nascimento.weekday() == 2:
    print('Você nasceu em uma Quarta-Feira')
elif nascimento.weekday() == 3:
    print('Você nasceu em uma Quinta-Feira')
elif nascimento.weekday() == 4:
    print('Você nasceu em uma Sexta-Feira')
elif nascimento.weekday() == 5:
    print('Você nasceu em um Sábado')
elif nascimento.weekday() == 6:
    print('Você nasceu em um Domingo')
else:
    print('O programa ficou doido...')

# Formatando datas/horas com strftime() -> String Format Time - dd/mm/yyyy hh:mm BR
hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

hoje_formatado = hoje.strftime('%d/%B/%y')

print(hoje_formatado)


def data_formatada(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    if data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    if data.month == 3:
        return f'{data.day} de Março de {data.year}'
    if data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    if data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    if data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    if data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    if data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    if data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    if data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    if data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    if data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


print(data_formatada(hoje))


from textblob import TextBlob

hoje = datetime.datetime.now()


def formatando_data(data):
    return f"{data.day} de {TextBlob(data.strftime('B')).translate(to='pt-br')} de {data.year}"


print(formatando_data(hoje))
"""
import datetime

nascido = datetime.datetime.strptime('24/03/1987', '%d/%m/%Y')

print(nascido)

data_informada = input('Informe sua data de nascimento dd/mm/yyyy: ')

# Manipulando o formato da data
data_informada = datetime.datetime.strptime(data_informada, '%d/%m/%Y')


almoco = datetime.time(12, 30, 0)
print(f'Sua hora para o almoço são às {almoco}')
