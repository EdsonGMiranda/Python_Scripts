# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Entre com a largura da parede : '))
altura = float(input('Entre com a altura da parece : '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua area é {}m2. \n Para pintar toda a parede, você precisará de {}l de '
      'tinta. '.format(largura, altura, area, (area/2)))
