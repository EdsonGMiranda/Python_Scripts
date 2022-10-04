# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

from random import randint
count = 0
escolha = ' '
while True:
    num = int(input('Entre com o número [1-10]: '))
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    if (num + computador) % 2 == 0 and escolha == 'P':
        print('--'*20)
        print(f'Você jogou {num} e o computador {computador}. O tatal deu {num+computador} e deu PAR!')
        print('--' * 20)
        print('VOCÊ GANHOU!')
        print('Vamos jogar novamente ...')
        print('-=' * 20)
        count += 1
    if (num + computador) % 2 == 1 and escolha == 'I':
        print('--'*20)
        print(f'Você jogou {num} e o computador {computador}. O tatal deu {num+computador} e deu IMPAR!')
        print('--' * 20)
        print('VOCÊ GANHOU!')
        print('Vamos jogar novamente ...')
        print('-='* 20)
        count += 1
    elif (num + computador) % 2 == 1 and escolha == 'P':
        print('--' * 20)
        print(f'Você jogou {num} e o computador {computador}. O tatal deu {num + computador} e deu IMPAR!')
        print('--' * 20)
        print('VOCÊ PERDEU!!')
        break
    elif (num + computador) % 2 == 0 and escolha == 'I':
        print('--' * 20)
        print(f'Você jogou {num} e o computador {computador}. O tatal deu {num + computador} e deu PAR!')
        print('--' * 20)
        print('VOCÊ PERDEU!!')
        break

print(f'GAME OVER! você venceu {count} vezes!')


