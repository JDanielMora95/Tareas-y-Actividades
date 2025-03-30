def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

print(es_primo(13)) # True

#
'''if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")'''