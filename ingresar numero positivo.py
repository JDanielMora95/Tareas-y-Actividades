def calcular_suma():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                break
            else:
                print("Error: El número debe ser mayor que cero.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    
    suma = sum(range(1, numero + 1))
    print(f"La suma de los números de 1 a {numero} es: {suma}")

calcular_suma()
