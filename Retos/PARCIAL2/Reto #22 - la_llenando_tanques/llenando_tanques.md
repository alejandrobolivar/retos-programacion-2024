# Reto #: 
#### Dificultad: Fácil | Publicación: 07/01/24 | Corrección: 07/01/24

## Enunciado

```
En un complejo residencial, un grupo de vecinos se ven en la necesidad de llenar sus tanques, en 
vista que hay serios problemas con el agua. Toda el agua disponible se encuentra almacenada en 
un tanque subterráneo del complejo, y para llenar el resto de los tanques basta con utilizar el agua 
disponible; pero, para mayor complicación el caudal de descarga no es lo suficientemente fuerte 
como para hacer el llenado utilizando una manguera y no disponen de una bomba hidráulica.
En vista de la situación y la gran necesidad de utilizar el agua, los vecinos toman la opción de 
llenar los tanques utilizando tobos.
En un archivo de datos de nombre “RESIDENCIAS.TXT” se encuentra almacenada la siguiente información:

En la primera línea,

VOLUMEN DE AGUA DISPONIBLE EN EL TANQUE SUBTERRÁNEO (m3), CAUDAL INICIAL DE DESCARGA (m3/s)

en las líneas siguientes, por cada tanque a llenar:

NÚMERO DE LA CASA A LA QUE PERTENECE EL TANQUE

y por cada tobo utilizado para llenar los tanques:

TIEMPO DE LLENADO DEL TOBO(S), ESTATUS (0 si no ha llenado el tanque, 1 si lo llena)

Procese la información del archivo “RESIDENCIAS.TXT” y genere dos archivos; “LLENOS.TXT”, donde 
se almacene el número de la casa donde su tanque se llenó completamente y cuantos tobos necesitó para lograrlo, y
“RESULTADOS.TXT” donde se imprima:

Para cada tobo:
  1. Volumen del tobo en L.

Por cada tanque que se logra llenar:
  2. Volumen del tanque en m3.
  3. Volumen disponible en el tanque subterráneo para llenar el resto de los tanques, expresado en m3.

Para todo el proceso de llenado:
  4. Número de la casa en la que el tanque se llenó parcialmente, pues no se llenó completamente por falta de
agua. Y ¿Cuántos tanques se llenaron completamente antes de intentar llenarlo?
Además imprima por consola:
  5. Tiempo promedio de llenado de los tanques que se pudieron llenar por completo en minutos.

Consideraciones:

   El caudal disminuye un 1% en cada llenado de un tobo y siempre se mantiene por lo menos por encima de cero
m3/s. Al finalizar el llenado de un tanque los vecinos descansan y el caudal para el llenado del siguiente tanque se
recupera, así que vuelve a ser el inicial.
   El volumen de un tobo se determina como: V = Q * t
V: Volumen del tobo (m3),
Q: Caudal (m3/s)
t: tiempo de llenado (s)
   1m3 es el equivalente a 1000 L.
   60 segundos es el equivalente a 1 minuto.
   El volumen de un tanque se determina como la suma de los volúmenes de todos los tobos utilizados para llenarlo.
   Cuando se acaba el agua disponible ya no se pueden llenar más tobos y por tanto no se llenan más tanques.
   Se llenan los tanques uno por uno. Una vez llenado un tanque se comienza a llenar otro.
```
Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
