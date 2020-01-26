"""
DOCUMENTANDO FUNÇÕES COM Docstrings

OBS: Podemos ter acesso á documentação de uma função utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()
"""


# Exemplos
def diz_oi():
    """ Uma função simples que retorna a String 'Oi!'"""
    return 'Oi! '


print(diz_oi())


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou 'número' á 'potência' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'número' por 'potência'
    """
    return numero ** potencia


print(exponencial(4, 7))
