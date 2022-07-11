# Racedrivers

## About libracingd.py

Los pilotos son catalogados del 1 al 100 en base a su puntaje, experiencia y el mismo vehiculo que conduzcan.

La manera de catalogarlos es utilizando el rating global del piloto (Global Driver Rating o GDR/RGP)

### Como se asigna el rating del piloto

#### **Usando el puntaje**

Supongamos que el piloto de pruebas "Stig" ha conseguido entrar en los puntos en las ultimas 3 carreras, en la primera consiguio llegar en decimo puesto, lo que le da 1 punto, en la segunda termino noveno ganando 2 puntos y en la carrera 3 termino en un tercer puesto que le valieron 15 puntos mas, ganando en total 18 puntos

Por cada 10 puntos que obtenga el piloto, se le sumara 1 punto a su rating global, Esto se puede apreciar de mejor manera en la siguiente tabla:

| Posición  | Puntaje | Suma al GDR |
|-----------|---------|-------------|
|   1ro     |   25pts |     2,5r    |
|   2do     |   18pts |     1,8r    |
|   3ro     |   15pts |     1,5r    |
|   4to     |   12pts |     1,2r    |
|   5to     |   10pts |     1r      |
|   6to     |   8pts  |     0,8r    |
|   7mo     |   6pts  |     0,6r    |
|   8vo     |   4pts  |     0,4r    |
|   9no     |   2pts  |     0,2r    |
|   10mo    |   1pts  |     0,1r    |

Adicionalmente, todo aquel piloto que se encuentre fuera de los puntos seguira ganando puntos de rating hasta llegar al puesto 15 (3er cuarto de la parrilla), una vez superado el 75% de esta, se comenzaran a restar puntos

| Posición  |   Suma al GDR |
|-----------|---------------|
|   11vo    |     0,08r     |
|   12vo    |     0,06r     |
|   13vo    |     0,04r     |
|   14to    |     0,02r     |
|   15to    |     0,01r     |
|   16to    |     -0,05r    |
|   17mo    |     -0,10r    |
|   18vo    |     -0,15r    |
|   19no    |     -0,20r    |
|   20mo    |     -0,25r    |

#### **La Experiencia**

Esta es mucho mas simple: por cada largada del piloto, se le asignara 1 punto de experiencia, mientras tanto, por cada carrera en la que no compita, perdera un punto de experiencia

Para asignar puntos al GDR, se utiliza la siguiente tabla:


| Largadas |   Suma al GDR |
|----------|---------------|
|     4    |      1r       |
|     3    |     0,75r     |
|     2    |     0,50r     |
|     1    |     0,25r     |

#### **El Coche**

Para asignar los puntos correspondientes al coche, se debe obtener el rating del vehiculo, dividirlo entre 10, redondearlo y ese numero sera puesto en la ecuacion de rendimiento.

Para mas información consultar la guia acerca de los vehiculos.

## ¿Como afecta al rendimiento?

Todos estos parametros son colocados en la formula de rendimiento que se explica a continuación:

### Formula:

**Ejemplo:** Piloto con 50 puntos en el campeonato, ha competido en 5 Grandes Premios y su vehiculo tiene un rating de 67

**Paso 1: Obtener los puntos GDR correspondiente a su puntaje en carrera**

En primer lugar, se tiene constancia de que el piloto ha obtenido 50 puntos, que quiere decir que tiene 5 puntos GDR.

**Paso 2: Obtener los puntos GDR correspondientes a su experiencia**

Al saber que el piloto ha largado en 5 carreras y que no se ha perdido ninguna, se sabe que tiene 1,25 puntos GDR

**Paso 3: Obtener los puntos GDR correspondientes a su Vehiculo**

El vehiculo tiene un rating de 67, que al redondearlo da 70, que al dividirlo entre 10 da 7 puntos, siendo este el puntaje GDR correspondiente.

**Paso Final: Sumar**

El puntaje base siempre va a ser de 1, todos los resultados anteriores se sumaran y daran como resultado el puntaje final, siendo en este caso 5 + 1,25 + 7 = 13,25, que al ser redondeado, se obtiene el numero 13, el rating GDR final.