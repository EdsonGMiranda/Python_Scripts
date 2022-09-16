frase = str(input('Digite um frase :')).upper().strip()
print('A frase possuí {} letras a'.format(frase.upper().count('A')))
print('O primeiro A fica na posição {}'.format(frase.find('A')+1))
print('A ultima letra A fica na posição {}'.format(frase.rfind('A')+1))
