edad = int(input("Ingresa tu edad: "))

if edad < 12:
    costo = 50
elif edad >= 12 and edad <= 17:
    costo = 80
else:
    costo = 120

print(f"El costo de la entrada es de ${costo}.")