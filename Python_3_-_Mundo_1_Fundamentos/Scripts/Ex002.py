'''
Exercicio 002
Fazer um script que solicite ao usuario um nome e apresente uma mensagem de boas vindas para o nome digitado
'''

nome = input('Por favor digite o seu nome: ')

#print simples
print('É um prazer lhe conhecer,', nome, '!')

#print formatado
print('É um prazer lhe conhecer, {}!'.format(nome))
