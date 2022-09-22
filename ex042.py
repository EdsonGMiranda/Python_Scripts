# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes



a = float(input('Entre com o primeiro segmento : '))
b = float(input('Entre com o segundo segmento : '))
c = float(input('Entre com o terceiro segmento : '))
if (b - c) < a and a < (b + c) and  (a - c) < b and b < (a + c) and (a - b) < c and c < (a + b):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if a == b == c:
        print('É um Triângulo EQUILÁTERO')
    elif a != b != c:
        print('è um Triângulo ESCALENO')
    else:
        print('O Triângulo é ISÓSCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

