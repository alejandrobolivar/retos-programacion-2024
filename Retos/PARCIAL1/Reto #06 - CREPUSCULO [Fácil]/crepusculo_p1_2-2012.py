'''
1ERA PARTE. CREPÚSCULO: EPISODIO FINAL.
Después de cuatro libros y cinco películas, finalmente llega el tan
esperado final de esta novela romántica sobre vampiros, escrita por
Stephenie Meyer. El pasado 16 de noviembre, llegó a las salas de cine la
segunda parte de “Amanecer”; por tratarse del estreno de la última
película de la saga, en un cine de Valencia se decidió proyectar un
maratón con las cinco películas.
Ante la gran cantidad de fanáticos que llegaron ese día al cine para el
maratón, se decidió levantar ciertas estadísticas para saber qué tan
bueno fue este estreno, para esto se tiene por cada fanático:
NOMBRE, HORA Y MINUTOS DE LLEGADA, HORA Y MINUTOS DE SALIDA
Elabore una aplicación de consola de Visual Basic 2010 que procese la información anterior y determine e
imprima:
Por cada fanático:
1. Tiempo total que permaneció en el cine, expresado en minutos.
2. Cual fue la primera película que logró ver el fanático, si no logró ver ninguna indíquelo.
Para todos los fanáticos:
3. Porcentaje de fanáticos que estuvieron presentes en la proyección de “Amanecer (Parte 2)”.
4. Tiempo promedio en minutos que duraron esperando los fanáticos el inicio del maratón.
5. Nombre del mayor fanático de esta saga.
CONSIDERACIONES:
• Considere que en la sala de cine solamente hay cupo para 150 fanáticos.
• Tanto la hora de llegada como la hora de salida están expresadas en formato militar.
• Un fanático estuvo presente en la proyección de una película si llega al menos un minuto antes de que
la misma termine.
• El mayor fanático de esta saga será aquel que estuvo más tiempo en el cine y que vio todo el maratón.
• La proyección de la primera película de la saga comenzó a las 12:00hrs (720 min del día).
• Tan pronto termina una película, comienza la otra, sin interrupciones de ningún tipo.

Nombre de la película Crepúsculo Luna Nueva Eclipse Amanecer Amanecer (parte2)
Tiempo de duración      90 min   120 min    150 min  120 min    150 min
Minutos del día       720        810        930     1080     1200              1350
'''

# Declaracion de variables
nombre_fanatico: str
hora_llegada: int
min_llegada: int
hora_salida: int
min_salida: int
contador_total_fanaticos: int
tiempo_fanatico_minutos: int
contador_amanecer_2: int
b: int
acumulador_minutos: int
contador_fanaticos_esperando: int
llegada_minutos: int
salida_minutos: int
prom: float
por: float
min_max: int
nom_max: str
cent: int

# Inicializacion de variables
contador_amanecer_2 = 0
contador_fanaticos_esperando = 0
contador_total_fanaticos = 0
b = 0
acumulador_minutos = 0
cent = 0

# Ciclo para procesar la lista
while (cent == 0) and (contador_total_fanaticos < 150):
    # Lectura de los datos de la lista
    nombre_fanatico = input("Introduzca el nombre del fanático")
    hora_llegada = int(input("Introduzca la hora de llegada"))
    min_llegada = int(input("Introduzca los minutos de llegada"))
    hora_salida = int(input("Introduzca la hora de salida"))
    min_salida = int(input("Introduzca los minutos de salida"))
    cent = int(input("Desea procesar otro fanático? (0:SI / 1: NO)"))

    # Contador total de fanaticos (Para detectar si se llena la sala y calculo del porcentaje)
    contador_total_fanaticos += 1

    # Conversion de la llegada y salida de horas y minutos a minutos
    llegada_minutos = (hora_llegada * 60) + min_llegada
    salida_minutos = (hora_salida * 60) + min_salida

    # Calculo e impresion del tiempo en minutos que permanecio el fanático en el cine
    tiempo_fanatico_minutos = salida_minutos - llegada_minutos
    print("El fanático: ", nombre_fanatico, " permaneció ", tiempo_fanatico_minutos, " minutos en el cine")

    # Primera película que logro ver el fanático
    if (salida_minutos < 720):
        print("El fanático no vio ninguna película")
    elif (llegada_minutos < 810):
        print("La primera película que el fanático vio fue Crepusculo")
    elif (llegada_minutos < 930):
        print("La primera película que el fanático vio fue Luna Nueva")
    elif (llegada_minutos < 1080):
        print("La primera película que el fanático vio fue Eclipse")
    elif (llegada_minutos < 1200):
        print("La primera película que el fanático vio fue Amanecer")
    elif (llegada_minutos < 1350):
        print("La primera película que el fanático vio fue Amanecer parte 2")

    # Contador de fanaticos que estuvieron presentes en amanecer parte 2 (Para el calculo del porcentaje)
    if (salida_minutos >= 1200):
        contador_amanecer_2 += 1

    # Promedio en minutos que duraron esperando los fanaticos el inicio del maraton
    if (llegada_minutos < 720) and (salida_minutos >= 720):
        acumulador_minutos = acumulador_minutos + (720 - llegada_minutos)
        contador_fanaticos_esperando += 1

    # Determinar el mayor fanático
    if llegada_minutos <= 720 and salida_minutos >= 1350:
        if b == 0:
            b = 1
            nom_max = nombre_fanatico
            min_max = tiempo_fanatico_minutos
        elif tiempo_fanatico_minutos > min_max:
            nom_max = nombre_fanatico
            min_max = tiempo_fanatico_minutos

# Mensaje adicional que le indica al usuario si la sala se lleno
if contador_total_fanaticos == 150:
    print("Disculpe, la sala se llenó, ya no se puede procesar mas fanáticos")

# Cálculo e impresión del porcentaje
por = (contador_amanecer_2 / contador_total_fanaticos) * 100
print("Porcentaje de fanaticos presentes en Amanecer parte 2: ", por, "%")

# Tiempo promedio de los fanáticos que llegaron temprano
if (contador_fanaticos_esperando != 0):
    prom = acumulador_minutos / contador_fanaticos_esperando
    print("Tiempo promedio en minutos que duraron esperando los fanáticos el inicio del maratón: ", prom)
else:
    print("Ningun fanático se quedó esperando")

# Impresión del mayor
if b == 0:
    print("ninguno de los procesados se considera como mayor fanático de la saga")
else:
    print("El mayor fanático de la saga fue: ", nom_max)

input("Presione cualquier tecla para continuar...")