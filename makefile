# ============================================================
# MAKEFILE - A-MAZE-ING
# ============================================================
# Automatiza tareas habituales del proyecto.
#
# Uso: make nombre_regla
# Ejemplo: make install, make run, make lint
#
# Make ejecuta los comandos de cada regla en orden.
# IMPORTANTE: los comandos deben comenzar con un TAB.
# ============================================================


# Python que utilizaremos para crear el entorno virtual.
PYTHON = python3
# Nombre de la carpeta donde se guardará el entorno virtual.
# Permite instalar librerías sin afectar al Python global.
VENV = venv
PIP = $(VENV)/bin/pip
RUN = $(VENV)/bin/python
MAIN = src/main.py

# ------------------------------------------------------------
# .PHONY
# ------------------------------------------------------------
# Indica que estos nombres son comandos, no archivos.
# Así Make los ejecuta aunque exista un archivo con ese nombre.
.PHONY: install run debug clean lint lint-strict #test
# test se activará cuando creemos las pruebas.

# ------------------------------------------------------------
# INSTALL - Instalar las dependencias
# ------------------------------------------------------------
# Uso: make install
#
# Primero crea el entorno virtual si todavía no existe.
# Después instala las dependencias de requirements.txt.
#
# Ejemplo:
# requirements.txt contiene flake8, mypy, pytest y black.
#
# No hace falta ejecutar make setup por separado.
install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt

# ------------------------------------------------------------
# RUN - Ejecutar el programa
# ------------------------------------------------------------
# Uso: make run
#
# Ejecuta main.py con el Python del entorno virtual.
# Cambiar la ruta si el archivo principal está en otro lugar.
run:
	$(RUN) $(MAIN)

# ------------------------------------------------------------
# DEBUG - Ejecutar el programa con el depurador
# ------------------------------------------------------------
# Uso: make debug
#
# pdb es el depurador integrado de Python.
# No necesita instalarse mediante pip.
#
# Permite detener la ejecución, avanzar paso a paso,
# entrar en funciones y consultar los valores de variables.
#
# Comandos principales dentro de pdb:
#
# n          -> Next: ejecuta la siguiente línea sin entrar
#               dentro de las funciones que se llamen.
#
# s          -> Step: avanza y puede entrar dentro de una función.
#
# c          -> Continue: continúa hasta el siguiente breakpoint
#               o hasta que termine el programa.
#
# p variable -> Print: muestra el valor de una variable.
#               Ejemplo: p width
#
# l          -> List: muestra el código alrededor de la línea.
#
# b 20       -> Breakpoint: establece una parada en la línea 20.
#
# q          -> Quit: sale del depurador.
#
# Ejemplo:
# make debug
# (Pdb) n
# (Pdb) p width
# (Pdb) c
debug:
	$(RUN) -m pdb $(MAIN)

# ------------------------------------------------------------
# LINT - Comprobar estilo y tipos (OBLIGATORIO EN EL SUBJECT)
# ------------------------------------------------------------
# Uso: make lint
#
# flake8:
#   Comprueba el estilo del código y detecta ciertos errores.
#   El punto "." indica que revisa el proyecto actual.
#
# mypy:
#   Comprueba los tipos de datos de nuestro código.
#
# Opciones de mypy exigidas por el subject:
#
# --warn-return-any:
#   Avisa si una función devuelve Any cuando espera otro tipo.
#
# --warn-unused-ignores:
#   Avisa si hemos puesto un # type: ignore innecesario.
#
# --ignore-missing-imports:
#   No da error por imports sin información de tipos.
#
# --disallow-untyped-defs:
#   Exige anotaciones de tipos en las funciones.
#
# --check-untyped-defs:
#   Comprueba el cuerpo de funciones sin tipos completos.
#
# Si flake8 falla, Make se detiene antes de ejecutar mypy.
lint:
	$(VENV)/bin/flake8 .
	$(VENV)/bin/mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

# ------------------------------------------------------------
# LINT-STRICT - Comprobación más exigente (OPCIONAL)
# ------------------------------------------------------------
# Uso: make lint-strict
#
# Ejecuta flake8 y mypy con --strict.
# --strict activa comprobaciones adicionales de tipos.
#
# Es más exigente que el lint obligatorio.
lint-strict:
	$(VENV)/bin/flake8 .
	$(VENV)/bin/mypy . --strict

# ------------------------------------------------------------
# CLEAN - Eliminar archivos temporales
# ------------------------------------------------------------
# Uso: make clean
#
# Elimina archivos temporales generados por Python y las pruebas.
# No elimina el código fuente ni el entorno virtual venv.
#
# Archivos que elimina:
# __pycache__: carpetas con bytecode almacenado por Python.
# .pytest_cache: caché generada por pytest.
# .mypy_cache: caché generada por mypy.
# *.pyc: archivos de bytecode compilado de Python.
#
# Explicación de los comandos:
#
# find .        -> Busca desde la carpeta actual y sus subcarpetas.
# -path         -> Comprueba si una ruta coincide con la indicada.
# './venv'      -> Ruta del entorno virtual que queremos excluir.
# './.git'      -> Carpeta de Git que también queremos excluir.
# \( ... \)     -> Agrupa las condiciones de exclusión.
# -prune        -> Evita entrar en una carpeta durante la búsqueda.
# -o            -> OR (o lógico): evalúa la otra condición si
#                  la primera no se cumple.
# -type d       -> Busca directorios (carpetas).
# -type f       -> Busca archivos.
# -name         -> Busca elementos por su nombre.
# -exec rm -rf  -> Elimina las carpetas encontradas.
# {} +          -> Agrupa las rutas encontradas para eliminarlas.
# -delete       -> Elimina los archivos encontrados.
#
# IMPORTANTE:
# Se excluyen venv/ y .git/ para no modificar el entorno virtual
# ni los archivos internos del repositorio Git.
# Funciona aunque todavía no existan las carpetas src/ y tests/.
#
clean:
	find . \( -path './venv' -o -path './.git' \) -prune -o -type d -name '__pycache__' -prune -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache
	find . \( -path './venv' -o -path './.git' \) -prune -o -type f -name '*.pyc' -delete

# ------------------------------------------------------------
# TEST - Ejecutar las pruebas
# ------------------------------------------------------------
# Uso: make test
#
# Ejecuta las pruebas de la carpeta tests/ utilizando pytest.
# Sirve para comprobar que el programa funciona correctamente.
# Incluye pruebas de casos normales y casos extremos.
#
# -m pytest ejecuta pytest con el Python del entorno virtual.
#test:
#	$(RUN) -m pytest tests/