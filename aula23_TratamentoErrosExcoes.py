# tipos de erros.
# primt(x) --> erro de sintaxe
# somente o print(x) ---> erro 'x' is not defined (erro de nao ter definido o x) exceção 


# n = int(input("numero:"))
# print(f'Voce digitou o numero{n}') (e voce digitou  oito) deu excecao value erro

# a = int (input('Numerador:'))
# b = int (input(Denomidador: '))
# r = a / b
# print(f'O resultado é {r} ')
#  falaha de excecao (divisao por zero)

# 2 / '2' (type error)


# lst =  [3, 6, 4]
# print(lst[3]) index erro pq só possui até o index 2 pq começa  no zero


# import uteis (se nao for encontrado, modulenotfoundError)

# Exception = exceção
# depois vem o comando tentar. try

# try: 
#   [operaçao]
# except:
#   

try:
    a = int(input('Numerador: '))
    b = int(input('Denomidaro: '))
    r = a / b
#except Exception as erro:
#    print(f'O problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir o número por zero')
except KeyboardInterrupt:
    print('O Usuário preferiu não informar os dados!')
else: 
    print(f'O Resultado é {r})')
finally:
    print('Volte sempre! Muito Obrigado!')

# todo o try pode ter mais de um exceptions
# todos com varios exceptions
