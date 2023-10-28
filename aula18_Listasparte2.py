#Listas compostas
#dados = list()
#dados.append('Pedro')
#dados.append(25)


# VISTO NA AULA PASSADO O ITEM ACIMA

#pessoas = list()
#pessoas.append(dados[:])

'''  
Indice interno             0      1            0      1             0      1 
Pessoas             [  ['Pedro'; 25] |    ['Maria' ; 19]   |    ['Joao' ; 32 ]  ]            o de cima e da lista interna e o de baixo e da lista geral
Indice externo                0                   1                    2  
print(pessoas[0][0]) Pedro
print(pessoas[1][1]) 19
print(pessoas[2][0]) joao
print(pessoas[1])  ['Maria'; 19 ] 


'''
# tambem da pra fazer assim :
# galera = [ ['Joao', 19], ['Ana', 33]], ['Joaquim', 13], ['Maria', 45]]
'''
teste = list()
teste.append('Gustavo')
teste.append('40')
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''
galera = list()
dado = list()
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) 
    dado.clear()
print (galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen += 1
print(f'O numero total de maiores são {totmai}  e o número de memores são {totmen} ')