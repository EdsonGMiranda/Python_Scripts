# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.

nome = str(input('Entre com seu nome :')).strip()
n = nome.split()
print('O primeiro e ultimo nome são {}.{}'.format(n[0], n[-1]))
print('O primeiro nome é {}'.format(n[0]))
print('O ultimo nome é {}'.format(n[-1]))
