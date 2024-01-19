# Enunciado: Pregunta Nro 1 - Cean 2023
'''
El juego Tetris consiste en colocar piezas en un tablero con el fin de completar líneas y mientras más líneas se completen en la colocación de una pieza en el tablero, mayor será el puntaje a obtener. El juego finaliza cuando por errores del competidor el agrupamiento de piezas llega a la cima del tablero.
Ya que se acerca el día del estudiante, la Facultad de Ingeniería de la Universidad de Carabobo, decide abrir una competencia de Tetris, con el fin de estimular más a sus estudiantes en querer su facultad. Para ello creara un archivo de datos de nombre “Partidas.Txt”, en el cual en la primera línea aparece la fecha de la competencia y posteriormente se registró para cada competidor que participó:
NOMBRE Y ESCUELA A LA QUE PERTENECE
Y para cada Pieza que completa al menos una línea o que finaliza el juego
TIPO DE PIEZA Y CUANTAS LÍNEAS SE COMPLETAN AL COLOCAR LA PIEZA
(Si la pieza es la que finaliza el juego su valor es cero).
Elabore un programa que empleando el archivo de datos “Partidas.Txt”, genere el archivo de datos “Desempeño.Txt” donde para cada competidor indique:
1. Nombre del competidor, Escuela a la que pertenece, Cantidad de líneas completadas y Puntaje final obtenido.
2. Porcentaje de veces que completo un Tetris con respecto a las piezas que lograron completar al menos una línea.
Además determine e imprima por consola Para todos los competidores:
3. Promedio de puntos obtenidos.
4. Nombre y cantidad de líneas formadas por el competidor que gana la competencia. En caso de haber más de uno reporte el primero que procesó e indique cuantos además de él lograron la hazaña.

Consideraciones:
 Los puntajes a obtener por formación de líneas al colocar una pieza en el tablero son: 800 si forma un Tetris (I,4), 400 para un trio de líneas, 200 una pareja y 100 puntos para la formación de una sola línea.
 El tipo de pieza se establece como: I T O LDer Liz SDer SIz

'''
# Variables de entrada
fecha: str
nom: str
esc: str
tpieza: str
nlineas: int

# Variables de salida
acum_lineas: int
puntaje: int
porc_tetris: float
prom_puntos: float
nom_gan: int
lineas_max: int
cmax: int = 0

# Variables Auxiliares
acum_puntaje: int = 0
puntaje_max: int
cant_tetris: int
cant_piezas: int
cant_competidores: int = 0

# Apertura de Archivos
arch1 = open("partidas.txt", 'r')
arch2 = open("desempeño.txt", 'w')

# Lectura de la fecha
fecha = arch1.readline()

# Ciclo de lectura
# Para cada Competidor
while True:
    linea = arch1.readline()
    if linea == '':
        break
    lst_ext = linea.strip().split(',')
    nom = lst_ext[0]
    esc = lst_ext[1]
    cant_competidores += 1
    puntaje = 0
    nlineas = 8 # valor para entrar al ciclo
    cant_piezas = 0
    cant_tetris = 0
    acum_lineas = 0

    # Para cada pieza
    while nlineas != 0:
        linea = arch1.readline()
        lst_int = linea.strip().split(',')
        tpieza = lst_int[0]
        nlineas = int(lst_int[1])
        acum_lineas += nlineas
        cant_piezas += 1

        # Determinacion del puntaje
        if nlineas == 1:
            puntaje += 100
        elif nlineas == 2:
            puntaje += 200
        elif nlineas == 3:
            puntaje += 400
        elif nlineas == 4:
            puntaje += 800
            cant_tetris += 1

    # Calculos Finales e impresiones para cada Competidor
    porc_tetris = cant_tetris * 100 / (cant_piezas - 1)

    # Impresiones por archivo
    arch2.write(f'{nom}, {esc}, {acum_lineas}, {puntaje}\n')
    arch2.write(f'Porcentaje de tetris = {porc_tetris:.2f}%\n')
    acum_puntaje += puntaje

    # Búsqueda del mayor
    if cant_competidores == 1:
        nom_gan = nom
        lineas_max = acum_lineas
        puntaje_max = puntaje
        cmax = 0
    elif puntaje > puntaje_max:
        nom_gan = nom
        lineas_max = acum_lineas
        puntaje_max = puntaje
        cmax = 0
    elif puntaje == puntaje_max:
        cmax += 1

# Calculos Finales e Impresiones para todos los competidores
prom_puntos = acum_puntaje / cant_competidores
print(f'Promedio de puntos = {prom_puntos:.2f}')
print(f'El ganador de la competencia es = {nom_gan} Formando {lineas_max}')
if cmax > 0:
    print(f'Y además de él hay {cmax} Empates')

# Cierre de archivos
arch1.close()
arch2.close()