# Exercício Python 088: faça um programa que ajude um jogador da "MEGA SENA" a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-=-' * 11)
print('GERANDO NÚMEROS PARA MEGA SENA')
print('-=-' * 11)
num = list()
jogos = list()
quant = int(input('Entre com o número de jogos: '))
print('--' * 17)
i = 0
for l in range(0, quant):
    for c in range(0, 6):
        n = randint(1, 60)
        num.append(n)
    #print(f'{l + 1}º jogo sorteado : {num}')
    jogos.append(num[:])
    num.clear()


for p, i in enumerate(jogos):
    print(f'{p + 1} jogo sorteado {i}')
    sleep(1)
