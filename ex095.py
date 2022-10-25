# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

score = dict()
jogadores = list()
partidas = list()
total = 0

while True:
    score["nome"] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas o {score["nome"]} jogou? '))
    soma = 0
    for i in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {i + 1}: ')))
        soma += partidas[i]
    score["gols"] = partidas[:]
    partidas.clear()
    total = soma
    score["total"] = total

    jogadores.append(score.copy())
    sair = input('Deseja continuar? [S/N]').upper().strip()[0]
    if sair in 'N':
        break


print('-=' * 30)
for p, it in enumerate(jogadores):
    print(it)
print('-=' * 30)
print(f'{"cod":>3}', end='')
for i in score.keys():
    print(f'{i:>15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-=' * 30)

while True:
    busca = int(input('Mostrar dados de qual jogador? [1000 para listar tudo ou 999 para sair '))
    if busca == 999:
        break

    if busca == 1000:
        print('Lista de todos jogadores:')
        for pos, part in enumerate(jogadores):
            print(f'O jogador {jogadores[pos]["nome"]} jogou {len(jogadores[pos]["gols"])} partidas')
            for r, i in enumerate(jogadores[pos]["gols"]):
                print(f'  => Na partida {r + 1} , fez {i} gols')
                r += 1
    if busca >= len(jogadores):
        print(f'Error! Não existe o codigo {busca}, digite novamente: ')
    else:
        print(f'Dados do jogador {jogadores[busca]["nome"]}')
        for pos, part in enumerate(jogadores[busca]["gols"]):
            print(f' => Na partida {pos + 1} , fez {part} gols ')

    print('-=' * 30)
print('FIM')


