#Pedimos los numeros
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
variable_Alt = numero1
#cambiamos valores
numero1 = numero2
numero2 = variable_Alt
#Imprimimos el resultado
print(f"El primer número es: {numero1}")
print(f"El segundo número es: {numero2}")