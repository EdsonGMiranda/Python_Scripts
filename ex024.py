cidade = input('Em qual cidade você nasceu ? ').upper()
cid = cidade.find('SANTO')
if cid == 0:
    print('TRUE')
else:
    print('FALSE')


# cid = str(input('Em que cidade você nasceu ?')).strip()
# print(cid[:5].upper() == 'SANTO')