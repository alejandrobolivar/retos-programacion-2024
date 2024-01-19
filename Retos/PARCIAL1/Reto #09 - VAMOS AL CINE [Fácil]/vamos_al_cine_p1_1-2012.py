'''
PROBLEMA. VAMOS AL CINE (14 PUNTOS)
Gracias a la situación de inseguridad en la que están sometidos a diario los profesores
de la Facultad de Ingeniería, hemos decidido llevarlos al cine con sus familiares a ver
LOS VENGADORES, para que tomen algunos ejemplos que puedan aplicar en la vida
real. Pero como no sólo nos aqueja la inseguridad sino la inflación, debemos evaluar el
presupuesto, según el día libre de cada profesor y su grupo familiar, para así poder
cubrir los gastos de las entradas. Para esto tenemos:
UN MONTO EN Bs, que fue donado por el Decano
Además de los siguientes datos de un grupo de V profesores de la Facultad:
NOMBRE, DEPARTAMENTO, DÍA LIBRE, CANTIDAD DE PERSONAS QUE
FORMAN EL GRUPO FAMILIAR y CUANTOS DE ELLOS SON NIÑOS
Desarrolle un programa tipo Aplicación de Consola VB2010 que procese la información anterior y determine e imprima:
Para cada profesor:
1. Monto a pagar por las entradas. (1 punto)
2. Cuanto queda de la Donación del Decano luego de cubrir los gastos del profesor. (1 punto)
Para todos:
3. Nombre del Profesor y monto a pagar, con el grupo familiar más numeroso que gastaría menos en la compra de
las entradas. (2 puntos)
4. Porcentaje de niños con respecto al total de personas que van a ir al cine. (1.5 puntos)
5. Nombre del último Profesor de la lista que pertenece al Departamento de Computación que puede ir un lunes al
cine. (1 punto)
6. Qué porcentaje de los gastos totales es cubierta con la donación del Decano. (1 punto)
Consideraciones:
1. El DÍA LIBRE se debe considerar como: LUNES, MARTES, MIÉRCOLES, JUEVES, VIERNES, SÁBADO o DOMINGO.
2. El valor de las entradas es el siguiente:
a. Para todo niño 14.50 Bs.
b. Para todo adulto, dependerá del día:
ENTRADA VALOR
Lunes Popular 14.50
Jueves para ti 19.00
Boletos General (resto de los días de la semana) 29.00
'''

# Variables de entrada
monto_decano: float
monto_menor: float
V: int
cantidad_familia: int
niños: int
nombre: str
departamento: str
dia_libre: str

# Variables de salida
nombre_ultimo: str
nombre_mayor: str
monto_pagar: float
porcentaje_niños: float
monto_restante: float
porcentaje_decano: float

# variables de proceso
acumulador_familia: int
acumulador_niños: int
band: int
familia_mayor: int
band_u: int
acumulador_monto: float = 0 # si hay un sola variable declarada se puede inicializar ahí

monto_decano = input("Escriba el monto dado por el decano en BsF: ")
V = input("Escriba la cantidad de profesores: ")

print("-------------------------------------------") # Solo para darle formato a la consola

acumulador_familia = 0
acumulador_niños = 0
band = 0
band_u = 0
familia_mayor = 0

for _ in range(V):
    nombre = input("Nombre: ")
    departamento = input("Departamento: ")
    dia_libre = input("Día Libre: ")
    cantidad_familia = input("Cantidad de Personas que forman su grupo familiar: ") # Incluyendo el profesor

    acumulador_familia += cantidad_familia

    niños = input("¿Cuántos Niños hay en su grupo familiar?: ")

    acumulador_niños += niños

    # El Ucase(variable) nos asegura que las letras de la variable van a ser evaluadas siempre en mayúsculas
    if dia_libre.upper() == "LUNES":
        monto_pagar = cantidad_familia * 14.5
    elif dia_libre.upper() == "JUEVES":
        monto_pagar = (cantidad_familia - niños) * 19 + niños * 14.5
    else:
        monto_pagar = (cantidad_familia - niños) * 29 + niños * 14.5

    acumulador_monto += monto_pagar
    print("El monto a pagar por las entradas es: ", monto_pagar, " BsF")
    # Para imprimir variables se puede unir la frase que yo quiero escribir junto con una variable por medio del,, colocando "...", variable

    monto_restante = monto_decano - acumulador_monto

    if monto_restante > 0:
        print("Queda {0} BsF de la donación del Decano", monto_restante)
        # Otra forma de imprimir una variable es indicar donde se va a imprimir la varible mediante {} y luego la variable en cuestión, colocando "...{0}...",variable

    else:
        print("No queda mas dinero de la donación del decano")

    if departamento.upper() == "COMPUTACION" and dia_libre.upper() == "LUNES":
        nombre_ultimo = nombre
        band_u = 1

    print("-------------------------------------------") # Solo para darle formato a la consola

    if band == 0:
        band = 1
        familia_mayor = cantidad_familia
        nombre_mayor = nombre
        monto_menor = monto_pagar
    else:
        if cantidad_familia > familia_mayor:
            familia_mayor = cantidad_familia
            nombre_mayor = nombre
            monto_menor = monto_pagar

        if cantidad_familia == familia_mayor:
            if monto_pagar < monto_menor:
                nombre_mayor = nombre
                monto_menor = monto_pagar

if band != 0:
    print(nombre_mayor, " es el Prof que tiene el grupo familiar mas numeroso que gastaría menos")

if acumulador_familia != 0:
    porcentaje_niños = acumulador_niños / acumulador_familia * 100
    print("El porcentaje de niños es de {0}%", porcentaje_niños)

if band_u == 0:
    print("No hubo profesor que fuera de Computación y además tuviera libre el lunes")
else:
    print(nombre_ultimo, " es último Profesor de la lista que pertenece al Departamento de Computación que puede ir un lunes al cine")

if acumulador_monto > monto_decano:
    porcentaje_decano = monto_decano / acumulador_monto * 100
    print("La donación del decano cubrió el {0}% del monto total", porcentaje_decano)
else:
    print("La donación del decano cubrió la totalidad del monto total")