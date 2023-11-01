# Nessa aula, vamos aprender mais sobre interactive help
# uso do docstrings, para documentar nossas funções
# aurgumentos opcionais para dar mais dinamismo
# escopo de funcionais
#funcoes que retornam resultados.

'''
Interactive Help
help() é uma função interna

'''
#help()

#docstring , documentacao interna do python, precisa fazer 3 aspas duplas para abrir e 3 aspas duplas para fechar.

def contador (i,f,p):
    """
    Faz Uma contagem e mostra na tela
    para i: inicio da contagem
    Para f: fim da contagem
    para p: passo da contagem
    return: sem retorno
    """
    '''
    c=i
    while c <=f:
        print(f'{c}', end='..')
        c+=p
    print('Fim!')


contador(2,10,2)

# help(contador) deu certo
'''

# parametros opcionais.
'''
def somar(a,b,c=0):
    s=a+b+c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
''' 

#      Escopo de variáveis
# local onde uma variáveil vai existir e onde não vai existir.

#def teste():
#    x = 8
#    print(f'Na função teste, n valor {n}')
 #   print(f'Na função teste, x vale {x}') # aqui x é escopo local

          
#programa principal
n=2 # aqui acaba sendo escopo global
#print(f'No programa principal, n valor {n}')
#teste(f'No programa principal, x vale {x}') 
'''
# VARIAVEL GLOBAL E VARIAVEL LOCAL

def teste(b):
    global a 
    # ele usa a como a variavel global e nao é possivel alterar
    b += 4
    c = 2
    a = 8
    print(f'A dentro vale {a}')
    print(f'B dentro Vale {b}')
    print(f'C dentro vale {c}')
# o a local vira 8


a = 5
teste(a)
print(f'A fora vale {a}')

# b = escopo local
# c = escopo  local

# a = escopo global

'''
# Retornando valores
# return
def somar (a=0, b=0, c=0):
    s = a + b + c
    return s #retorna para r1 e r2 e r3



r1 = somar (3,2,5)
r2 = somar (1,7)
r3 = somar (4)
# ou jogar direto no print
print(f'Meus cálculos deram {r1}, {r2} e {r3}. ')


def fatorial (num =1):
    f = 1
    for c in range (num,0,-1):
        f*=c
    return f # return tbm retorna cvalor logico booleano

f1 =  fatorial (5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultado são {f1}, {f2} e {f3}')