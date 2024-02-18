# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ padrão
# O Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
try:
    import sys
    # sys.path.append('D:/cursos/python3/udemy/')
except ModuleNotFoundError:
    ...
import modulo_python
import aula104_m
from aula104_m import variavel_modulo, soma

print('Esta módulo se chama', __name__)
print(aula104_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula104_m.soma(2, 3))