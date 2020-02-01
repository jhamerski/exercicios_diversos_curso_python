"""
POO - ATRIBUTOS

Atributos -> Representam as característica do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

Atributo de Instãncia: São atributos declarados dentro do método construtor

OBS: Método construtur é um método especial utilizado para a construção do objeto

Em JAVA, uma classe Lampada, incluindo seus atributos ficaria mais ou menos assim:
public class Lampada(){
    private int voltagem;
    protected String cor;
    public Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é PUBLICO. Ou seja, pode ser acessado em
todo o PROJETO.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado ou
utilizado somente dentro da própria classe onde está declarado, utiliza-se '__' duplo underscore no inicio de seu nome.
Isso é conhecido também como Name Mangling.
"""


# Classe Python equivalente a escrita em JAVA acima - Classe com atributo de Instância Público
class Lampada:

    def __init__(self, voltagem, cor):  # Método construtor
        self.votagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __index__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos ou privados
class Acesso:

    def __init__(self, email, senha):
        self.email = email  # Público
        self.__senha = senha  # Privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos
# atributos fora da classe
user = Acesso('user@gmail.com', '123456')

print(user.email)
# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso, mas não deveríamos fazer esse acesso (Name Mangling)

user.mostra_senha()
user.mostra_email()

"""
O que significa atributos de isntância?
    - Significa que ao criarmos instância de uma classe, todas as instâncias terão estes atributos
"""
user1 = Acesso('user1@gmail.com', '123456')  # Criamos instâncias da classe Acesso
user2 = Acesso('user2@gmail.com', '654321')  # Criamos instâncias da classe Acesso

user1.mostra_email()
user1.mostra_senha()

user2.mostra_email()
user2.mostra_senha()

"""
ATRIBUTOS DE CLASSES
Atributos de Classes são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um
valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância de classe
ter seus próprios valores como é o caso dos atributos de instância, com os atríbutos de classe todas as instâncias terão
o mesmo valor para esse atributo
"""


# Refatorar a classe Produto
class Produto:

    # Atributo de classe
    imposto = 1.05  # OU seja, 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.imposto)  # Acesso possível, porém incorreto
print(p2.imposto)  # Acesso possível, porém incorreto

print(p1.valor)
print(p2.valor)

# Não precisamos criar uma instância de classe para fazer acesso ao atributo de classe
print(Produto.imposto)  # Acesso correto que um atributo de classe

print(f'Produto 1 tem id = {p1.id}')
print(f'Produto 2 tem id = {p2.id}')

# OBS: Em Java os atributos de classes como no Python, são chamados de atributos estáticos

"""
ATRIBUTOS DINÂMICOS
É um atributo de instância que pode ser criado em tempo de execução.

OBS: O atributo dinâmico será exclusivo que instância que o critou.
"""
p2 = Produto('Caneta Bic', 'Material Escolar', 5)
p3 = Produto('Lápis de Cor', 'Material Escolar', 8.50)

# Criando um atributo dinâmico em tempo de execução
p3.quantidade = '12uni'  # Note que na classe Produto não existe o atributo quantidade
print(f'Produto: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor} e quantidade: {p3.quantidade}')

# Deletando atributos
print(p2.__dict__)
print(p3.__dict__)

del p3.quantidade
del p3.valor
print(p2.__dict__)
print(p3.__dict__)

