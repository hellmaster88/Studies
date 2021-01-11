'''
Crie um programa que leia algo pelo teclado e mostre:
1- Seu tipo primitivo
2- Todas as informacoes is possiveis sobre ele
'''

v1 = input('Entre com um valor qualquer pelo teclado (letras e/ou numeros)')
print('O tipo primitivo da variavel é: {}'.format(type(v1)))

print('isupper : {}'.format(v1.isupper()))
print('isspace : {}'.format(v1.isspace()))
print('isascii : {}'.format(v1.isascii()))
print('isalpha : {}'.format(v1.isalpha()))
print('isalnum : {}'.format(v1.isalnum()))
print('islower : {}'.format(v1.islower()))
print('isnumeric : {}'.format(v1.isnumeric()))
print('isdecimal : {}'.format(v1.isdecimal()))
print('isdigit : {}'.format(v1.isdigit()))
print('isidentifier : {}'.format(v1.isidentifier()))
print('isprintable : {}'.format(v1.isprintable()))
print('istitle : {}'.format(v1.istitle()))
