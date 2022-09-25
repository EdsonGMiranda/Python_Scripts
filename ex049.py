# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Entre com um  número : '))
print('A tabuada de {} é:'.format(n))
for i in range(11):
    print('{} x {} = {}'.format(n, i, (n * i)))
