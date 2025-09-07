
numero = int(input("Ingresa un número para invertir: "))

es_negativo = False
if numero < 0:
    es_negativo = True
    numero = -numero
    

numero_invertido = 0


while numero > 0:
    ultimo_digito = numero % 10 
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero = numero // 10 

if es_negativo:
    numero_invertido = -numero_invertido


print("El número invertido es:", numero_invertido)