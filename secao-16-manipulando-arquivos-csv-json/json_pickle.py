"""
JSON e PICKLE

JSON -> JavaScript Object Notation

API -> São meios de comunicaçõa entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube) e terceiro (nós
desenvolvedores)

"""
import json

# dumps 'transforma' pra .json. Colocando aspas duplas
ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'novo', '220V', 2340)}])

print(type(ret))

print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Feliz', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

# Intetrando .json com piclke. Instalar a biblioteca (pip install jsonpickle)
import jsonpickle

felix = Gato('Feliz', 'Vira-Lata')

# Escrevendo o arquivo jsonpickle
with open('felix.json', 'w') as arq:
    retor = jsonpickle.encode(felix)
    arq.write(retor)

retorno = jsonpickle.encode(felix)

print(retorno)

with open('felix.json', 'r') as arq:
    conteudo = arq.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
