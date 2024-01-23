# Reto #: 
#### Dificultad: Fácil | Publicación: 07/01/24 | Corrección: 07/01/24

## Enunciado

```
Su profesor de física le propuso un tema de investigación de campo que consiste en estudiar y 
simular las trayectorias de los batazos de los jugadores de beisbol. La idea fundamental es crear 
un programa que lea de un archivo de datos de nombre stadium.txt , el cual contiene la 
información del stadium y los batazos registrados en ese stadium. La información del archivo tiene 
la siguiente estructura, en la primera línea la información del stadium:

Distancia del Home al Muro por el Center Field o Largo del Campo (m) y la altura del Muro (m) y a 
continuación los datos de los batazos que se han registrado en ese stadium, que consiste en:

  Nombre del Bateador, Altura del Bateo (m), Velocidad de Salida (m/s) y ángulo de salida (expresado en grados)

Desarrolle un programa que lea la información del archivo stadium.txt y genere un archivos de nombre 
"jonrones.txt" el cual debe contener los nombres de los bateadores que batearon jonrón y otro de 
nombre "otros.txt" que debe contener los nombres de los bateadores que conectan batazos que no son 
jonrón. Además imprima por pantalla las siguientes estadísticas:
  1. Porcentaje de Batazos de cada tipo(Ver consideraciones)
  2. Nombre del Bateador, Velocidad y ángulo de salida del jonrón más largo

CONSIDERACIONES:
  a) Distancia Horizontal máxima de alcance (m), se calcula según la siguiente
fórmula:
Xmax = (Velocidad) ** 2 * sin(2 * Angulo) / 9.81
  b) Altura del Batazo (m), se calcula según la siguiente la fórmula:
Y = AlturaBateo + Largo * tan(Angulo) - 9.81 * (Largo) ** 2 / (2 * (Velocidad) ** 2 * (cos(Angulo)) ** 2)
  c) Los tipos de Batazo son:
    Tipo de Batazo; Condición
    Dentro del Cuadro; Xmax <= 36.88
    En los Outfielders; (36.88 < Xmax < Largo del Campo) ó (Xmax > Largo Campo y Altura del Batazo <= Altura del Muro)
    Jonrón; Xmax > Largo Campo y Altura del Batazo > Altura del Muro
    PI radian = 180°
  d) g=9.81 m/s (aceleración de la gravedad terrestre)
```
Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
