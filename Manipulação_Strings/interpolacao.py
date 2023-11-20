# OLD STYLE

nome = 'Thiago'
idade = 37
profissao = 'programador'
linguagem = 'Python'

pessoa = {'nome':'Thiago','idade': 37,'profissao': 'programador','linguagem': 'Python'}

print ('Olá, me chamo %s, tenho %d anos e sou %s. Atualmente estou programando em %s.' % (nome,idade,profissao,linguagem))


# NEW STYLE 

"""USANDO O .FORMAT"""

#sem determinar posições
print ('Olá, me chamo {}, tenho {} anos e sou {}. Atualmente estou programando em {}.'.format(nome,idade,profissao,linguagem))

#determinando posições
print ('Olá, me chamo {3}, tenho {2} anos e sou {1}. Atualmente estou programando em {0}.'.format(nome,idade,profissao,linguagem))

#argumentos de forma nomeada. O valor que vai antes do sinal de igual dever ser o mesmo que vai dentro das chaves.
print ('Olá, me chamo {name}, tenho {age} anos e sou {ocupation}. Atualmente estou programando em {language}.'.format(name=nome,age=idade,ocupation=profissao,language=linguagem))

#utilizando dicionário
print ('Olá, me chamo {nome}, tenho {idade} anos e sou {profissao}. Atualmente estou programando em {linguagem}.'.format(** pessoa))

"""USANDO O f-string"""

print(f'Olá, me chamo {nome}, tenho {idade} anos e sou {profissao}. Atualmente estou programando em {linguagem}.')

#formatando com f-string

pi = 3.14159

print(f'O valor de PI é: {pi:.2f}')
print (f'O valor de PI é: {pi:10.2f}') # o width determina quantos caracteres serão gerados antes do valor