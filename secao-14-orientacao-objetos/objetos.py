"""
POO - OBJETOS

Objetos -> São instâncias da classe, ou seja, após o mapeamento do objeto do mundo real, para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma
classe como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_status(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é: {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos
lamp = Lampada('Branca', 220, 60)  # o self é o próprio objeto, que nesse caso é 'lamp'

#  lamp1 = Lampada() | TypeError: _requer 3 argumentos: 'cor', 'voltagem', and 'luminosidade'

lamp.ligar_desligar()

print(f'A lâmpada esta ligada? {lamp.checa_status()}')

# conta = ContaCorrente(500.00, 2500.00)

user = Usuario('Jonas', 'Hamerski', 'jonashamerski87@gmail.com', '1234')

print(type(user))

cli = Cliente('Jonas Hamerski', '123.123.123-12')

cc = ContaCorrente(5000.00, 1500.00, cli)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()  # Acessando de forma errada
