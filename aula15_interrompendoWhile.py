# Nessa aula vamos aprender comandos para encerramento do while, com break.

# Entendendo o comando break
# Aula Pratica

n = 0
s = 0
while True:
    n = int(input('Digite um número: ' ))
    if n == 999:
        break
    s += n

print('Acabou')