# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Entre com o peso (em kg) da {}° pessoa: '.format(i + 1)))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print('O maior peso é {}kg e o menor peso é {}kg '.format(maior, menor))

