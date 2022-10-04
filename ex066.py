# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).


count = soma = i = 0
print('-=-' * 20)
print('Programa que lê N numeros e diz a soma (para sair aperte 999)')
print('-=-' * 20)

while True:
    n = int(input(f'Entre com o {i+1}° número: '))
    if n == 999:
        break
    else:
        soma += n
        i += 1
print(f'Você digitou {i} números e a soma deles é {soma}')

