numero=input('Digite um número ')
if numero.isdigit():
    numero=int(numero)
if numero%2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')