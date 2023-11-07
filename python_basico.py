#COMO IMPRIMIR ALGO
print ("Hello World!")

#TIPO DE DADOS
print(1+20) #int
print (1.5 + 1 + 0.5) #float(somando um int)
print(True) #bool
print(False) #bool
print("Python") #str

#VARIÁVEIS E CONSTANTES
"""As variáveis são escritas em letras minúsculas e as constantes em maiúsculas, 
    e ambas deve seguir o padrão snake(_) """

nome = "thiago"
idade = 36
print(nome,idade)

nome, idade = "Laura", 35
print(nome,idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP","RJ","SC","RS"]
print(BRAZILIAN_STATES)


#CONVERTENDO TIPOS
print(int(1.9)) #converte um float para int(resultado do print = 1)
print(int("10")) #converte str para int
print(float("10.10")) #converte str para float
print(float(100)) #converte int para float (resultado do print  = 100.1)
print(type(str(10.10))) #float para str (o type serve para mostrar o tipo de valor impresso)

#USANDO PRINT/INPUT
nome = input("informe o seu nome: ") #o input pede um dado ao usuario, e o armazena na variavel determinadada
print(nome)
idade = input("Informe a idade: ")
print(nome,idade)
print(nome, idade, end ="...\n") #o end determina o que sera impresso apos o resultado das variaveis
print (nome,idade, sep="#") #o sep altera o separador padrão que é um espaço pelo separador desejado(neste caso o #)
print (nome,idade, sep="#", end ="...\n") #junção deo sep e end

#OPERAÇÃOES ARITIMÉTICAS
produto_1 = 20
produto_2 = 10
produto_3 = 3

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2) #retorna um float
print(produto_1 // produto_2) #retorna um int
print(produto_1 * produto_2) 
print(produto_1 % produto_3) #retorna um módulo(resto da divisão)
print(produto_1 ** produto_3) #retorna uma exponenciação

#OPERADORES DE COMPARAÇÃO
"""Os operadores de comparação retornam valores booleanos"""

valor_1 = 200
valor_2 = 100

print(valor_1 == valor_2)
print(valor_1 >= valor_2)
print(valor_1 <= valor_2)
print(valor_1 != valor_2)

#OPERADORES DE ATRIBUIÇÕES
saldo = 2000
print(saldo) #atribuição simples

saldo += 200 #soma
print(saldo)

saldo -= 200 #subtração
print(saldo)

saldo /= 200 #divisão com resultado float
print(saldo)

saldo //= 2 #divisão com resultado int. Obs: se o resultado anterior for float, aqui também retorna float
print(saldo)

saldo *= 200 #multiplicação
print(saldo)

saldo **= 2 #exponencicação
print(saldo)

saldo %= 3 #módulo
print(saldo)

#OPERADORES LÓGICOS
"""Tabela Verdade"""

"""print(True and True)
print(True and False)
print (False and False)
print(True or True)
print(True or False)
print (False or False)"""

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite #operador AND (E)
saldo >= saque or saque <= limite #operador OR (OU)

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque)
print(exp)

#OPERADORS DE IDENTIDADE
"""São usados para saber se dois objetos comparados ocupam a mesma posição na memória.
    Os operadores são: IS e IS NOT """

curso = "Curso Python"
nome_curso = curso
saldo, limite = 200,200

curso is nome_curso

#OPERADORES DE ASSOCIAÇÃO
"""São operadores utilizados para verificar se um objeto esta contido em uma sequência
    Os operadores são: IN e NOT IN """

curso = "Curso Python"
frutas = ["Laranja","Uva", "Limão"]
saques = [1500,100]

print("Python" in curso)
print("maçã"  not in frutas)
print(200  in saques)