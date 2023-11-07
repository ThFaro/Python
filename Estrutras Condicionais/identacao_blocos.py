"""A identação em java é determinada pelo : demarcando o inicio de método, 
e para saber o que faz parte de cada bloco, são utilados 4 espaços"""

def sacar(valor:float): #inicio do bloco
    saldo = 500 #contem 4 espaços, portanto esta dentro do metodo

    if saldo >=valor: # inicio do if
        print("Saque realizado com sucesso") #possui 8 espaços, portanto esta dentro do if
        print("Retire o dinheiro na boca do caixa") #possui 8 espaços, portanto esta dentro do if

    #fim do if

    print("Obrigado por escolher nosso banco, tenha um bom dia") #sempre será impressa pois nao faz parte do if

sacar(100)

