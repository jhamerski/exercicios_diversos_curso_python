"""
POO - HERANÇA (INHERITANCE)

A idéia de herança é de reaproveitar código. Também estender nossas classes

OBS: Com a herança, a partir de uma classe existente, nós estendemos outra classe que passa a herdar atributos e métodos
da classe herdada

Cliente:                        Funcionário:
    - nome                          - nome
    - sobrenome                     - sobrenome
    - cpf                           - cpf
    - renda                         - matricula


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cli = Cliente('Jonas', 'Hamerski', '123.456.789-00', 1000.00)

func = Funcionario('Francielle', 'Barreto', '987.654.321-00', 320200)

print(cli.nome_completo())
print(func.nome_completo())

OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica
Quando uma classe herda de outra classe, ela é chamada de:
    [Cliente or Funcionário]
    - Sub Classe
    - Classe filha
    - Classe Específica

Sobrescrita de métodos (Overrinding)
Ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes filhas

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self,nome, sobrenome, cpf, renda):
        # super().__init__(nome, sobrenome, cpf)
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da Super Classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma COMUM de acessar dados da Super CLasse
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())  # Acessando a super classe
        return f'Nome: {self._Pessoa__nome}, Matrícula: {self.__matricula}'


cli = Cliente('Jonas', 'Hamerski', '123.456.789-00', 1000.00)

func = Funcionario('Francielle', 'Barreto', '987.654.321-00', 320200)

print(cli.nome_completo())
print(func.nome_completo())

print(cli.__dict__)
print(func.__dict__)

# Sobrescrita de métodos (Overrinding)



