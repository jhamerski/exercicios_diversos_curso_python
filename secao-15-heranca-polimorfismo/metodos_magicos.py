"""
POO - MÉTODOS MÁGICOS

São todos os métodos que utilizam dunder __metodo__

dunder __init__ -> Construtor
__repr__ -> Representação customizada do objeto
__str__ -> Transforma em string, normalmente feita para o usuário final
__len__ -> Inplementação para verificar o tamanho do objeto através de um parâmetro
__del__ -> Deletar objetos da memória
__add__ -> Serve para poder somar (+) duas strings
__mul__ -> Concatenando string com inteiro
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    # Representação do nosso objeto
    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    # Implementação feita para o usuário final
    def __str__(self):
        return f'O título é {self.__titulo}'

    # Implementando o len através das páginas
    def __len__(self):
        return self.__paginas

    # Deletar um objeto da memória
    def __del__(self):
        print(f'Um objeto do tipo Livro foi deletado da memória')

    # Somar (+) duas Strings
    def __add__(self, other):
        return f'{self} - {other}'

    # Concatenando string com inteiro
    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('A Sutil Arte de Liga o Foda-se', 'Mark Manson', 427)
livro2 = Livro('Inteligência Artificial com Python', 'Geek', 1023)

print(livro1)  # <__main__.Livro object at 0x01641F88> endereço de memória onde está armazenado o objeto
print(livro2)  # <__main__.Livro object at 0x01641FE8> endereço de memória onde está armazenado o objeto

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)
