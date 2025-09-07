calificacion = int(input("Ingresa la calificacion del (0-100): "))

if 90 <= calificacion <= 100:
    print("Tu calificacion es: A")
elif 80 <= calificacion <= 89:
    print("Tu calificacion es: B")
elif 70 <= calificacion <=79:
    print("Tu calificacion es: C")
elif 60 <= calificacion <=69:
    print("Tu calificacion es:")
else:
    print("Tu calificacion es: F")
