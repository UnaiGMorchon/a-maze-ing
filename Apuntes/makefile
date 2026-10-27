PYTHON = python3
VENV = venv

.PHONY: setup install test lint format clean run

setup:  # Crea el entorno virtual e instala/actualiza pip
		$(PYTHON) -m venv $(VENV)
		$(VENV)/bin/pip install --upgrade pip

install: setup  # Instala dependencias y antes de ejecutar install, Make ejecutará setup
		$(VENV)/bin/pip install -r requirements.txt

test:  # Ejecuta los tests con pytest
		$(VENV)/bin/python -m pytest tests/

lint:  # Comprueba el estilo y los tipos (obligatorio)
		$(VENV)/bin/flake8 .
		$(VENV)/bin/mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:  # Comprobación estricta (opcional)
		$(VENV)/bin/mypy . --strict

format:  # Formatea el código con Black
		$(VENV)/bin/black src/

run:  # Ejecuta el programa
		$(VENV)/bin/python src/main.py

# pdb es el depurador integrado de Python.
# Te permite ejecutar el programa paso a paso, detenerlo e inspeccionar variables.
debug:  # Ejecuta el programa con el depurador pdb 
		$(venv)/bin/python -m pdb src/main.py

clean:  # Elimina archivos temporales
		find . -type d -name '__pycache__' -prune -exec rm -rf {} +
		rm -rf __pycache__ .pytest_cache .mypy_cache
		find . -type f -name '*.pyc' -delete



Entrarás en el depurador y podrás utilizar comandos como:

Comando			Significado
n			Ejecutar la siguiente línea
s			Entrar dentro de una función
c			Continuar la ejecución
p variable		Mostrar el valor de una variable








q	Salir del depurador
