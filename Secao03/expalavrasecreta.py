### Qual a palavra a ser descoberta ###
#palavra_secreta = 'Palmeiras'

### entrada de dados do usuário ###
#palusuario = input('Digite uma letra ')

### verifica se a palavra é uma String ###

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print('*')

