#Pedimos el nombre y apellidos
nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

#Sacamos las letras con su posicion
iniciales = nombre[0].upper() + "." + apellido1[0].upper() + "." + apellido2[0].upper()

#Imprimimos el resultado
print(f"Las iniciales son: {iniciales}")
