"""
TRY - EXCEPT - ELSE - FINALLY

Dica:
    - TODA ENTRADA DE DADOS DEVE SER TRATADA.

else() -> É executado somente se não ocorrer o erro. Para cada except(), podemos ter um else()
finally() -> É SEMPRE executado, independente se houve exceção ou não. Geralmente é utilizado para fechar ou desalocar
recursos.
"""
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')

# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally!')


# Exemplo mais complexo ERRADO
def dividir(a, b):
    return a / b

try:
    a = float(input('Informe o primeiro valor: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    b = float(input('Informe o segundo valor: '))
except ValueError:
    print('O valor precisa ser numérico.')

try:
    print(dividir(a, b))
except NameError:
    print('Valor incorreto.')


# Exemplo complexo CORRETO - OBS: Você é responsável pelas entradas das suas funções
def dividir_um(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return 'Valor inválido.'
    except ZeroDivisionError:
        return 'Divisão por zero é impossível de ser feita.'


a = input('Informe o primeiro valor: ')
b = input('Informe o segundo valor: ')

print(dividir_um(a, b))


# Outro exemplo (SEMI-GENÉRICO)
def dividir_um(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'


a = input('Informe o primeiro valor: ')
b = input('Informe o segundo valor: ')

print(dividir_um(a, b))
