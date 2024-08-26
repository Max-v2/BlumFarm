# BlumFarmProject

Este proyecto es una herramienta automatizada para interactuar con la ventana de telegram y farmeo de blum

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/Max-v2/BlumFarm_v2.0.git
    cd BlumFarm_v2.0
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
    - 2. Español

3. Ingresa el nombre de la ventana con la que deseas interactuar. Por ejemplo, para TelegramDesktop, ingresa `1`.

4. El script buscará la ventana especificada y te notificará si la encuentra o no:
    - Si la ventana es encontrada, verás un mensaje de confirmación.
    - Si la ventana no es encontrada, verás un mensaje de error.

5. Para pausar la interacción, presiona la tecla `q`. Para continuar, presiona `q` nuevamente y para teminar, presiona la tecla `x`

## Notas

- Asegúrate de tener todas las dependencias instaladas correctamente antes de ejecutar el script.
- Si encuentras algún problema con la instalación de `pyscreeze`, puedes instalarlo manualmente usando `pip install pyscreeze`.

Este proyecto está licenciado bajo los términos de la licencia MIT. Para más detalles, consulta el archivo LICENSE.
