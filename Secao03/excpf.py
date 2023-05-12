#entrada de dados do primeiro digito
#74682489070
cpf_inp = input('Digite o valor do CPF, sem traços ou pontos ')
if '.' in cpf_inp or '-' in cpf_inp:
    print('Digitar o CPF sem traços ou pontos')

cpf_util1 = cpf_inp[:9]
contador = 10
resultado = 0

for numero in cpf_util1:
    resultado += int(numero) * contador
    contador -= 1
numero_1 = (resultado*10) % 11
numero_1 = numero_1 if numero_1 <=9 else 0
print(numero_1)

cpf_util2 = cpf_inp[:9] + str(numero_1)
contador2 = 11
resultado2 = 0

for numeroaux in cpf_util2:
    resultado2 += int(numeroaux) * contador2
    contador2 -= 1
numero_2 = (resultado2*10) % 11
numero_2 = numero_2 if numero_2 <=9 else 0
print(numero_2)