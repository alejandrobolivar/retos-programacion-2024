'''
Competencia Aérea
Se encontraban Phineas y Ferb viendo un programa en el canal de documentales,
cuando Phineas dice: Ferb, ¡ya se que vamos a hacer hoy!
Así fue como se les ocurrio la sorprendente idea de realizar una carrera en aeronaves
con sus amigos. Como es de suponer, no podian pedirles aviones de verdad a sus
padres, asi que decidieron diseñar y ensamblar sus propios aviones y los de sus amigos.
Antes de iniciar la carrera, declararon que Perry el ornitorrinco sería el juez encargado
de anunciar al ganador. Perry se aprovechó de su tecnología de super agente secreto y
colocó un dispositivo rastreador GPS en cada avión participante.
Al final de la competencia, los rastreadores proporcionarán los siguientes datos, para
cada uno de los aviones participantes:
IDENTIFICACIÓN DEL AVIÓN, DISTANCIA TOTAL RECORRIDA (EXPRESADA EN KM) Y TIEMPO DE DURACIÓN DEL VUELO (EXPRESADO EN
MINUTOS)
Esta información se encuentra almacenada en el archivo competidores.txt. Por lo que, Perry necesita que usted
desarrolle un programa que lea los datos del archivo, y determine e imprima en otro archivo de nombre
resultados.txt lo siguiente:
Para cada competidor:
 Identificación del avión, un mensaje que indique si llegó a la meta o no, y
 Velocidad de vuelo del avión expresada en Km/h.
Para todos los competidores:
 Porcentaje de competidores que no llegaron a la meta,
 Identificación del avión ganador.
Consideraciones
 No todos los aviones pudieron llegar a la meta por defectos técnicos.
 La meta se encuentra a 4600 Km del punto de partida y el ganador será aquel que haya recorrido una
distancia mayor o igual a 4600 Km con la mayor velocidad.
 Utilice los siguientes datos de ejemplo para el diseño de su archivo:

Identificación Distancia Tiempo
MAC18F 4800 338.4
FERB1A 3500 201.6
MOB05C 3800 375
PHINEAS16 4780 336.6
BEB30L 4601 370.8
ABC47A 4500 293.4
'''


'Declaración de variables

# Entrada
Identificacion: str = " "
Distancia: float
Tiempo: float

# Proceso
Velocidad: float
Cont_Total: int
Cont_NoLlegaron: int
band: int
DistanciaMayor: float
VelocidadMayor: float

# Salida
Porcentaje: float
Ident_Ganador: str = " "

# Inicialización de variables
Cont_Total = 0
Cont_NoLlegaron = 0
band = 0

# Archivos
arch1 = open("competidores.txt", 'r')
arch2 = open("resultados.txt", 'w')

# Recorrido del archivo
for registro in arch1:
    # Devuelve una lista con los campos del registro
    linea = registro.split(',')

    Identificacion  = linea[0]
    Distancia = float(linea[0])
    Tiempo = float(linea[0])

    Cont_Total = Cont_Total + 1

    if Tiempo != 0:
        Velocidad = Distancia / Tiempo
    else:
        Velocidad = 0

    if Distancia >= 4600 and Velocidad != 0:
        arch2.write("El avión " & Identificacion & " SI logró llegar a la meta y su velocidad de vuelo fue " & Format(Velocidad, "00.00") & " km/h")
        PrintLine(2)

        if band == 0:
            band = 1
            DistanciaMayor = Distancia
            VelocidadMayor = Velocidad
            Ident_Ganador = Identificacion
        elif Velocidad > VelocidadMayor:
            DistanciaMayor = Distancia
            VelocidadMayor = Velocidad
            Ident_Ganador = Identificacion

    elif Distancia < 4600:
        arch2.write("El avión " & Identificacion & " NO logró llegar a la meta y su velocidad de vuelo fue " & Format(Velocidad, "00.00") & " km/h")
        PrintLine(2)
        Cont_NoLlegaron = Cont_NoLlegaron + 1
    else:
        arch2.write("El avión " & Identificacion & " no participó en la competencia")

if Cont_Total != 0:
    Porcentaje = Cont_NoLlegaron / Cont_Total * 100
    arch2.write("Porcentaje de participantes que no llegaron a la meta: " & Format(Porcentaje, "00.00") & "%")
    PrintLine(2)
else:
    arch2.write("No hubo participantes en la competencia")
    PrintLine(2)

if band == 1:
    arch2.write("El avión ganador fue: " & Ident_Ganador)

arch1.close()
arch2.close()