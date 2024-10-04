#Pedir numero
numero = int(input("Introduce un número de dos cifras: "))

#Calculamnos
decenas = numero // 10  # Obtiene la parte de las decenas
unidades = numero % 10  # Obtiene la parte de las unidades
#Generamos resultado
numero_invertido = (unidades * 10) + decenas

#Imprimimos el número invertido
print(f"El número invertido es: {numero_invertido}")
