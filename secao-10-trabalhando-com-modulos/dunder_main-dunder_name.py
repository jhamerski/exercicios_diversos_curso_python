"""
DUNDER

Dunder -> Double Under

Dunder Main -> __main__
Dunder Name -> __name__

Em Python, são utilizados dunder para criar funções, atributos/propriedades e etc... utilizando Double Under para não
gerar conflito com os nomes desses elementos na programção.

Na linguagem C, temos um programa da seguinte forma:
int main(){
    return 0;
}

Na linguagem JAVA temos um programa da seguinte forma:
public static void main(String[] args){

}

Em Python, se executarmos um módulo Python na linha de comando, internamente o Python atribuirá a variável __name__ o
valor __main__ indicando que este módulo é o módulo de executação principal
"""
print(__name__)  # __main__

from funcoes.funcao_multiplicacao import multiplicacao

print(multiplicacao(5, 9))
