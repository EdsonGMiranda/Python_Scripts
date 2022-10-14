# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


numeros = []
for i in range(5):
    numero = int(input("Digite um número: "))
    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            break
    else:
        numeros.append(numero)
print("Lista atual:", numeros)
