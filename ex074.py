# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n = ((randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)))
print('-=-' * 18)
print(f'Os valores sorteados foram:', end=' ')
for i in n:
    print(f'{i}', end=' ')
print('')

print('-=-' * 18)
print(f'O maior valor é o {max(n)}.')
print('-=-' * 18)
print(f'O menor valor é o {min(n)}')
print('-=-' * 18)



