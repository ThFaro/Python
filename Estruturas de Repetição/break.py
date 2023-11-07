while True:
    numero = int(input("Adivinhe o número de 1 a 100: "))

    if numero == 10:
        print ("Voce acertou!")
        break
    
    print("Errou. Tente novamente!")

    # existe o continue que serve para ignorar determinada variavel/condição.