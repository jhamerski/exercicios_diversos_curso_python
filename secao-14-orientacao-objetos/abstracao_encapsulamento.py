"""
POO - ABSTRAÇÃO E ENCAPSULAMENTO

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes

Encapsular -> Cápsula

               classe
-----------------------------------
|                                 |
|      Atributos e Métodos        |
|_________________________________|

# Relembrando Atributos/Métodos privador em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado
falar()

Esses elementos privados, só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia esse acesso fora da
classe. Com Python oferece um fenômeno Name Mangling, que faz uma alteração na forma de acessar os elementos privados,
conforme _Classe__Elemento
Exemplo - Acessando elementos privados fora da classe:
    instancia._Pessoa__nome
    instancia._Pessoa__falar()

Abstração -> Em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados do
usuário


"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando
conta = Conta('Jonas Hamerski', 5000.00, 2500.00)

print(conta.numero)
print(conta.titular)
print(conta.saldo)
print(conta.limite)

conta.numero = 42
conta.titular = 'Xuxa'
conta.saldo = 9999999
conta.limite = 999999

print(conta.__dict__)
conta.extrato()
print(30 * '-=')


# Refatorando a classe
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser positivo. Valor informado {valor}')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print(f'Saque não autorizado! Você tem de saldo {self.__saldo} e limite de {self.__limite}')
        else:
            print('O valor deve ser positivo.')

    def transferir(self, valor, conta_destino):
        # Remover o valor da conta origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa a ser cobrada para cada transferência realizada

        # Adicionar valor conta destino
        conta_destino.__saldo += valor


conta = Conta('Jonas Hamerski', 5000.00, 2500.00)

conta.extrato()

print(conta._Conta__titular)  # Name Mangling (Não recomendado)

conta.depositar(1000.00)

conta.extrato()

conta.sacar(3500.00)

conta.extrato()

conta2 = Conta('Francielle Barreto', 10000.00, 5000.00)

print(30 * '-=')
conta.extrato()
conta2.extrato()

conta2.transferir(500, conta)

conta.extrato()
conta2.extrato()

