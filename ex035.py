# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

a = float(input('Entre com o primeiro segmento : '))
b = float(input('Entre com o segundo segmento : '))
c = float(input('Entre com o terceiro segmento : '))
if (b - c) < a and a < (b + c) and  (a - c) < b and b < (a + c) and (a - b) < c and c < (a + b):
    print('Os segmentos acima \033[34;0mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[31;0mNÃO PODEM FORMAR\033[m um triângulo!')


