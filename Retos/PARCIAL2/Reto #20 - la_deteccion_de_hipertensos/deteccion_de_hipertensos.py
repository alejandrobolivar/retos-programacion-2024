'''
Los estudiantes de la Facultad de Ciencias de la Salud inician una jornada de
despistaje de hipertensión arterial, registrando durante días consecutivos la
presión de un conjunto de personas. Para el procesamiento de la información
le solicitarán apoyo a la Facultad de Ingeniería a la cual le hacen entrega del
archivo de datos “Tensiones.txt” con la siguiente estructura:
Para cada persona se registra:
NOMBRE, GÉNERO, EDAD Y CANTIDAD DE MEDICIONES
Y para cada una de las mediciones de la persona:
FECHA (DÍA/MES), PRESIÓN SISTÓLICA y PRESIÓN DIASTÓLICA expresadas en MMHG (milímetros de mercurio).
Se le pide a ud. que desarrolle una aplicación de consola VB2010 que procese el archivo “Tensiones.txt” y
genere el archivo de dato “resultados.txt” el cual debe contener por cada paciente NOMBRE, EDAD y un
mensaje que indique si está sano o es hipertenso, adicionalmente se requiere que determine y muestre las
siguientes estadísticas en pantalla:
Por cada Paciente:
1. Porcentaje de mediciones consideradas como Tensión Alta.
2. Fecha, presión sistólica y diastólica en donde el paciente registro menor diferencia entre las dos
presiones.
Para todos los Pacientes:
3. Nombre y Edad del primer paciente con todas las mediciones de tensión normal.
4. Género (Masculino o Femenino) que tiene más pacientes hipertensos.
CONSIDERACIONES:
1. Se considera una Tensión Alta: si la Presión Sistólica está por encima de 139 mmHg o la Presión
Diastólica está por encima de 89 mmHg.
2. Un paciente es hipertenso si al menos la mitad de las mediciones registradas se consideran como
tensión alta.
'''
from math import abs
# Zona 1:
# Entradas
Nombre: str
Genero: str
Edad: int
Cant_Mediciones: int
Fecha: str
PresionS: int
PresionD: int

# Salidas
Porc_Tension_Alta: float
Fecha_Menor: str
PresionS_Menor:int
PresionD_Menor: int
Nomb_Primero: str
Edad_Primero: int
Gen_Mayor_Cant_Hipertensos:str

# Procesos
Cant_Mediciones_Altas: int
band_menor:bool
Diferencia:int
Dif_Menor: int
band_primero:bool
Cant_Masculino_Hipertensos: int
Cant_Femenino_Hipertensos: int

# Manejo de Archivos
arch1 = open("tensiones.txt", 'r')
arch2 = open("resultados.txt", 'w')

# Inicializaciones (TODOS LOS PACIENTES)
band_primero = True
Cant_Masculino_Hipertensos = 0
Cant_Femenino_Hipertensos = 0

# Ciclo Externo (CADA PACIENTE)
registro = arch1.readlines()
linea = 0

while linea < len(registro):
    # Zona 2:
    lista_ext = registro[linea].split(',')
    linea += 1

    # Lectura de datos de cada paciente
    Nombre = lista_ext[0]
    Genero = lista_ext[1]
    Edad = int(lista_ext[2])
    Cant_Mediciones = int(lista_ext[3])

    # Inicializaciones (CADA PACIENTE)
    Cant_Mediciones_Altas = 0
    band_menor = True

    # Ciclo Interno (CADA MEDICIÓN)
    for _ in range(Cant_Mediciones):
        # Zona 3:
        # Lectura de datos de cada medición
        lista_int = registro[linea].split(',')
        linea += 1
        Fecha = lista_int[0]
        PresionS = int(lista_int[1])
        PresionD = int(lista_int[2])

        # Determinar si una medición es considerada como tensión alta
        if PresionS > 139 or PresionD > 89:
            Cant_Mediciones_Altas += 1

        # Cálculo de la menor dif. entre presiones
        Diferencia = abs(PresionS - PresionD)

        if band_menor:
            Fecha_Menor = Fecha
            PresionS_Menor = PresionS
            PresionD_Menor = PresionD
            Dif_Menor = Diferencia
            band_menor = False
        elif Diferencia < Dif_Menor:
            Fecha_Menor = Fecha
            PresionS_Menor = PresionS
            PresionD_Menor = PresionD
            Dif_Menor = Diferencia

    # Zona 4:
    # Imprimir datos en el archivo
    if (2 * Cant_Mediciones_Altas) >= Cant_Mediciones: # Paciente Hipertenso
        arch2.write(Nombre, Edad, "Hipertenso")

        # Cálculo del género con más pacientes hipertensos
        if Genero == "F" or Genero == "f":
            Cant_Femenino_Hipertensos += 1
        elif Genero == "M" or Genero == "m":
            Cant_Masculino_Hipertensos += 1

    else: # Paciente sano
        arch2.write(Nombre, Edad, "Sano", '\n')

    # Cálculo e impresión del porcentaje de mediciones consideradas como tensión alta
    Porc_Tension_Alta = (Cant_Mediciones_Altas / Cant_Mediciones) * 100

    print(f"Paciente:{Nombre}, Porc. Med. Altas: {Porc_Tension_Alta:.2f}%")

    # Primer paciente con todas las med. consideradas tensión normal
    if Cant_Mediciones_Altas == 0 and band_primero:
        Nomb_Primero = Nombre
        Edad_Primero = Edad
        band_primero = False

    # Imprimir datos del registro con menor diferencia entre las 2 presiones
    print("Nombre del Paciente: ", Nombre)
    print(f"Registro con menor dif: Fecha:{Fecha_Menor}, PS:{PresionS_Menor}, PD:{PresionD_Menor}")

# Zona 5:
# Imprimir Primer paciente con todas las med. consideradas tensión normal
if not band_primero:
    print("Primer paciente con todas las med. de tensión normales: Nombre:{0}, Edad:{1}", Nomb_Primero, Edad_Primero)
else:
    print("Ningun paciente con med. de tensión normales")

# Imprimir el género con mayor cantidad de pacientes hipertensos
if Cant_Masculino_Hipertensos > Cant_Femenino_Hipertensos:
    Gen_Mayor_Cant_Hipertensos = "Masculino"
    print("El género con mayor cantidad de pacientes hipertensos es: ", Gen_Mayor_Cant_Hipertensos)
elif Cant_Femenino_Hipertensos > Cant_Masculino_Hipertensos:
    Gen_Mayor_Cant_Hipertensos = "Femenino"
    print("El género con mayor cantidad de pacientes hipertensos es: ", Gen_Mayor_Cant_Hipertensos)
else:
    print("Ambos géneros tiene igual cantidad de pacientes hipertensos")

# Cierre de Archivos
arch1.close()
arch2.close()