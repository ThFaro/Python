# MANIPULAÇÃO DE STRINGS

"""Formatando caracteres"""

nome = "ThIaGo"

print (nome.upper()) # deixa todos os caracteres em maiúsculo
print (nome.lower()) # deixa todos os caracteres em minúsculo
print (nome.title()) # deixa apenas o primeiro caractere em maiúsculo

"""Eliminando espaços"""

texto = "  Ola mundo!    "

print(texto.strip() + ".") # elimina os espaços dos dois lados
print(texto.lstrip()+ ".") # elimina os espaços do lado esquerdo
print(texto.rstrip()+ ".") # elimina os espaços do lado direito

"""Manipulação de espaços e quantidades de caracteres"""

menu = 'Python'
print('####'+menu+'####') # normal com concatenação
print (menu.center(14)) # centralizando o texto dentro da quantidades de caracteres desejados
print (menu.center(14,'#')) # centralizando, determinando o total de caracteres, e o que será inserido nos caracteres novos.


""""Determinando um caractere entre cada caractere do texto"""

menu = 'Python'
print("P-y_t_h_o-n") # print normal
print ("-".join(menu)) # print usando join

for letra in menu: # usando for
    print(letra, end = "-")
print()