# sourcery skip: merge-else-if-into-elif, swap-nested-ifs, switch
'''
Pregunta 2. Pesos Pesados
ENTRADA: ¿Qué Tengo? SALIDA: ¿Qué Quiero Lograr? PROCESO: ¿Cómo lo Hago?
El índice de masa corporal (IMC) es una medida de
asociación entre el peso y la talla de un individuo, que se
calcula con la expresión matemática: imc=peso/talla**2
Donde:
IMC: Corresponde al índice de masa corporal
PESO: Corresponde al peso del individuo (kg).
TALLA: Corresponde a la estatura del individuo (m).

ÍNDICE DE MASA CORPORAL
MUJERES     HOMBRES     INTERPRETACIÓN DEL IMC
MENOR A 20  MENOR A 20  BAJO PESO
20 - 24.9   20-23.9     PESO NORMAL
25-29.9     24-28.9     OBESIDAD TIPO 1
30-40       29-37       OBESIDAD TIPO 2
MAYOR QUE 40 MAYOR QUE 37 OBESIDAD TIPO 3
Dados los datos de un grupo de M personas: NOMBRE, SEXO, PESO Y ESTATURA. Desarrolle un programa en Visual Basic
que procese dicha información y determine e imprima, según el IMC:
1. Para cada persona, Si es obesa, un mensaje que indique el tipo de Obesidad.
2. Promedio de IMC de Hombres que se encuentran por encima del Peso Normal.
3. Nombre de la primera mujer Obesa en procesarse y cuántas mujeres además de ella se ubican en el mismo
tipo de obesidad.
4. Nombre y sexo de la persona de bajo peso que tiene la menor talla.
'''


# Variables a Leer del Usuario (Entrada)
M: int # Cantidad de Personas (Lista de Tamaño conocido)
Nombre: str # Nombre de la Persona
Sexo: str # Genero de la Persona
Peso: float # Peso en Kg de la Persona
Estatura: float # Talla en m de la Persona

# Resultados a Mostrar al Usuario (Salida)
Interpretacion_IMC: int # 1=Bajo, 2=Normal, 3=Obeso 1, 4=Obeso 2, 5=Obeso 3
Pro: float # Promedio de IMC de hombres por encima del peso normal
PrimeraMujer: str = "" # Nombre de la primera mujer la lista que su IMC dice que es obesa
CMObesas: int # Cantidad de Mujeres tienen el mismo tipo de obesidad que la Primera Mujer
NMenor: str = "" # Nombre del la persona de bajo peso con la menor talla
SMenor: str # Genero de la persona de bajo peso con la menor talla

# Variables de Proceso o Auxiliares
I: int # Variable contadora del ciclo
IMC: float # Indice de Masa Corporal
SIMCH: float # Sumatoria del IMC de los hombres por encima del peso normal
CIMCH: int # Cantidad de hombres por encima del peso normal
Band1: int # Bandera para la captura de Nombre de la primera mujer obesa en la lista
Tipo_Obesidad: int # Tipo de Obesidad de la Primera Mujer obesa en la lista
Menor: float # Menor Talla entre las persona de bajo peso
Band2: int # Bandera para la menor talla entre las personas de bajo peso

# Iniciación de variables
CMObesas = 0
SIMCH = 0
CIMCH = 0
Band1 = 0
Band2 = 0

# Lectura de la Lista y su Proceso
M = input("Cantidad de Personas en la Lista=")

for _ in range(M):

    Nombre = input("Nombre de la Persona=")
    Sexo = input("Sexo de la Persona (M=Masculino,F=Femenino)?=")
    Peso = input("Peso en Kg de la Persona=")
    Estatura = input("Estatura en m de la persona=")

    IMC = Peso / Estatura ** 2

    if Sexo.upper() == "F":  # Determinar la Interpretacion del IMC (depende del sexo)
        if IMC < 20:
            Interpretacion_IMC = 1 # Bajo Peso
        elif IMC < 25:
            Interpretacion_IMC = 2 # Peso Normal
        elif IMC < 30:
            Interpretacion_IMC = 3 # Obesidad Tipo 1
        elif IMC <= 40:
            Interpretacion_IMC = 4 # Obesidad Tipo 2
        else:
            Interpretacion_IMC = 5 # Obesidad Tipo 3

    else: # Es un hombre
        if IMC < 20:
            Interpretacion_IMC = 1
        elif IMC < 24:
            Interpretacion_IMC = 2
        elif IMC < 29:
            Interpretacion_IMC = 3
        elif IMC <= 37:
            Interpretacion_IMC = 4
        else:
            Interpretacion_IMC = 5

    if Interpretacion_IMC > 2: # Persona Obesa
        if Interpretacion_IMC == 3:
            print("Persona con Obesidad tipo 1")
        elif Interpretacion_IMC == 4:
            print("Persona con Obesidad tipo 2")
        elif Interpretacion_IMC == 5:
            print("Persona con Obesidad tipo 3")

        # Promedio de IMC de los hombre por Encima se su Peso Normal
        if Sexo.upper() == "M":
            SIMCH = SIMCH + IMC
            CIMCH = CIMCH + 1
        else: # Nombre y Genero de la Primera Mujer Obesa de la Lista
            if Band1 == 0:
                PrimeraMujer = Nombre
                Tipo_Obesidad = Interpretacion_IMC
                Band1 = 1
            else: # Mujeres obesas que comparten el mismo tipo de obesidad que la primera obesa de la lista
                if Interpretacion_IMC == Tipo_Obesidad:
                    CMObesas = CMObesas + 1

    if Interpretacion_IMC == 1:
        if Band2 == 0:
            Menor = Estatura
            NMenor = Nombre
            SMenor = Sexo
            Band2 = 1
        elif Estatura < Menor:
            Menor = Estatura
            NMenor = Nombre
            SMenor = Sexo

# ***********************************************
# *      Impresion de Resultados Totales       **
# ***********************************************
if CIMCH == 0:
    print("No hubo Hombres Obesos en la Lista")
else:
    Pro = SIMCH / CIMCH
    print("Promedio de IMC de los hombres por encima del Peso Normal=", Pro)

if Band1 == 0:
    print("No hubo mujeres obesas en la lista")
else:
    print("Primera Mujer Obesa de la Lista=", PrimeraMujer)
    print("Cantidad de mujeres con el mismo tipo de obesidad que la anterior=", CMObesas)

if Band2 == 0:
    print("No hubo personas de bajo peso en la lista")
else:
    print("Persona de bajo peso con la menor Talla=", NMenor)
    print("y cuyo sexo es=", SMenor)

input("Pulse una tecla")