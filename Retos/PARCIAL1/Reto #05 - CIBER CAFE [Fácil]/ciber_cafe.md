# Reto #05: Ciber Café 
#### Dificultad: Fácil | Publicación: 07/01/24 | Corrección: 07/01/24

## Enunciado

```
Un cybercafé es un local público donde se ofrece a los clientes acceso a Internet y en algunos 
locales, servicio de cafetería. El cybercafé “Los Pobresores” necesita controlar las operaciones del
negocio, así que para lograr este objetivo se evaluaron en la recepción del local los siguientes 
datos de un grupo de N clientes:

  NOMBRE DEL CLIENTE, EDAD, HORA Y MINUTOS DE LLEGADA,
y de PODER hacer uso de los servicios del local se lee además,
EL TIEMPO DE CONEXIÓN EN MINUTOS Y SI PIDIÓ SERVICIO DE CAFETERÍA (“SI”/”NO”)

Se debe desarrollar un programa que procese los datos suministrados y determine
e imprima la siguiente información:

Por cada cliente:
  1) Indique si pudo entrar o no al cibercafé, en caso de entrar, indique a qué hora salió (en horas y
minutos), de no entrar indique por qué razón no pudo entrar, si por la edad o porque el cybercafé ya
cerró.
  2) Si el cliente puede hacer uso de los servicios, pero llegó antes de la hora de abrir el cybercafé, indique
cuantos minutos debe esperar para poder entrar y considere el cálculo para la hora de salida en el
punto anterior.

Para todos los clientes:
  3) Nombre y edad del cliente que llegó al cybercafé después de las 12:00 (720 min del día) y salió después
del cierre 17:00 (1020 min del día), con el mayor tiempo de conexión, de haber más de uno con la
misma condición, indique el último en procesar.
  4) Porcentaje de clientes que esperaron que abriera el cybercafé y pudieron hacer uso de nuestros
servicios con respecto a los clientes atendidos en el día.
  5) Cuantos clientes se procesaron antes de atender el primero que pidió servicio de cafetería y cuantos
pidieron ese servicio después de él.

CONSIDERACIONES:
  a) El cibercafé abre a las 8:00 (480 min del día) y cierra a las 17:00 (1020 min del día).
  b) Todo cliente que llega antes de abrir el local necesita hacer uso del local y espera que abra.
  c) Los clientes deben tener más de 17 años para poder entrar al cybercafé.
  d) Los clientes son procesados según la hora y minutos del día que van llegando, así que se atienden un
máximo de N clientes o hasta que aparezca el primer cliente que llegue después del cierre del
cybercafé.
  e) Las horas se manejan en formato de 24 horas.
```
Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.
