"""
POO MÉTODOS

Métodos (Funções) -> Representam os comportamentos do objeto, ou seja, a ações que este objeto pode realizar no seu
sistema

Em Python dividimos os métodos em dois grupos: Métodos de Instância e Métodos de Classe

O método dender init (__init__) é um método especial chamado de construtor e sua função é construir o objeto a partir da
classe

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

Os métodos /funções dunder em Python são chamados de métodos mágicos

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline
"""
# MÉTODOS DE INSTÂNCIA


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

"""
from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # 200 mil embaralhamento com tamanho 16

    # Não é recomendado criar métodos utilizando dunder, pois o Python já possui vários métodos com essa forma.
    def __correr__(self, metros):
        print(f'{self.__nome} está correndo {metros} metros.')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


p1 = Produto('PlayStation 4', 'Video Game', 2300)

print(p1.desconto(10))
print(Produto.desconto(p1, 50))

user = Usuario('Jonas', 'Hamerski', 'jonashamerski87@gmail.com', '1234')
user1 = Usuario('Angelina', 'Jolie', 'aj@gmail.com', '4321')

print(user.nome_completo())
print(Usuario.nome_completo(user))

print(user1.nome_completo())

print(f'Senha user = {user._Usuario__senha}')  # Acessando de forma inválida
print(f'Senha user1 = {user1._Usuario__senha}')  # Acessando de forma inválida

nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
email = input('Informe seu email: ')
senha = input('Informe sua senha: ')
confirma_senha = input('Confirmação de senha: ')

if senha == confirma_senha:
    user3 = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere!')
    exit(1)

print('Usuário Criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user3.checa_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')

print(f'Senha User3 Criptografada: {user3._Usuario__senha}')  # Acessando de forma errada
"""
from passlib.hash import pbkdf2_sha256 as cryp


# MÉTODOS DE CLASSE em Python são conhecidos como métodos estáticos em outras linguagens
# Refatorando
class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema!')

    @classmethod
    def ver(cls):
        print('Teste')

    # Método Estático
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # 200 mil embaralhamento com tamanho 16
        Usuario.contador = self.__id
        print(f'Usuário criado {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def ver(self):  # Como não fazemos acesso a nenhum atributo de instância, o ideal é fazer um MÉTODO DE CLASSE
        print('Teste')

    # Método privado
    def __gera_usuario(self):
        return self.__email.split('@')[0]  # jonashamerski87@gmail.com ['jonashamerski87', 'gmail.com']


user5 = Usuario('Jonas', 'Hamerski', 'jonashamerski87@gmail.com', '1234')

Usuario.conta_usuario()  # Foma correta

user5.conta_usuario()  # Possível, porém incorreto

user6 = Usuario('Jonas', 'Hamerski', 'jonashamerski87@gmail.com', '1234')

# MÉTODO ESTÁTICO
print(Usuario.contador)
print(Usuario.definicao())

user7 = Usuario('Jonas', 'Hamerski', 'jonashamerski87@gmail.com', '1234')

print(user7.contador)
print(user7.definicao())
