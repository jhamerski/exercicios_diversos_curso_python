"""
MÓDULOS CUSTOMIZADOS

Como módulos Python, nada mais são do que arquivos Python, então todos os arquivos que criamos nesse curso são módulos
Python, prontos para serem utilizados.
"""
# Importando uma função específica do nosso módulo
from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Importando todo o módulo (Temos acesso a todos elementos do módulo)
from funcoes_com_parametros as fcp

print(fcp.lista)

print(fcp.soma_impares(fcp.lista))
