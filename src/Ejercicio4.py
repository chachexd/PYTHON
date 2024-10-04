#Pedimos los numeros
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
# Calcula las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
#Comprobamos que 2 no sea 0
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre 0"

#Imprimimos los resultados
print(f"La suma de los dos números es: {suma}")
print(f"La resta de los dos números es: {resta}")
print(f"La multiplicación de los dos números es: {multiplicacion}")
print(f"La división de los dos números es: {division}")
