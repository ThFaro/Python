frutas = ["laranja","uva","maçã","banana"] # delclarando lista usando []
print (frutas)
print (frutas [0])# acesso direto
print (frutas [-1])# acesso pelo indice negativo. Obs o indice negativo começa de -1

frutas = [] # declarando uma lista vazia
print(frutas)

letras = list('python') # delclarando lista usando o construtor list
print (letras)

# Lista Aninhada (lista dentro de lista)

matriz =[            # matriz bidimensional 3x3
    [1,'a',2]
    ['b',2,4]
    [6,5,'c']
]

# Fatiamento

lista = ['p','y','t','h','o','n']
lista[2:] # [t,h,o,n]
lista[:2] # [p,y]
lista[1:3] # [y,t]
lista[0:3:2] # [p,t]
lista[::] # [p,y,t,h,o,n]
lista[::-1] # [n,o,h,t,y,p] 

# Iterar listas

carros = ["gol","celta","palio"]

for carro in carros:
    print(carro)

# Percorrendo a lista e achando o indice do objeto (ENUMERATE)

carros = ["gol","celta","palio"]

for indice, carro in enumerate(carros):
    print (f"{indice}: {carro}")

# Compreensão de listas

#usando for e append
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numeros % 2 == 0:
        pares.append(numero)
        

#usando comprehension
numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]
print([pares])



# Modificando valores de uma lista

#usando for e append
numeros = [1,30,21,2,9,65,34]
quadrado= []


for numero in numeros:
    quadrado.append(numero **2)
    
 
 #usando compreheinsion
numeros = [1,30,21,2,9,65,34]
quadrado = [numero  ** 2 for numero in numeros]
print ([quadrado])
