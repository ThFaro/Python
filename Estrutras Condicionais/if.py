saldo = 200.0
saque  = float(input("Informe o valor desejado: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")

if saldo < saque:
    print("Saldo insuficiente!")