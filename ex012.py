# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

item = float(input('Entre com o valor do produto : R$'))
desconto = 5/100
print('O novo valor do produto é {}' .format(item - item*desconto))
