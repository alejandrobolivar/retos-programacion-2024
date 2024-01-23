# Reto #26: Tanques 
#### Dificultad: Fácil | Publicación: 07/01/24 | Corrección: 07/01/24

## Enunciado

```
Una empresa fabricadora de tanques de agua para el consumo humano, ha decidido automatizar el 
control de ventas de sus productos, en sus tres presentaciones especiales que tienen forma: cilíndrica, 
esférica y de cubo; todo esto motivado por la necesidad de los clientes, en cuánto a la selección de 
la forma y tamaño del tanque requerido para la vivienda. Para ello la empresa dispone de un listado 
de clientes en un archivo de nombre “tanques.txt” con la siguiente información de los pedidos:

Por cada cliente se conoce:

  El nombre del cliente y la cantidad de tanques requeridos.

Y para cada uno de los tanques se conoce:
  La forma (1: cilíndrica, 2: esférica, 3 cubo), las dimensiones (m) dependiendo de la forma, y el color.

Desarrolle un programa que procese la información anterior y determine e imprima por consola:

Para cada tanque:
  1. Volumen del tanque (m3).
  2. Costo del tanque en Bs.

Para cada cliente:
  3. Cantidad de tanques de más de 100 litros solicitados.
  4. Promedio del volumen (litros) en tanques cilíndricos.

Para todos los pedidos:
  5. Nombre del cliente que realizó la mayor compra, en caso de haber más de uno con el mismo 
monto indique cuántos.

Consideraciones:

  • Las dimensiones básicas en metros, según la forma son: para el cilíndrico, el radio y la altura; 
para el esférico, el radio; y para el cubo, un lado.
  • El tanque cilíndrico cuesta 100 Bs/m3, el esférico 150 Bs/m3 y el cubo 50 Bs/m3.
  • 1 m3 = 1000 litros.
  • El volumen de una forma esférica es Vesfera = (4/3) π r3, para una forma cilíndrica es 
Vcilindro = π r2 h y para una forma de cubo Vcubo = l3
  • El valor de  se obtiene mediante la función math.pi.
  • Ejemplo del archivo de dato “tanques.txt”.
```
Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
