# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print('-=-'*20)
    num = int(input('Quer ver a tabuada de qual valor?  '))
    print('-=-' * 20)
    if num < 0:
        break
    else:
        i = 1
        while i <= 10:
            print(f'{num} x {i} = {num * i}')
            i += 1

