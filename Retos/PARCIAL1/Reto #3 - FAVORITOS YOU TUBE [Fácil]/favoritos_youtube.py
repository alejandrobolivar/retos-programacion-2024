'''
PROBLEMA 2. Favoritos de YouTube (6 PUNTOS)
YouTube, es un sitio web en el cual los usuarios pueden subir y compartir videos. La empresa desea realizar
algunos estudios relacionados con las visitas y los videos más visitados en el sitio web, con el fin de mejorar
el servicio que presta a todos sus visitantes. Diariamente se lleva un registro de los datos de cada video
conformado por:
Código, Tipo, Cantidad de visitas del día anterior, Cantidad de visitas del día actual
YouTube, le ha contratado a Ud. para que desarrolle un programa que procese la información indicada
anteriormente y determine e imprima:
Para cada video:
1. Un mensaje que indique si el video está entre los favoritos o no.
Para todos los videos:
2. ¿Cuántos videos están fuera de los favoritos?
3. Porcentaje de videos de Cine con respecto al total de videos registrados.
4. Código del video con el menor incremento de visitas. Si existe más de un video con el mismo menor
incremento, indique el que tiene la menor cantidad de visitas del día anterior.
Consideraciones:
• El tipo de video es: 1= Música, 2= Comedia, 3=Deportes, 4= Cine.
• El video está entre los favoritos si se mantiene o incrementa la cantidad de visitas
'''
# Declaracion de variables
# Variables de entrada
codigo: str # Código del video
tipo: int # Tipo de video
visitas_ant: int # Cantidad de visitas del dia anterior
visitas_act: int # Cantidad de visitas del dia actual
# Variables de proceso
band: int # Bandera para obtener el codigo del video con mayor incremento de visitas
cent: int # Centinela para el control de ciclo while
incremento: int # incremento de visitas del video
incremento_mayor: int # variable que guarda el mayor incremento de visitas
anterior_m: int # Variable que guarda el numero de visitas del video con mayor incremento que se compara con otro video del mismo incremento de visitas

# Variables de salida
porct: float # Porcentaje de videos de musica respecto al total de videos registrados
codigo_m: str # Código del video con mayor incremento de visitas
cont1: int
cont2: int
cont3: int # contadores: 1 videos favoritos, 2 videos de musica, 3 videos registrados
# inicializacion de variables
cont1 = 0
cont2 = 0
cont3 = 0
cent = input("Hay datos que procesar? 1 (si)/2 (no):  ")
# ciclo para datos desconocidos
while cent == 1:
    # Proceso de lectura
    codigo = input("Ingrese el código del video: ")
    tipo = input("Ingrese el tipo de video: (1)Música, (2)Comedia, (3)Deportes, (4)Cine ")
    visitas_ant = input("Ingrese la cantidad de visitas del dia anterior: ")
    visitas_act = input("Ingrese la cantidad de visitas del dia actual: ")

    # Verificar si el video es favorito o no
    if visitas_act >= visitas_ant:
        print("Este video se encuentra entre los favoritos!!")
        cont1 += 1 # contador de videos favoritos
    else:
        print("Este video NO se encuentra entre los favoritos!!")

    # cantidad de videos de musica
    if tipo == 1:
        cont2 += 1

    # calculo del incremento de visitas
    incremento = visitas_act - visitas_ant
    if incremento > 0:
        # codigo del video con el mayor incremento de visitas
        if band == 0:
            codigo_m = codigo
            incremento_mayor = incremento
            anterior_m = visitas_ant
            band = 1
        elif incremento > incremento_mayor:
            codigo_m = codigo
            incremento_mayor = incremento
            anterior_m = visitas_ant
        elif incremento == incremento_mayor: # si exite mas de un video con el mismo mayor incremento se indica el de mayor visitas del dia anterior
            if anterior_m < visitas_ant:
                codigo_m = codigo

    # contador de videos registrados
    cont3 += 1
    # pregunto si hay mas videos
    cent = input("Desea ingresar otro video? (1)Si ,(2)No")

if cont1 != 0:
    print("Entre los favoritos sen encuentran ", cont1, " video(s)")
else:
    print("No hay videos favoritos")

# calculo de porcentaje de videos de musica respecto al total
if cont3 > 0:
    porct = (cont2 / cont3) * 100
    print("El porcentaje de videos de musica con respecto al total de videos registrados fue de ", porct, "%")

if band == 1:
    print("El video con mayor incremento de visitas fue el del codigo : ", codigo_m)
else:
    print("Ningun video obtuvo un incremento de visitas")

print(input"Pulse una tecla para continuar"))