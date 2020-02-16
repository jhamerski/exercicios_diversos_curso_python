"""
PORQUE TESTAR NOSSO CÓDIGO
    - Reduzir bugs(problemas) no código existente.
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos.
    - Testes garantem que bugs que foram corrigidos anteriormente continuam corrigidos.
    - Testes garantem que refatoração que costumamos a fazer, não tragam novos bugs.

Testes automatizados!

TDD -> Test Driven Development (Desenvolvimento Guiado por Teste).
Com TDD é utilizado estágios de desenvolvimento>
    - Primeiro escreve seu teste.
    - Então você escreve o código mínimo para fazer o teste passar, ou seja, executar com sucesso.
    - Então refatora o código e testa novamente.
    - Uma vez que o teste passe, o recurso é considerado completo.

Estes estágios de TDD, são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red.
    - Green.
    - Refactor.


"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')

felix.miar()
print(felix.nome)




