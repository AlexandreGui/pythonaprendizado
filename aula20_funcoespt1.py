# Nessa aula vamos aprender o que são funcoes ou rotinas e como utilizar funçoes em python.
# comando DEF
# parametro siples ou composto
# Rotina!!!


'''
funções que eu já utilizei com python :
print() ; len (); input() ; int() , float ()

def = definicão de função

'''


'''
def mensagem(msg):
    print('-' *30)
    print(msg)
    print('-' *30)


mensagem('Curso em Video')
mensagem('Python é muito bom')
'''

'''
def soma(n1 , n2):  # vamo tambem pode explicitar quem é o n1 e o n2 na hora que for lançar e usar o em formula
    s = n1 + n2
    print(s)


soma(2 , 5)
soma(18, 22)

def contador (* núm): # com o asterisco pode ser diversos parametros
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam}')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2) 
# esse comando criou uma tupla 

'''

valores = [7, 2, 5, 0 , 4]


def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    


dobra(valores)
print(valores)

