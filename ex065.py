# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = ''
cont = 0
soma = 0
maior = 0
menor = 0
while resposta != 'N':
    n = int(input('Entre com o {}º valor: '.format(cont+1)))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if maior > n:
            menor = n
        else:
            maior = n
    resposta = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
print('Você digitou {} vezes e a média dos numeros é {:.2f}'.format(cont, soma/cont))
print('E o maior numero foi {} e o menor foi {}'.format(maior, menor))
