"""
POO - PROPRIEDADES (PROPERTIES)

Em linguagem de programação como JAVA, ao declararmos atributos privados nas classes, costumamos criar métodos públicos
para manipulação desses atributos. Esses métodos são conhecidos por getters e setters, onde os getters retornam o valor
do atributo e setters alteram o valor do mesmo

EXEMPLOS JAVA (getters - setters)

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'O cliente {self.__titular} tem um saldo de {self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Jonas', 2000, 2000)

conta2 = Conta('Francielle', 5000, 5000)

print(conta1.extrato())
print(conta2.extrato())

saldo_total = conta1._Conta__saldo + conta2._Conta__saldo  # Acessando de forma Incorreta

soma_saldo = conta1.get_saldo() + conta2.get_saldo()

print(f'O saldo total das contas: {saldo_total}')  # Forma Incorreta

print(f'O saldo todal das contas (forma correta): {soma_saldo}')
"""


# Refatorando utilizando propriedades
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'O cliente {self.__titular} tem um saldo de {self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property  # Criando uma função como propriedade
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Jonas', 2000, 2000)

print(conta1.__dict__)

print(conta1.limite)

conta1.limite = 5000

print(conta1.__dict__)

print(conta1.valor_total)
