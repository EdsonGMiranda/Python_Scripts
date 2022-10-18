# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em
# graus Celsius e converta para graus Fahrenheit.

temp = float(input('Entre com a temperatura em grau celsius : '))
temp_new = (temp * 1.8) + 32
print('A temperatura {} em celsius equivale a {:.2f} fahrenheit'.format(temp, temp_new))
