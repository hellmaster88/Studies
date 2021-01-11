'''
Tipos primitivos

4 Tipos básicos de tipos primitivos mais utilziados:
INT - Numeros inteiros -> Ex: 7, -4, 0, 9875
FLOAT - Numeros reias/numeros de ponto flutuante -> Ex: 4.5, 0.00075, -1.586, 7.0
BOOL - Valores lógicos ou booleanos -> Ex: True, False
STR - Valores string -> 'Bruno', 'Olá Mundo!', '7.0', ''

Nota1: Python e padrão internacional utiliza . (ponto) ao invez de , (virgula) para separar numero reais.
Nota2: Sempre que for utilizar True e Falso colocar a primeira letra (T ou F) sempre em maiusculo.

---------------------------------------------------------------------------

Nova forma de print (A partir do Python 3)

print('A soma vale: {}'.format(variavel))

Nota3: .format é a invocação do metodo format da própria string.
'''

# Testes e exemplos do conteudo da aula
#######################################################################################################################

n1 = input('Digite um numero: ')
print(type(n1))  # Imprime o tipo da variavel n1

n1 = int(input('Digite um numero: '))
print(type(n1))

n1 = int(input('Digite o primeiro numero da soma: '))
n2 = int(input('Digite o segundo numero da soma: '))
n3 = n1 + n2
print('O resultado da soma entre {} + {} = {}'.format(n1, n2, n3))

n1 = float(input('Digite um valor numerico (resultado apresentado em float): '))
print(n1)

n1 = bool(input('Entre com um valor (ou nao) para a variavel e aperte enter!'))
print(n1)

n = input('Digite um valor qualquer para verificarmos informações sobre a variavel: ')
print(n.isnumeric())  # Diz se é possivel converter o valor da varivel no tipo numerico!
print(n.isalpha())  # Para saber se é letras (Alpha)
print(n.isalnum())  # Para saber se é alphanumeric
print(n.islower())  # Verifica se esta apenas em letras minusculas
print(n.isupper())  # Verifica se esta apenas em letras maiusculas
print(n.isspace())  # Vericiar se é um espaço
print(n.isascii())

#######################################################################################################################
