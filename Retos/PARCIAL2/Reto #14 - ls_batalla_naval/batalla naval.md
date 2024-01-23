# Reto #14: Batalla Naval
#### Dificultad: Fácil | Publicación: 07/01/24 | Corrección: 07/01/24

## Enunciado

```
El último deseo de Timmy Turner fue jugar Batalla Naval con barcos de verdad, y sus padrinos magicos 
cumpliendos con su deber, se lo concedieron. Una vez iniciada la batalla Timmy comenzó a disparar 
misiles a diestra y siniestra contra la flota enemiga, pero debido a su poca inteligencia, Timmy no tomaba en
cuenta la cinematica del lanzamiento de proyectiles y a veces acertaba y otras veces no.
Esto obligo a Timmy a desear un ingeniero que lo ayudara con el problema; como resultado del deseo apareció usted.
El problema es el siguiente: el centro de control del barco de Timmy registra los siguientes datos sobre los barcos de la flota enemiga:

IDENTIFICACIÓN, DISTANCIA DE DICHO BARCO AL BARCO DE TIMMY (EXPRESADO EN METROS) Y VELOCIDAD INICIAL HORIZONTAL (V0X) DEL MISIL QUE TIMMY LANZÓ CONTRA ÉL (EXPRESADO EN M/S)

Usted debe desarrollar un programa que lea los datos registrados por el centro de control, en el archivo 
"LANZAMIENTOS.DAT" y usando la teoría del lanzamiento de proyectiles:

Procese la información y determine e imprima por pantalla:
  • De los barcos destruidos, la identificación del barco que estaba más cerca.
  • De los barcos que NO fueron destruidos, porcentaje de misiles que no alcanzaron al barco enemigo
expresado respecto al total de barcos No destruidos.
  • Porcentaje de barcos destruidos.
  • Velocidad inicial vertical (V0Y) promedio en m/s.

CONSIDERACIONES
  • Timmy disparó un misil por cada barco enemigo.
  • La velocidad inicial (V0) es un dato proporcionado por el manual del lanzamisiles, el cual 
especifica que la velocidad inicial del primer lanzamiento es de 250 m/s, y por cada nuevo 
lanzamiento disminuye 1%.
  • Los barcos se considerarán destruidos, si la diferencia entre distancia entre el barco de
Timmy y el barco a destruir almacenada en el archivo y el alcance determinado mediante la fórmula, 
es en valor absoluto menor a 10-5
o El misil puede caer antes del barco, en cuyo caso se considera que no alcanzó el barco, o puede 
caer después del barco en cuyo caso, se considera que sobrepasó el barco. En ambos casos el barco 
se considera NO DESTRUIDO
  • Formulas necesarias:
alvance=vox*tvuelo, tvuelo=2voy/g, vo=(vox+voy)**0.5
```
Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
