"""
LEVANTANDO OS PRÓPRIOS ERROS COM RAISE

raise -> Lança exceções

OBS: O raise NÃO é uma função, raise é uma palavra reservada, assim como def ou qualquer outra em Python

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro
A forma geral de utilização é:
    -raise TipoDoErro('Mensagem de erro')

OBS: O raise assim como return finaliza a função, ou seja, nada após o raise é executado
"""


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('O texto precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Jonas', 'vermelho')
# colore(1, 'azul')


def colore_outro(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('O texto precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa uma entre: {cores}')
    print('Depois do raise. Nunca será executado.')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore_outro('Hamerski', 'vermelho')
