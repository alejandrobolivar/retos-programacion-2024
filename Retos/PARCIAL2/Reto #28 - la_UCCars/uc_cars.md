# Reto #28: UC Cars 
#### Dificultad: Fácil | Publicación: 07/01/24 | Corrección: 07/01/24

## Enunciado

```
Una compañía ensambladora de automóviles está realizando pruebas de eficiencia a los diferentes 
modelos de autos que ensambla. Estas pruebas consisten en subir el auto a velocidad constante por 
varias colinas con diferentes ángulos de elevación (alfa).
Los resultados de dichas pruebas se utilizan para calcular el porcentaje de eficiencia del auto, de 
acuerdo a la siguiente expresión:

Eficiencia[%] = consumo teórico de gasolina [L] * 100 / consumo real de gasolina [L]

Para ello, la compañía ensambladora registra en un archivo de datos de nombre pruebas.dat, la siguiente
información del auto:

  Modelo, Masa del auto (kg), Eficiencia mínima aceptable (%), Número de pruebas

Y para cada auto se registra la información de las pruebas realizadas:

  Angulo de la colina (grados), Distancia recorrida (m), Consumo real de gasolina en el recorrido (L)

En vista de su altísimo rendimiento en la materia Computación I, usted fue seleccionado para que 
desarrolle un programa que lea la información del archivo de datos "pruebas.dat" y determine e
imprima en un archivo de datos de nombre "aprobados.dat", los siguientes datos de los modelos que pasan
la prueba de subir colinas:

  Modelo, Eficiencia mínima aceptable (%), Eficiencia promedio obtenida (%)

Además se pide que imprima por pantalla lo siguiente:
  • Modelo del auto y ángulo de elevación de la prueba con menor eficiencia.
  • Porcentaje de autos que pasaron la prueba.

CONSIDERACIONES:
  • Un auto pasa las pruebas de subir colinas si el promedio de las eficiencias obtenidas en las pruebas es mayor a la
eficiencia mínima aceptable del auto.
 consumo teórico de gasolina [L] = Trabajo para subir el automóvil [Joule] / Calor de combustión de la gasolina[Joule/L]
  • 180° = pi rad
  • La función interna de pascal que calcula el seno se escribe sin(x), donde x es el valor o la expresión del que
desean obtener el valor del seno, debe estar en radianes.
```
Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
