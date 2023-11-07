import sys

saldo = 200.0
opcao = int(input("Informe uma opção desejada: \n [1]Sacar \n [2] Extrato: "))

if opcao == 1:
    saque = float(input("Informe o valor desejado: "))
    if saque <= saldo:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif opcao == 2:
    print("Exibindo extrato...", saldo)

else:
    sys.exit("Opção inválida!")
