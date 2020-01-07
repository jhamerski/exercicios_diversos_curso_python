"""
Faça uma função que receba a data atual (dia, mês e ano em inteiro e imprima na tela em formato textual por extenso.
Exemplo: Data:01/01/2000 - Imprimir: 1 de Janeiro de 2000
"""
d = int(input('Informe o dia: '))
m = int(input('Informe o mês: '))
a = int(input('Inform o ano: '))


def data_qualquer(dia, mes, ano):
    if mes == 1:
        return f'{dia} de Janeiro de {ano}'
    elif mes == 2:
        return f'{dia} de Fevereiro de {ano}'
    elif mes == 3:
        return f'{dia} de Março de {ano}'
    elif mes == 4:
        return f'{dia} de Abril de {ano}'
    elif mes == 5:
        return f'{dia} de Maio de {ano}'
    elif mes == 6:
        return f'{dia} de Junho de {ano}'
    elif mes == 7:
        return f'{dia} de Julho de {ano}'
    elif mes == 8:
        return f'{dia} de Agosto de {ano}'
    elif mes == 9:
        return f'{dia} de Setembro de {ano}'
    elif mes == 10:
        return f'{dia} de Outubro de {ano}'
    elif mes == 11:
        return f'{dia} de Novembro de {ano}'
    elif mes == 12:
        return f'{dia} de Dezembro de {ano}'
    else:
        return 'Mês inválido!'


print(data_qualquer(d, m, a))
