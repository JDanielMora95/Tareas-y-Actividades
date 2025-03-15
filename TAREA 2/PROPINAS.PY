
    total = float(input("Ingresa el total de la cuenta: "))
    porcentaje = int(input("Ingresa el porcentaje de propina (10, 15, 20): "))
    propina = total * (porcentaje / 100)
    total_pagar = total + propina
    print(f"Debes pagar en total: {total_pagar:.2f}")