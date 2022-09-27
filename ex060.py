# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('''Entre com o número 
para saber seu fatorial: '''))
fat = num
soma = 1
print('Calculando {}!= '.format(num),end='')
while fat > 0:
    print('{}'.format(fat), end='')
    print(' x ' if fat > 1 else ' = ', end='')
    soma *= fat
    fat -= 1
print(soma)

