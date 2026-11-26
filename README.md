*Este proyecto ha sido creado como parte del currículo de 42 por ugarcia-, davcasti*

# A-Maze-ing

## Descripción

A-Maze-ing es un proyecto desarrollado en Python cuyo objetivo es generar, resolver y visualizar laberintos de forma automática a partir de un archivo de configuración.

El programa permite personalizar las dimensiones del laberinto, los puntos de entrada y salida, la semilla de generación y el tipo de laberinto.

Además, incorpora una interfaz interactiva que permite modificar la visualización, regenerar el laberinto y mostrar su solución.

## Funcionalidades

- Generación de laberintos mediante un algoritmo DFS.
- Generación de laberintos perfectos y no perfectos.
- Configuración mediante un archivo externo.
- Validación de parámetros y gestión de errores.
- Incorporación del patrón 42.
- Resolución del camino mediante un algoritmo BFS.
- Visualización interactiva del laberinto.
- Cambio de colores.
- Animación del proceso de generación.
- Animación del proceso de resolución.
- Exportación del laberinto en formato hexadecimal.
- Generador reutilizable como paquete Python (`mazegen`).

## Instrucciones

### Requisitos

- Python 3.10 o superior.
- pip.
- Make.

### Instalación

Crear el entorno virtual e instalar las dependencias:

`make install`

### Ejecución

Ejecutar el programa:

`make run`

### Depuración

Ejecutar el programa utilizando el depurador de Python:

`make debug`

### Comprobación del código

Ejecutar las comprobaciones de Flake8 y Mypy:

`make lint`

### Comprobación estricta

`make lint-strict`

### Limpieza

Eliminar archivos temporales y cachés generados durante el desarrollo:

`make clean`

## Algoritmos utilizados

### DFS (Depth-First Search)

Algoritmo de búsqueda en profundidad utilizado para generar el laberinto, recorriendo las celdas y eliminando las paredes correspondientes.

### BFS (Breadth-First Search)

Algoritmo de búsqueda en anchura utilizado para encontrar el camino más corto entre la entrada y la salida del laberinto.

## Distribución del trabajo

El proyecto se ha desarrollado de forma colaborativa, distribuyendo las diferentes responsabilidades entre los integrantes del equipo.

### ugarcia- — Unai Garcia

- Validación del archivo de configuración.
- Gestión de errores y excepciones.
- Desarrollo y revisión del patrón 42.
- Revisión de la generación y resolución del laberinto.
- Desarrollo de funcionalidades interactivas.
- Animaciones de generación y resolución.
- Preparación del sistema de empaquetado de `mazegen`.
- Configuración del Makefile.
- Pruebas y corrección de errores.

### davcasti — David Castillo

- Desarrollo de la generación de laberintos no perfectos.
- Reestructuración del código mediante clases.
- Organización de los componentes del generador.
- Adaptación del generador para su reutilización.
- Integración de funcionalidades.
- Pruebas y corrección de errores.

### Trabajo conjunto

- Diseño y organización de la arquitectura del proyecto.
- Integración de los diferentes componentes.
- Revisión del cumplimiento de los requisitos del subject.
- Pruebas de funcionamiento.
- Elaboración de la documentación.

## Librería mazegen

El proyecto incluye la preparación de una librería Python independiente que permitirá utilizar el generador de laberintos desde otros proyectos.

La librería podrá instalarse mediante pip sin necesidad de utilizar la aplicación completa.

La documentación de instalación, configuración y utilización del generador se completará una vez finalizada su implementación.

## Recursos

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Setuptools](https://setuptools.pypa.io/)
- [Flake8](https://flake8.pycqa.org/)
- [Mypy](https://mypy.readthedocs.io/)
- [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search)
- [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search)

## Estado del proyecto

Actualmente en desarrollo. Pendiente de finalizar la integración de las clases, el empaquetado definitivo del generador, las pruebas finales y la documentación.

## License

Copyright (C) 2026 Unai Garcia and David Castillo.

This project is licensed under the GNU General Public License v3.0 or later (GPL-3.0-or-later).

See [LICENSE.md](LICENSE.md) for more information.







