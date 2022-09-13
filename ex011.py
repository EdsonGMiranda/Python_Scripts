largura = float(input('Entre com a largura da parede : '))
altura = float(input('Entre com a altura da parece : '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua area é {}m2. \n Para pintar toda a parede, você precisará de {}l de '
      'tinta. '.format(largura, altura, area, (area/2)))
