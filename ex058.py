# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

print('-='*40)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-='*40)
num = int(input('Em que número eu pensei? '))
robo = random.randint(0, 10)
count = 0
while num != robo:
    num = int(input('Você errou e eu ganhei, tente novamente em que número eu pensei? '))
    count += 1
print('-='*40)
print('Muito bem!! você acaba de ganhar! Eu pensei no número {}'.format(robo))
print('Mas você precisou de {} tentativas para acertar'.format(count))
print('-='*40)
