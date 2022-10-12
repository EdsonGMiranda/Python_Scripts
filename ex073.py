# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense (Botafogo).

times = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense', 'Athletico-PR',
'Atlético-MG', 'América-MG', 'Botafogo', 'Fortaleza', 'São Paulo', 'Bragantino',
'Goiás', 'Santos', 'Coritiba', 'Ceará', 'Cuiabá',
'Atlético-GO', 'Avaí', 'Juventude')

print('-=-' *5)
print(f'Campeonato Brasileiro 2022 : {times}')
print('-=-' *5)
print('Topo da tabela')
print('-=-' *5)
for i, time in enumerate(times[:5]):
    print(f'{i+1}º colocado é {times[i]}')
print('-=-' *5)
print('Zona de rebaixamento')
print('-=-' * 5)
print(f'Os 4 ultimos colocados são: {times[16:20]}')
print('-=-' * 5)
print(f'Os times em ordem alfabetica:  {sorted(times)}')
print('-=-' * 5)
print(f'O Botafogo está na {times.index("Botafogo")+1}ª posição')



