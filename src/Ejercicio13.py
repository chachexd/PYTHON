#Pedimos las respuestas
correctas = int(input("Respuestas correctas: "))
incorrectas = int(input("Respuestas incorrectas: "))
blanco = int(input("Respuestas en blanco: "))
#Calculamos
nota_final = (correctas * 5) + (incorrectas * -1) + (blanco * 0)
#Imprimimos el resultado
print(f"La nota final del estudiante es: {nota_final}")
