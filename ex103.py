# Exercício Python 103: faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):
    if nome == '' and gols == '':
        return f'O jogador <desconhecido> fez 0 gols no campeonato.'
    elif nome == '':
        return f'O jogador <desconhecido> fez {gols} gols no campeonato.'
    elif gols == '':
        return f'O jogador {nome} fez {gols} gols no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gols no campeonato.'


name = input('Nome do Jogador: ')
gol = int(input('Numero de gols: '))

print(ficha(name, gol))
