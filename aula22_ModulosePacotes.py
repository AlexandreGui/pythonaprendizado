import modulos
# Nessa aula vamos entender sobre modularização e pacotes.
# basicamente é uma função que fica como arquivo e resgatada como um modulo.
# montei um arquivo modelos.py
# from modulos import fatorial ( ai nao precisa colocar o modulos.fatorial)
#from math import sqrt
# from random import randint



num = int(input('Digite Um Valor: '))
fat = modulos.fatorial(num)
print(f' O fatorial de {num} é {fat}. ')

# vantagens
# organização
# facilita a manutencão
# ocultação do código detalhado
# reutilização em outros projetos


# PACOTES
# pasta que contem modulos
# e colocar __init__.py , ai você consegue configurar de maneira correta

