# Nessa aula vamos aprender sobre Tuplas (lista imutavel, hehe)

# temos indice de 0 a 3 
# 0 , 1, 2, 3 total 4 itens pq começa no zero
# lembrando que em intervalor 0:2 ele nao pega o ultimo (o 2 seria excluido)
# for c in lanche: pega todos os itens de lanche
'''  
AS TUPLAS SAO IMUTAVEIS




'''

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
# for comida in lanche:     (tambem funciona)
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(4))