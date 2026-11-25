## Empaquetado de la librería `mazegen`

La librería `mazegen` permite utilizar el generador de laberintos
como un paquete independiente e instalable mediante `pip`.

Todos los comandos deben ejecutarse desde la raíz del proyecto.

### Requisitos previos

Disponer de un entorno virtual e instalar la herramienta de construcción:

```bash
python3 -m venv venv
venv/bin/pip install build
```

### 1. Limpiar empaquetados anteriores

Eliminar los archivos generados durante construcciones anteriores:

```bash
rm -rf dist/ build/ mazegen.egg-info/
```

### 2. Construir el paquete

Generar el paquete utilizando la configuración de `pyproject.toml`:

```bash
venv/bin/python -m build
```

### 3. Comprobar los archivos generados

```bash
ls -lh dist/
```

Se generarán los siguientes archivos:

- `mazegen-1.0.0-py3-none-any.whl`: paquete instalable.
- `mazegen-1.0.0.tar.gz`: distribución del código fuente.

### 4. Instalar el paquete

Instalar la librería dentro del entorno virtual:

```bash
venv/bin/pip install dist/mazegen-1.0.0-py3-none-any.whl
```

### 5. Verificar la instalación

Comprobar la versión, ubicación e información del paquete instalado:

```bash
venv/bin/pip show mazegen
```

### 6. Comprobar la importación

Verificar que la clase `MazeGenerator` puede importarse desde
el paquete instalado:

```bash
venv/bin/python -I -c "from mazegen import MazeGenerator"
```

Si no aparece ningún error, la importación se ha realizado
correctamente.

---

## Comandos adicionales

### Desinstalar el paquete

```bash
venv/bin/pip uninstall mazegen
```

### Reinstalar el paquete

Actualizar el paquete sin necesidad de desinstalarlo previamente,
aunque se mantenga la misma versión:

```bash
venv/bin/pip install --force-reinstall dist/mazegen-1.0.0-py3-none-any.whl
```

### Limpiar los archivos generados

```bash
rm -rf dist/ build/ mazegen.egg-info/
```

---

## Preparación para la entrega

Copiar el paquete definitivo a la raíz del repositorio,
tal y como exige el subject del proyecto A-Maze-ing:

```bash
cp dist/mazegen-1.0.0-py3-none-any.whl .
```

---

## Consideraciones importantes

- Desinstalar el paquete no elimina el código fuente.
- Limpiar las carpetas generadas no desinstala el paquete.
- Reinstalar permite actualizar el código manteniendo la misma versión.
- Después de modificar el código fuente, es necesario volver a
  construir e instalar el paquete.
- No eliminar `dist/` antes de copiar el paquete definitivo
  a la raíz del repositorio.
- No eliminar `pyproject.toml` ni la carpeta `mazegen/`.
- Si se modifica la versión en `pyproject.toml`, se deberán
  adaptar los nombres de los archivos en los comandos anteriores.