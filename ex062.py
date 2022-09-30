# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-=' * 10)
print('10 TERMOS DE UMA PA')
print('-=' * 10)

primeiro = int(input('Entre com o primeiro termo da PA: '))
razao = int(input('Entre com a razão de uma PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} '.format(termo), end=' -> ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Gostaria de mostrar mais algum termo? '))
print('...')