# Curso de Programación - Trabajo final 2022

En este trabajo final se busca complementar todos los conocimientos adquiridos durante el curso. Para esta ocasión se proponen dos caminos:
- [Contribuir en la librería Faker](./tp_final.md#contribuir-en-la-librería-faker)
- [Proyecto individual](./tp_final.md#proyecto-propio)

## Contribuir en la librería Faker

Durante el [Lab3](../labs/lab3.md) estuvimos viendo librerías entre ellas, la librería Faker.

Faker es una librería o paquete de Python que genera datos falsos. Puede generar nombres de personas, apellidos, direcciones, códigos postales, nombres de ciudades, cualquier cosa en la que haya sido programada.

Faker está implementado para varios idiomas y regiones pero aún NO ha sido implementado para los datos de Argentina, por lo que este proyecto propone aportar al software libre y desarrollar la librería con los datos de Argentina.
Algunos datos con los que se puede colaborar son:
- Nombres de personas
- Nombre de calles
- Números de teléfonos
- Patente de vehículos

### Organizandonos

- Repositorio de trabajo [Fork de Faker](https://github.com/kity-linuxero/faker)
- Nuestro provider será `es_AR`.
- Se le brindará acceso sobre un branch para trabajar, por ejemplo... `feature/es_ar-address`.
- Una vez terminado, solicitar el merge al instructor.
- Se debe utilizar comentarios en inglés y poner comentarios de donde se puede sacar la info. Por ejemplo, los nombres de personas pueden ser obtenidos de [datos.gob.ar](), o el formato de patentes de autos de Argentina de este [link](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Argentina).
- **Observar el código ya implementado puede serle de mucha ayuda**: puede ayudarse de los providers, `es_MX`, `es_ES`, `es_CO` o `es_CL` para usar como referencia.
- Cada alumnx trabajará sobre un _provider_ (o más) y será su TP antes de realizar el merge.
- Luego una vez completado con la documentación, la idea es hacer un `pull-request` a los desarrolladores de la librería. Si aceptan el PR, el código estará en las próximas versiones de la librería.

### Normas de contribución para Faker

Siguiendo las [notas de contribución](https://github.com/kity-linuxero/faker/blob/master/CONTRIBUTING.rst) de Faker, se resumen en la siguiente lista:

- Crear un branch por cada tema que vamos a trabajar.
- Seguir el [estilo de código](https://github.com/kity-linuxero/faker/blob/master/docs/coding_style.rst)
    - No exceder las líneas de 120 caracteres.
    - Al usar listas largas, ordenarlas alfabéticamente y no exceder los 120 caracteres por línea.
    - Sugerencias de tipo:
        - [`typing.py`](https://github.com/kity-linuxero/faker/blob/master/faker/typing.py): incluye sugerencia de tipos [_Type Hints_](https://github.com/kity-linuxero/faker/blob/master/docs/coding_style.rst#type-hints)
- Revisar espacios en blanco innecesarios antes de realizar un commit.
- Realizar los test necesarios para revisar los cambios.
- Correr todos los test para verificar que nada se haya roto accidentalmente.

## Cómo trabajar con Faker.

### Clonar el repositorio _fork_

```
git clone https://github.com/kity-linuxero/faker.git
```

### Verificar si hay alguna versión de Faker instalada previamente

```pip list```

Si existe una versión instalada, desinstalar con:

```pip uninstall faker```

### Lugar de trabajo

Una vez clonado el repositorio, la estructura de carpetas será:

`faker/faker/providers`

Nos centraremos en trabajar sobre:

`faker/faker/providers/xxxx/es_AR/__init__.py`

- (Opcional) Crearemos un archivo `my_program.py` sobre `faker/` para ir realizando las pruebas. Ese archivo NO DEBE SER agregado al commit. Y se usará solo como prueba.

### Ejemplo:

Supongamos que vamos a trabajar sobre las patentes de vehículos de Argentina.

Una vez clonado el repo de `faker`. Vamos a crear la el archivo: `faker/faker/providers/automotive/es_AR/__init__.py` con el siguiente contenido:

```python
import re

from string import ascii_uppercase

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):

    """Implement automotive provider for ``es_AR`` locale.

    Sources:

    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Argentina

    """


    license_formats: ElementsType = (
                                    'AAA123',
                                    'BBB123',
                                    'ETK256',
                                    'HYN908',
                                    'NAT840',
                                    )

    def license_plate(self) -> str:
        """Generate a license plate."""
        temp = re.sub(
            r"\?",
            lambda x: self.random_element(ascii_uppercase),
            self.random_element(self.license_formats),
        )
        return self.numerify(temp)

```

`faker/my_program.py`:
```python
from faker import Faker
fake = Faker('es_AR')


for a in range(5):
    print(fake.license_plate())
```

### Output

```bash
BBB123
BBB123
NAT800
BBB123
AAA123
```

O bien puede ver como están implementados otros providers, como por ejemplo [automotive/es_CL](https://github.com/kity-linuxero/faker/blob/master/faker/providers/automotive/es_CL/__init__.py).

## Links útiles para trabajar contribuyendo a Faker

A continuación tiene una lista de links útiles:

- [Documentación](https://faker.readthedocs.io/en/master/index.html)
- [Repositorio Github](https://github.com/joke2k/faker)
- [Referencia Español - México](https://faker.readthedocs.io/en/master/locales/es_MX.html)
- [Referencia Español - Chile](https://faker.readthedocs.io/en/master/locales/es_CL.html)
- [Referencia Español - Colombia](https://faker.readthedocs.io/en/master/locales/es_CO.html)
- [Referencia Español - España](https://faker.readthedocs.io/en/master/locales/es_ES.html)
- [Providers](https://github.com/joke2k/faker/tree/master/faker/providers)
    - [Direcciones](https://github.com/joke2k/faker/tree/master/faker/providers/address)
    - [Patentes de vehículos](https://github.com/joke2k/faker/tree/master/faker/providers/automotive)
    - [Colores](https://github.com/joke2k/faker/blob/master/faker/providers/color/__init__.py)
    - [Nombres y apellidos](https://github.com/joke2k/faker/blob/master/faker/providers/person/__init__.py)
    - [Números de teléfonos](https://github.com/joke2k/faker/tree/master/faker/providers/phone_number)
    - [Oficios / trabajos](https://github.com/joke2k/faker/blob/master/faker/providers/job/__init__.py)
- [Funciones `lambda` en Python](https://ellibrodepython.com/lambda-python)

## Proyecto propio

Si usted tiene un proyecto en mente o está a mitad de un desarrollo propio, puede presentarlo como trabajo final para tener la tutoría del instructor y servirá para aprobación del presente curso. Como requisitos se pedirá:

- Presentar la idea al instructor
- Tener un repositorio Git con acceso al instructor para su seguimiento. Usar las recomendaciones sobre los repositorios git; utilizar los branchs necesarios.
- En el repositorio, debe haber un archivo llamado _README.md_ con la descripción del programa y como hacerlo funcionar. Utilice la sintaxis [Markdown](https://markdown.es/sintaxis-markdown/) para organizar la documentación y el readme.
- Realizar tests de unidad
- Realizar manejo de excepciones de manera de hacer robusto su programa
- Realizar al menos una breve documentación del programa
- No es necesario que tenga una interfaz gráfica de usuario. Pero si es la idea a futuro, definir bien los módulos, funciones y/o métodos para integrarlo luego.
- Piense un proyecto simple y realizable en base al tiempo disponible y a las exigencias del TP.

`Let's code!`