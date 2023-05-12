hora=int(input('Qual a hora? '))
if hora <= 11:
    print('Bom dia')
if (hora >= 12) and (hora <= 17):
    print('Boa tarde')
if (hora >= 18):
    print('Boa noite')