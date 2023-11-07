texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "") # O (end = "") serve para o resultado sair na mesma linha
else:
    print() #adciona um quebra linha

#for com built-in range
for numero in range(0,51,5): # tabuada do 5
    print(numero) 