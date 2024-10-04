#Solicitamos la distancia entre los vehículos y sus velocidades
distancia = float(input("Distancia entre los dos vehículos (km): "))
v1 = float(input("Velocidad del primer vehículo (km/h): "))  
v2 = float(input("Velocidad del segundo vehículo (km/h): "))  

#Calculamos
if v2 > v1:
    
    diferencia_v = v2 - v1
    tiempo_horas = distancia / diferencia_v
    tiempo_minutos = tiempo_horas * 60

    #Imprimimos el resultado
    print(f"Alcanzará al otro en {tiempo_minutos:.2f} minutos.")
else:
    
    print("El segundo vehículo no es más rápido que el primero, por lo tanto, no lo alcanzará.")
