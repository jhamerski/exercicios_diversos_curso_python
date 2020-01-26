"""
ERROS MAIS COMUNS

ATENÇÃO!
É importante prestar atenção e aprender a ler a saída de erros geradas pela execução do nosso código

Os erros mais comuns:
 - SyntaxError: Ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não
 reconhece como parte da linguagem.
    Exemplos:
        a) def funcao:
               print('Jonas Hamerski')
        b) None = 1
        c) return

 - NameError: Ocorre quando uma variável ou função não foi definida
    Exemplos:
        a) print(Jonas)
        b) teste()
        c) a = 18
             if a < 10:
                msg = 'É maior que 10.'

            print(msg)

  - TypeError: Ocorre quando uma função/operação/ação é aplicada a um tipo errado
    Exemplos:
        a) print(len(5))
        b) print('Jonas' + [])
        c) print('Hamerski' + 5)

  - IndexError: Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
  índice inválido.
    Exemplos:
        a) lista = ['Jonas']
           print(lista[2])
           print(lista[0][7])
        b)

 - ValueError: Ocorre quando uma função ou operação built-in (integrada) recebe um argumento com tipo correto mas valor
 inapropriado.
    Exemplos:
        a) print(int('Jonas'))

 - KeyError: Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
    Exemplos:
        a) dic = {}
           print(dic['Qualquer'])

 - AttributeError: Ocorre quando uma variável não tem um atributo ou função
    Exemplos:
        a) tupla = (11, 2, 31, 4)
           print(tupla.sort())

 - IndentationError: Ocorre quando não respeitamos a indentação do Python (4 espaços)
    Exemplos:
        a) def nova():
           print('Erro de indentação)
        b) for i in range(10):
           print(i + 1)

OBS: Exception e Erros são sinônimos na programação.

Sempre ler e prestar atenção na saída de Erro.
"""