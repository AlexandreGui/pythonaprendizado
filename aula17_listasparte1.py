# Listas sao semelhantes a tuplas, mas são mutáveis 

# aula 09 ajuda muito nessa aula
# espaços dentro da lista ou tupla no python é chamado de key
# lanche.append('cookie')     adiciona algo a lista no final da lsita
# lanche.insert(0,'\')
#
# apagar elementos
# del lanche[3]
# lanche.pop(3) (ultimo elemento, exceto que voce especifique )
# lanche.remove('pizza') (escolhe o conteudo, a primeira incidencia)

#criando lista com range
#valores = list(range(4,11))

#valores.sort() (ordena todos os valores)
# valores.sort(reverse=True)
#len(valores)
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(f'Essa lista tem {len(num)} elementos')
print(num)
'''
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista')
''' 
a = [2, 3, 4, 7]
b = a[:]
# b = a  isso cria uma ligacao de igualdade o que mexe em uma lista mexe na outra
b[2] = 8
print(f'A lista A: {a} ')
print(f'A lista B: {b}')
