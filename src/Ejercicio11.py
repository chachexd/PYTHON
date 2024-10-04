#Pedimos la Hora
hora = int(input("Hora de salida (HH): "))
minuto = int(input("Minutos de salida (MM): "))
segundo = int(input("Segundos de salida (SS): "))
#pedimos el tiempo en segundos
tiempo_viaje = int(input("Tiempo de viaje en segundos: "))
#Convertimos
tiempo_total_segundos = (hora * 3600) + (minuto * 60) + segundo + tiempo_viaje

hora_llegada = (tiempo_total_segundos // 3600) % 24  # Para formato 24 horas
minuto_llegada = (tiempo_total_segundos % 3600) // 60
segundo_llegada = tiempo_total_segundos % 60

#Imprimimos el resultado con el formato en decimal correcto
print(f"La hora de llegada será: {hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")
