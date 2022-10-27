# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar().A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)

    for c in lista:
        print(f'{c}', end=' ')
    print('-- PRONTO!')


def somapar(lista):
    sorteia(lista)
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos numeros pares foi {soma}')
    lista.clear()


numeros = list()
print('-' * 50)
somapar(numeros)
print('-' * 50)
somapar(numeros)
print('-' * 50)
somapar(numeros)
