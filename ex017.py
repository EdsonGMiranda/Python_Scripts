import math

c_o = float(input('Entre com o cateto oposto : '))
c_a = float(input('Entre com o cateto adjacente : '))
hip = math.hypot(c_o, c_a)
print('A soma do cateto oposto {} com o cateto adjacente {} é igual a hipotenusa {} '.format(c_o, c_a, hip))