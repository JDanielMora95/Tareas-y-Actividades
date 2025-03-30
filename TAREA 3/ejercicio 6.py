saldo = 1000
opcion = ""

while opcion != "salir":
    print("\n1. Consultar saldo\n2. Retirar\n3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Saldo actual:", saldo)
    elif opcion == "2":
        cantidad = int(input("¿Cuanto deseas retirar?: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print("Retiro exitoso. Nuevo Saldo:", saldo)
        else:
            print("Fondos insuficientes.")
    elif opcion == "3":
        opcion = "salir"
    else:
        print("Opcion no valida.")

# 1. ¿Qué ventaja tiene match sobre if en este caso?
#    R: Sintaxis más clara y legible.
# 2. ¿Qué pasa si el usuario pone otro símbolo?
#    R: Se mostrará "Opción no válida".
# 3. ¿Qué deberías validar antes de dividir?
#    R: Que el divisor no sea cero, aunque en este código en particular no se realiza ninguna división.