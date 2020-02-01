"""
POO - CLASSES

Classes -> Nada mais são do que modelos dos objetos do mundo real, sendo representados computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle de lâmpadas da sua casa

CLasses podem conter:
    - Atributos: representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados dos objetos. No caso da lâmpada, possivelmente iríamos querer saber se a lâmpada é 110
    ou 220 volts, se ela é branca, amarela, vermelha, ..., qual é a luminosidade dela e etc

    - Métodos (funções): representam os comportamentos do objeto, ou seja, as ações que esse objeto podem realizar no
    seu sistema. No caso da Lâmpada, por exemplo, um comportamento comum que muito provavelmente iriamos querer
    representar no nosso sistema é o de ligar ou desligar a mesma.


Em Python, para definir uma classe utilizamos a palavra reservada 'class'

OBS: Utilizamos a palavra 'pass' em Python, quando temos um bloco de código que ainda não está implementado

OBS: Quando nomeamos NOSSAS CLASSES em Python utilizamos em convenção o nome com inicial em maiúsculo. Se o nome for
composto, utiliza-se a inicial de ambas palavras em maíusculo, todas juntas.

DICA!
    - Em programação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes de classes,
    atributos, metodos, arquivos, diretorios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamaos esses objetos
que serão mapeados para classes de entidade, exemplo: lampada, produto, Conta Corrente são entidades
"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass

