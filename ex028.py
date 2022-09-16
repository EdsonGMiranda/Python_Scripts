import random

print('='*40)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('='*40)
num = int(input('Em que número eu pensei? '))
robo = random.randrange(5)
if num == robo:
    print('Muito bem!! você acaba de ganhar! Eu pensei no número {}'.format(robo))
else:
    print('GANHEI! Eu pensei no número {} e não no número {} '.format(robo, num))

