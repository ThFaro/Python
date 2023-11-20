nome = 'Thiago'

mensagem = f"""
Olá, meu nome é {nome},
        Eu sou programador

                Fim.
"""

print (mensagem)

print (''' 
    ======== MENU ========

    1-Saque
    2-Extrato
    3-Saldo
    4-Transferencia
    5-PIX
    6-SAIR

    =====================

         Obrigado
''')


T = int(input("Ola"))
if T > 140:
    print("MUTE")
else:
    print("TWEET")