import json
import pyautogui
from pynput.mouse import Listener
from colorama import init, Fore, Style

init(autoreset=True)

# Cargar datos de colores desde color_data.json
try:
    with open('color_data.json', 'r') as f:
        color_data = json.load(f)
except FileNotFoundError:
    color_data = {"tokens": [], "bombs": [], "ice": []}

# Función para manejar los clics del mouse
def on_click(x, y, button, pressed):
    if pressed:
        screen_x, screen_y = x, y
        scrn = pyautogui.screenshot()
        r, g, b = scrn.getpixel((screen_x, screen_y))
        color = {'r': r, 'g': g, 'b': b}
        print(f"Color detectado en ({screen_x}, {screen_y}): {color}")
        category = input("Ingrese la categoría (token, bomba, hielo): ").strip().lower()
        if category == 'token':
            color_data['tokens'].append(color)
        elif category == 'bomba':
            color_data['bombs'].append(color)
        elif category == 'hielo':
            color_data['ice'].append(color)
        else:
            print(Fore.RED + "Categoría no válida. Inténtalo de nuevo.")
            return
        with open('color_data.json', 'w') as f:
            json.dump(color_data, f, indent=4)
        print(f"Color {color} guardado en la categoría {category}")

# Iniciar el listener para capturar clics del usuario
def main():
    print(Fore.GREEN + "Iniciando captura de colores. Haz clic en la pantalla para capturar un color.")
    print(Fore.YELLOW + "Presiona 'Ctrl+C' para salir.")
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()