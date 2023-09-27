# Nessa aula será para manipulacao de instrings no python, uma das aulas mais importantes.
'''' 
o que é uma cadeia de caracteres?

'Curso em Video Python'
[C][u][r][s][o][][e][m][][V][i][d][e][o][][P][y][t][h][o][n]
 0  1  2  3  4  5 6  7 8 9  10 11 12 13 14 15 16 17 18 19 20

ele cria mini espacos e colocar cada letras e espaco entre elas
lembrando que sempre comeca no zero em python **********
e sempre exclui o ultimo na contagem
frase[9:13] ele pega o V e vai ate o E (nao pega 'ó' pois ele e o 13)

(ajuda no conceito de lista pois e usado da mesma forma)

frase[9:13] pega no intervalor (excluindo o final)
frase[9:13:2] pegando de 2 em 2
frase[9] pega somente o 9
frase[9;13] pega o 9 e o 13
frase[:5] do zero ao 4
frase[15:] do 15 ao final
frase[9::3]

----------------------------- Analise ----------------------------


len(frase) = mostra a qtos caracteres tem a frase
frase.count('o') = conta quantas vezes existe a letra o
frase.count('o',0,13) conta quantas vezes existe a letra o entre 0 a 12
frase.find('deo') mostra em qual posicao ele achou 'deo' na frase (se nao existe a funcao ele retorna -1)
'Curso' in frase (resposta e True)


----------------------------Transformacao ------------------------

frase.replace('Python','Android')   =  altera a palavra python para android.
frase.upper() = transforma tudo em maiusculo
frase.lower() = transforma tudo em minusculo
frase.capitalize() = joga tudo em minusculo e so a primeira letra de cada palavra em maiusculo (menos as preposicoes)
frase.title() =  joga tudo pra minusculo mas a primeira letra de cada palavra para maiusculo (mesmo as preposicoes)

frase.strip() = remove os espacos do inicio e do final da frase (deixa os do meio)
frase.rstrip() = remove somente o lado direito (os ultimos)
frase.lstrip() =  remove os espacos da esquerda (os primeiros)

 
 --------------------------Divisao --------------------------
 frase.split() = divisao das palavras usando cada espaco vazio e recebe uma lista nova cada palavra dentro da lista original, cada uma ganhando seu index do zero ao final
 '-'.join(frase) = junta todos os elementos de frase e vai usar o separador que o tracinho colocado no inicio
 
 
 
 '''