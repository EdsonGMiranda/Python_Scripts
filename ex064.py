# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
soma = 0
count = 0
while 1 == 1:
    n = int(input('Entre com um numero: '))
    if n == 999:
        break
    else:
        soma += n
        count += 1

print('Você digitou {} números e a soma deles é {}'.format(count, soma))



