# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite um frase :')).upper().strip()
print('A frase possuí {} letras a'.format(frase.upper().count('A')))
print('O primeiro A fica na posição {}'.format(frase.find('A')+1))
print('A ultima letra A fica na posição {}'.format(frase.rfind('A')+1))
