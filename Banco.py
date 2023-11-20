menu = """

[D]Deposito
[S]Saque
[E]Extrato
[Q]Sair

==> """

saldo = 100.00
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Qual valor você deseja depositar:'))

        if valor > 0:
            saldo += valor
            print("Depósito Realizado com sucesso")
            extrato += f'{saldo:.2f}\n'
        else:
            print('Depósito inválido')

    elif opcao == 's':
        valor = float(input('Qual valor você deseja sacar:'))

        if numero_saques < LIMITE_SAQUE:
            if saldo >= valor and valor <= limite:
                saldo -= valor
                print('Saque realizado com sucesso')
                extrato += f'Saque: -{valor:.2f}\n'
                numero_saques += 1  
            elif valor > limite:
                print('Limite de saque por operação excedido')
            elif valor > saldo:
                print('Saldo insuficiente')
        else:
            print('Limite de saques diários excedido!')

    elif opcao == 'e':
        print("Extrato atual:")
        print(saldo)

    elif opcao == 'q':
        break

    else:
        print('Opção inválida')
