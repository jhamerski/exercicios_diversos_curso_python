"""
TRY EXCEPT

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare
de funcionar e o usuário receba mensagens de erros inerperados.

A forma geral mais simples é:
try:
    //Execução problemática
except:
    //O que deve ser feito em caso de problemas
"""
# Tratando erro genérico
try:
    jonas()
except:
    print('Deu algum problema!')
# Tente executar a função jonas(), caso você encontre erro, imprima a mensagem
# OBS: Tratar erro de forma genérica, não é a melhor forma para ser tratado o erro. Sempre tratar de forma específica

# Tratando um erro específico
try:
    jonas()
except NameError:
    print('Você está utilizando uma função inexistente!')

# Tratando um erro específico, com detalhe do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamento de erro de uma vez
try:
    # len(5)
    # jonas()
    print('jonas'[10])
except TypeError as erra:
    print(f'Deu TypeError: {erra}')
except NameError as errb:
    print(f'Deu NameError: {errb}')
except:
    print('Deu um erro diferente!')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': 'Jonas'}
print(pega_valor(dic, 'nome'))
dic = {'nome': 'Jonas'}
print(pega_valor(dic, 'outro'))
