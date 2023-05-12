nome=input('Digite seu nome ')
idade=input('Digite sua idade ')
if nome =='' or idade == '':
    print('Desculpe, Você deixou campos vazios')
else:
    print('Seu nome é {}'.format(nome))
    print('Sua idade é {}'.format(idade))
    print('Seu nome invertido é {}'.format(nome[::-1]))
    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print('Seu nome contém {} letras'.format(len(nome)))
    print('A primeira letra do seu nome é {}'.format(nome[0]))
    print('A última letra do seu nome é {}'.format(nome[-1]))