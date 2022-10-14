# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_num = []
lista_par = []
lista_impar = []

while True:
    lista_num.append(int(input('Entre com o valor: ')))
    sair = input('Deseja continuar? [S/N]').strip().upper()[0]
    if sair == 'N':
        break
print('-*' * 20)
for i in lista_num:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'Lista digitada foi: {lista_num}')
print(f'A lista de pares: {lista_par}')
print(f'A lista de impares: {lista_impar}')
