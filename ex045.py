# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep

print('-='*40)
print('Vamos Jogar Jokenpô "Pedra, Papel e Tesoura')
print('-='*40)
jogada = str(input('Entre com sua jogada :')).lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
maquina = choice(['pedra', 'papel', 'tesoura'])
if jogada == 'pedra' and maquina == 'tesoura':
    print('Você jogou {} e eu joguei {} , Você GANHOU!!!'.format(jogada, maquina))
elif jogada == 'pedra' and maquina == 'papel':
    print('Você jogou {} e eu joguei {} , Você PERDEU!!!'.format(jogada, maquina))
elif jogada == 'papel' and maquina == 'pedra':
    print('Você jogou {} e eu joguei {} , Você GANHOU!!!'.format(jogada, maquina))
elif jogada == 'papel' and maquina == 'tesoura':
    print('Você jogou {} e eu joguei {} , Você PERDEU!!!'.format(jogada, maquina))
elif jogada == 'tesoura' and maquina == 'papel':
    print('Você jogou {} e eu joguei {} , Você GANHOU!!!'.format(jogada, maquina))
elif jogada == 'tesoura' and maquina == 'pedra':
    print('Você jogou {} e eu joguei {} , Você PERDEU!!!'.format(jogada, maquina))
else:
    print('Você jogou {} e eu joguei {} , e deu EMPATE!!!'.format(jogada, maquina))