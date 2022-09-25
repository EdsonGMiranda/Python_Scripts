# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# os espaços. Exemplos de palíndromos:
# EX: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print('-='*21)
print('Entre com um frase para ver se é palíndromo')
print('-='*21)
frase = str(input('Entre com uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
esarf = ''
for letra in range(len(junto) - 1, -1, -1):
    esarf += junto[letra]
print('{} '.format(esarf), end='')
if esarf == junto:
    print('é um palindromo')
else:
    print('não é um palindromo')



