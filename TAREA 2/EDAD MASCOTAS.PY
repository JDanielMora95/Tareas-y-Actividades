
tipo = input("¿Tu mascota es un perro o un gato?: ").lower()
    edad = int(input("Ingresa la edad de tu mascota en años: "))
    if tipo == "perro":
        print(f"Su edad en años humanos es: {edad * 7}")
    elif tipo == "gato":
        print(f"Su edad en años humanos es: {edad * 5}")
    else:
        print("Solo aceptamos perros o gatos.")
