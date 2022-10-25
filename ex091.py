# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from operator import itemgetter
from random import randint

jogada = dict()
list_jogador = list()
count = 1
for i in range(1, 5):
    jogador = i
    dado = randint(1, 6)
    jogada[f'Jogador_{i}'] = dado


for k, v in jogada.items():
    print(f'O {k} jogou no dado {v}')
    sleep(1)

ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)

print('-*' * 20)
print(f'{"    ===RANKING DOS JOGADORES==="}')
print('-*' * 20)
for p, j in enumerate(ranking):
    print(f'O {p+1}ª lugar: {j[0]} com {j[1]}.')
    sleep(1)
