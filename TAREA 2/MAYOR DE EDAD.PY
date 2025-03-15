edad = 20

    edad = int(input("Ingresa tu edad: "))
    if edad < 18:
        print("¡Lo siento, no puedes entrar!")
    elif 18 <= edad <= 21:
        print("Puedes entrar, pero sin bebidas alcohólicas.")
    else:
        print("¡Bienvenido!")