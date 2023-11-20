# Adicionar objetos na lista [].apend
lista = []

lista.append(1) # um int
lista.append("Python") # uma string
lista.append([40,30,20]) # uma lista

print(lista)

# Limpar uma lista [].clear
lista = [1,'python',[20,30,10]]
print (lista)
lista.clear()
print (lista)

# Copiar lista [].copy
lista = [1,'python',[20,30,10]]
l2 = lista.copy()
print(lista)
print (id(l2), id(lista))
'''O que altermos no l2(copy) nao influencia na lista original'''

# Contar quantas vezes um elemento aparece na lista [].count
cores = ['vermelho','azul','verde','azul']

cores.count('vermelho')
cores.count('azul')
cores.count('verde')

print(cores.count('azul'))

# Juntar listas [].extend OBS: Os objetos ja existentes nao sao substituidos
linguagens = ['python','java','css']
print(linguagens)

linguagens.extend(['js','C++','java'])
print(linguagens)

# Achar a primeira ocorrencia de um objeto [].index
linguagens = ['python','java','css', 'java']

print(linguagens.index('java'))
print(linguagens.index('css'))

# Remover um objeto em pilha .pop Ex: Pilha de pratos
linguagens = ['python','java','css', 'java']

linguagens.pop() # tira o ultimo adicionado
print(linguagens)

linguagens.pop(2) # tira o do indice escolhido
print(linguagens)


# Remover com [].remove OBS: se tiver  objetos duplicados, será excluida apenas a primeira ocorencia
linguagens = ['python','java','css', 'java']

linguagens.remove('css') # com remove passamos o nome do  objeto
print(linguagens)


# Transpor uma lista
linguagens = ['python','java','css', 'java']

linguagens.reverse()
print(linguagens)

# Ordenar lista
linguagens = ['python','java','css', 'csharp','cobol']
linguagens.sort() # por padrão deixa em ordem alfabética
linguagens.sort(reverse=True) #  deixa a ordem alfabética invertida
linguagens.sort(key=lambda x: len(x)) #  ordena pela quantidade de caracteres (menor por maior)
linguagens.sort(key=lambda x: len(x), reverse=True) #  ordena pela quantidade de caracteres inversa (maior por menor)

# Saber o tamanho da lista (quantidade de elementos) 'len'
linguagens = ['python','java','css', 'csharp','cobol']
print(len(linguagens))



