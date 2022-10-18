# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele.

n = input("Digite alguma coisa : ")
print(type(n))
print("Tem espaços? ", n.isspace())
print("É um numero? ", n.isnumeric())
print('É um alfanumerico? ', n.isalnum())
print('É alfabético? ', n.isalpha())
print('Está em maiuscula?', n.isupper())
print('está em minuscula?', n.islower())
