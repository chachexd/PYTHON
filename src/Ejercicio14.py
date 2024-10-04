#Pedimos las monedas
monedas_2euros = int(input("Monedas de 2€: "))
monedas_1euro = int(input("Monedas de 1€: "))
monedas_50c = int(input("Monedas de 50 céntimos: "))
monedas_20c = int(input("Monedas de 20 céntimos: "))
monedas_10c = int(input("Monedas de 10 céntimos: "))
#Calculamos
total_centimos = (monedas_2euros * 200) + (monedas_1euro * 100) + (monedas_50c * 50) + (monedas_20c * 20) + (monedas_10c * 10)
#convertimos
euros = total_centimos // 100  # División entera para obtener los euros
centimos = total_centimos % 100  # Resto para obtener los céntimos
#Imprimimos el resultado
print(f"Tienes un total de {euros} euros y {centimos} céntimos.")
