# Laboratorio 2
En este laboratorio usted aprenderá a:
- Manejar fechas y formato hora/tiempo en Python
- Crear _objetos_ con formato fecha `datetime`
- Comparar y calcular diferencia entre fechas y/o tiempo.

## Fechas y unidades de tiempo.

Por razones obvias, sabemos que es útil trabajar con fechas, horas y unidades de tiempo para registrar eventos. Todo acontece en un momento determinado que puede ser necesario tener un registro de cuando pasó.
En Python hay un modulo que se puede importar llamado `datetime` que nos permite manipular _objetos_ de formato tiempo/hora. Otros lenguajes pueden tener módulos similares que se importan o contener manejo de tiempo o fechas de forma nativa. Pero lo que importa saber es que los lenguajes modernos proveen alguna forma que podamos trabajar con fechas y unidades de tiempo.

[Documentación datetime](https://docs.python.org/es/3/library/datetime.html?highlight=datetime#)

## Usando fechas en Python

Si quisiéramos tener una variable que contenga la hora actual, en Python podemos obtenerla de la siguiente forma:
```python
from datetime import datetime

ahora = datetime.now()
print(ahora)
```

Lo que nos dará como resultado la siguiente salida:
```bash
2022-08-01 20:05:21.901967
```
En la variable `ahora` tendremos la información de la fecha y hora que obtuvimos en un momento determinado. Es importante saber que esa fecha/hora no es dinámica y corresponde al momento justo que se ejecutó esa instrucción. Es decir, `ahora` no tendrá siempre la fecha actual. Si queremos obtener otra vez la fecha y hora actual tendremos que volver a invocar `datetime.now()`.

También podemos definir manualmente una fecha determinada

```python
from datetime import datetime

fecha = datetime(1986, 12, 24)
print(fecha)
```

```bash
1986-12-24 00:00:00
```

Por defecto, la hora será las `00:00:00`.

También es posible acceder a los elementos de un `datetime` como su día, mes, año.

``` python
from datetime import datetime

fecha = datetime(1986, 12, 24)
print("Día:", fecha.day)
print("Mes:", fecha.month)
print("Año:", fecha.year)
```

```bash
Día: 24
Mes: 12
Año: 1986
```

También es posible especificar la hora del día:

```python
from datetime import datetime

fe1 = datetime(2021, 6, 30, 13)     # 30/06/2021 a las 13 hs
fe2 = datetime(2021, 6, 30, 18, 45) # 30/06/2021 a las 18:45 hs
```

## Comparar y calcular diferencia entre intervalos de tiempo

Es posible comparar fechas y rango de tiempos. Vea el siguiente ejemplo del programa que dice si el curso de programación ha finalizado o no.

```python
from datetime import datetime

hoy = datetime.now()
fin_curso = datetime(2022, 12, 16)

if hoy < fin_curso:
    print("El curso de programación aún no ha finalizado")
elif hoy == fin_curso:
    print("¡Hoy finaliza el curso de programación!")
elif hoy > fin_curso:
    print("El curso de programación ha finalizado")
```
Si corremos este programa hoy, el resultado será:
```bash
El curso de programación aún no ha finalizado
```

La diferencia entre dos rangos de tiempo se puede obtener simplemente restando las fechas.

```python
from datetime import datetime

hoy = datetime.now()
fin_curso = datetime(2022, 12, 16)

diferencia = (fin_curso - hoy).days # Para quedarme solo con los días

if hoy < fin_curso:
    print(f"Faltan {diferencia} días para finalizar el curso.")
elif hoy == fin_curso:
    print("¡Hoy finaliza el curso de programación!")
elif hoy > fin_curso:
    print(f"El curso de programación ha finalizado hace {abs(diferencia)}")
    # Se utiliza abs (valor absoluto) porque de lo contrario indicaría días negativos
```

Al realizar la resta entre dos fechas, el _objeto_ resultante será un `deltatime` y no un `datetime`.
[Documentación deltatime](https://docs.python.org/es/3/library/datetime.html?highlight=datetime#timedelta-objects)

## Formato de fecha y hora

Tal vez haya notado que el formato por defecto de la fecha y hora mostrado en los ejemplos anteriores no se usan en nuestra zona. Afortunadamente, el módulo `datetime` incorpora el método `strftime()` para formatear la fecha y hora para poder adaptarlo a nuestros programas.

```python
from datetime import datetime

fecha = datetime.now()
print(fecha.strftime("%d.%m.%Y"))
print(fecha.strftime("%d/%m/%Y %H:%M"))
```

```bash
19.10.2021
19/10/2021 09:31
```

El formato de fecha/hora utiliza caracteres específicos para indicar formatos. La siguiente es una lista de alguno de ellos:

| Notacion | Significado                  |
|----------|------------------------------|
| `%d`     | Día (01-31)                  |
| `%m`     | Mes (01-12)                  |
| `%y`     | Año en formato de 2 dígitos  |
| `%Y`     | Año en formato de 4 dígitos  |
| `%H`     | Horas en formato de 24 horas |
| `%M`     | Minutos (00-59)              |
| `%S`     | Segundos (00-59)             |

[Documentación strftime](https://docs.python.org/es/3/library/time.html#time.strftime)

El formato en `datetime` funciona de forma inversa de manera que puede formatear desde un string hacia una fecha. Vea el siguiente ejemplo:

```python
from datetime import datetime

cumple = input("Por favor ingrese su fecha de nacimiento en formato dd.mm.yyyy: ")
fecha = datetime.strptime(cumple, "%d.%m.%Y")

if fecha < datetime(2000, 1, 1):
    print("Naciste en el milenio anterior.")
else:
    print("Naciste en este milenio.")
```


```bash
Por favor ingrese su fecha de nacimiento en formato dd.mm.yyyy: 12.12.2001
Naciste en este milenio.
```



# Ejercicios


## Calculadora de edad

Escriba un programa que pregunte al usuario su fecha de nacimiento y calcule la edad. 

**Easter egg:** Si el día del cumpleaños coincide con el día en que está corriendo el programa debe saludarlo con un felíz cumpleaños. Puede usar algo creativo de [ASCII Art](https://www.asciiart.eu/holiday-and-events/birthdays)

## Registro de horas de pantalla

Escriba un programa para registrar la cantidad de tiempo que un usuario ha pasado frente a una pantalla durante un período de tiempo específico y guarde la data en un archivo llamado `registro-dia-mes-año.txt`.
El día, mes y año del nombre del archivo debe corresponder a la fecha inicial.

```bash
Fecha inicial (formato dd.mm.yyyy): 21.12.2021 
Cantidad de días: 5

Ingrese la cantidad de minutos que ha estado frente a la pantalla para cada día.

Tiempo para el día 21.12.2021: 54
Tiempo para el día 22.12.2021: 60
Tiempo para el día 23.12.2021: 0
Tiempo para el día 24.12.2021: 182
Tiempo para el día 25.12.2021: 45

Se ha almacenado la información en el archivo registro-21-12-2021.txt
```

El archivo `registro-21-12-2021.txt` debe contener la siguiente información:

```
Período: 21.12.2021 al 25.12.2021
Total de minutos: 341
Promedio en minutos: 68,2 minutos por día
-- Detalle:
21.12.2021: 54
22.12.2021: 60
23.12.2021: 0
24.12.2021: 182
25.12.2021: 45
```

## Reloj en español

Implemente un reloj en español en base a una hora enviada por el usuario. Si el usuario no manda ningún horario, debe tomar la hora actual. Por ejemplo:

| Hora | Expresion español      |
|------|------------------------|
| 6:00 | las seis               |
| 6:05 | las seis y cinco       |
| 6:15 | las seis y cuarto      |
| 6:20 | las seis y veinte      |
| 6:30 | las seis y media       |
| 6:40 | las siete menos veinte |
| 6:45 | las siete menos cuarto |
| 6:50 | las siete menos diez   |


### Ejemplo de ejecución

```bash
Ingrese una hora: 21:05
Son las nueve y cinco.
--
Ingrese una hora: 1:30
Es la una y media
--
Ingrese una hora: 1:45
Son las dos menos cuarto
--
Ingrese una hora: 1:00
Es la una
```

Ref:
- [Hora en español](https://espanol.lingolia.com/es/vocabulario/numeros-fechas-horas/horas)
- [Ejemplos de hora](https://www.quia.com/jg/12243list.html)