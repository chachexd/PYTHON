#Pedimos los minutos
minutos_totales = int(input("Introduce la cantidad de minutos: "))

#Calculamos las horas
horas = minutos_totales // 60  
#Calculamos resto
minutos_restantes = minutos_totales % 60  

#Imprimimos el resultado
print(f"{minutos_totales} minutos son {horas}h:{minutos_restantes}m.")
