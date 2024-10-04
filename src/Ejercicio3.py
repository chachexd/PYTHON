#importamos la libreria math que nos ayudara a operaciones matematicas
import math  
#Pedimos los catetos
cateto1 = float(input("Introduce el valor del primer cateto: "))
cateto2 = float(input("Introduce el valor del segundo cateto: "))

#Calculamos
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

#imprimimos
print(f"La hipotenusa del triángulo es: {hipotenusa}")
