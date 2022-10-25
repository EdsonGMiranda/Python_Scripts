# Exercício Python 093: crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o
# total de gols feitos durante o campeonato.

score = dict()
partidas = list()
total = 0

score["nome"] = str(input('Nome: '))
tot = int(input(f'Quantas partidas o {score["nome"]} jogou? '))

for i in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {i + 1}: ')))
score["gols"] = partidas[:]

for count in partidas:
    total += count
score["total"] = total

print('-=' * 20)
print(score)
print('-=' * 20)

for k, v in score.items():
    print(f'O campo {k} tem o valor {v}.')


print('-=' * 20)

print(f'O jogador {score["nome"]} jogou {len(score["gols"])} partidas')
for r, i in enumerate(score["gols"]):
    print(f'  => Na partida {r + 1} , fez {i} gols')
    r += 1

