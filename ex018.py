# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o Angulo desejado : '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {:.2f}° tem o SENO  de {:.2f}'.format(angulo, seno))
print('O angulo de {:.2f}° tem o COSSENO  de {:.2f}'.format(angulo, cosseno))
print('O angulo de {:.2f}° tem o TANGENTE  de {:.2f}'.format(angulo, tangente))
