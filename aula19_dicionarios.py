#Variaveis compostas de dicionarios
'''
Tuplas ()
Listas []
Dicionarios {} ou dados = dict()
dados = {'nome':'Pedro','idade':25 }
print(dados['nome'])  Pedro
print(dados['idade']) 25


filme = {'titulo': 'Star Wars', 
'ano':1977,
'diretor':'George Lucas''
}


print(filme.values()) retorna : (star wars , 1997 e geoage lucas sao keys)
print(filme.keys()) retorna : (titulo, ano, diretor)
print(filme.items()) retorna: filme = {'titulo': 'Star Wars', 'ano':1977, 'diretor':'George Lucas''}

pode usar o for tbm com isso

for k, v in filme.items()
    print(f'O {k} é {v}')

    
    também pode colocar um dicionario dentro de uma lista

 '''
# Pratica

#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.items())
#pessoas['nome'] = 'Leandro'
#for k, v in pessoas.items():
 #   print(f'{k} = {v}')

'''
brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 =  {'uf':  'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
'''
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# copy de um metodo

for e in brasil:
    for v in e.values():
        print(v, end= ' ')
    print()
     # for k, v in e.items():  
     #      print(f'O campos {k} tem valor {v}. ')
