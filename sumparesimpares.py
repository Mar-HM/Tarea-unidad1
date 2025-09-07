
n = int(input("Ingresa un número: "))

suma_pares = 0
suma_impares = 0

for i in range(1, n + 1):
    
    if i % 2 == 0:
        suma_pares = suma_pares + i

    else:
        suma_impares = suma_impares + i

print("La suma de los números pares hasta", n, "es:", suma_pares)
print("La suma de los números impares hasta", n, "es:", suma_impares)