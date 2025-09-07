lado1=float(input("intruduce la primera longuitud: "))
lado2=float(input("introduce la segunda longuitud: "))
lado3=float(input("introduce la tercera longuitud: "))

if lado1 == lado2 == lado3:
    print("El triangulo es equilatero:")
elif lado1 ==lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isoceles")
else:
    print("el triangulo es escaleno")