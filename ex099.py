# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* num):
    cont = mais = 0
    msg = 'Analisando os valores passados'
    tam = len(msg)
    print(f'{msg}')
    print(f'-' * tam)
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            mais = valor
        else:
            if valor > mais:
                mais = valor
        cont += 1
    print()
    print(f'Foram informador {cont} valores')
    print(f'E o maior foi {mais}.')
    print(f'-' * tam)


maior(3, 4, 5, 6, 7, 8, 9, 4, 6, 2)
maior(4, 5, 6)
maior()
