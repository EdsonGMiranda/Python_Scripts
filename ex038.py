# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

a = int(input('Entre com o primeiro numero:'))
b = int(input('Entre com o segundo numero:'))
if a > b:
    print('O PRIMEIRO valor é maior')
elif a < b:
    print('O SEGUNDO valor é maior')
elif a == b :
    print('Os dois valores são IGUAIS')
