"""
ITERADOR CUSTOMIZADO

for n in range(11):
    print(n)


"""


class Contador:  # OBS: Quando tiver uma função dentro de uma classe o 1° parâmetro é o SELF
    def __init__(self, menor, maior):  # Construtor
        self.menor = menor
        self.maior = maior

    def __iter__(self):  # iter()
        return self

    def __next__(self):  # next()
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


for n in Contador(1, 6):
    print(n)
