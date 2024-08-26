# BlumFarmProject

Este proyecto es una herramienta automatizada para interactuar con la ventana de telegram y farmeo de blum

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://tu-repositorio-url.git
    cd BlumFarmProject
    ```

2. Crea y activa un entorno virtual:

    En Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    En macOS y Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal:

    ```bash
    python BlumFarm.py
    ```

2. Selecciona el idioma en el que deseas interactuar:
    - 1. English
    - 2. Русский
    - 3. Español

3. Ingresa el nombre de la ventana con la que deseas interactuar. Por ejemplo, para TelegramDesktop, ingresa `1`.

4. El script buscará la ventana especificada y te notificará si la encuentra o no:
    - Si la ventana es encontrada, verás un mensaje de confirmación.
    - Si la ventana no es encontrada, verás un mensaje de error.

5. Para pausar la interacción, presiona la tecla `q`. Para continuar, presiona `q` nuevamente y para teminar, presiona la tecla `x`

## Notas

- Asegúrate de tener todas las dependencias instaladas correctamente antes de ejecutar el script.
- Si encuentras algún problema con la instalación de `pyscreeze`, puedes instalarlo manualmente usando `pip install pyscreeze`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Para más detalles, consulta el archivo LICENSE.
