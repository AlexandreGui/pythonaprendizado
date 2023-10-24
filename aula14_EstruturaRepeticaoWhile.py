# Nesta aula vamos estudar laço while, muito bom repeticao 
""" Basicamento é uma estrutura que só sai com parametros especificos
Não precisa necessariamente ser em um tervalo de tempo ou numero
pode ser com alguma ordem especifica.
Geralmente usado quando não há limite de tempo, pode ser rodado quando nao sabe o limite
apenas em quanto não for feito um tipo exato de processo.
"""
# Aula Prática

#c = 1
#while c < 10 :
#   print(c)
#    c = c + 1 
#print('Fim')

r = 'S'
while r == 'S':
    n =int (input('Digite Um Valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim')