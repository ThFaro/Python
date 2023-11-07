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