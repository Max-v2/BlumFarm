try:
    import pyscreeze
except ImportError:
    print("pyscreeze no está instalado. Por favor, instálalo usando 'pip install pyscreeze'.")
    exit(1)

from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
from colorama import init, Fore, Style

init(autoreset=True)

mouse = Controller()
time.sleep(0.5)

# Encabezado estilo Matrix en movimiento con cambio de colores
def moving_header():
    colors = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    header = """
██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗ █████╗ ██████╗ ███╗   ███╗
██╔══██╗██║     ██║   ██║████╗ ████║██╔════╝██╔══██╗██╔══██╗████╗ ████║
██████╔╝██║     ██║   ██║██╔████╔██║█████╗  ███████║██████╔╝██╔████╔██║
██╔══██╗██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║
██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                                              
"""
    footer = """
Blumfarm
GitHub: https://github.com/tu_usuario
© 2023 Derechos Reservados
"""
    color = colors[int(time.time()) % len(colors)]
    for line in header.splitlines():
        print(color + Style.BRIGHT + line + Style.RESET_ALL)
    for line in footer.splitlines():
        print(Fore.CYAN + Style.BRIGHT + line + Style.RESET_ALL)

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def get_window_by_name(name):
    windows = gw.getWindowsWithTitle(name)
    if not windows:
        print(Fore.RED + "[❌] | Ventana - {} no encontrada!".format(name))
        return None
    print(Fore.GREEN + "[✅] | Ventana encontrada - {}\nPresiona 'q' para pausar.".format(name))
    return windows[0]

def main():
    while True:
        moving_header()
        window_name = input("\nIngrese el nombre de la ventana (1 - TelegramDesktop): ")
        if window_name == '1':
            window_name = "TelegramDesktop"

        telegram_window = get_window_by_name(window_name)
        if not telegram_window:
            continue

        paused = False

        while True:
            if keyboard.is_pressed('q'):
                paused = not paused
                print(Fore.YELLOW + "Pausado\nPresiona 'q' nuevamente para continuar" if paused else Fore.GREEN + "Continuando.")
                time.sleep(0.2)

            if keyboard.is_pressed('x'):
                print(Fore.RED + "Saliendo del programa.")
                return

            if paused:
                continue

            window_rect = (
                telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
            )

            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

            scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

            width, height = scrn.size
            pixel_found = False

            for x in range(0, width, 20):
                for y in range(0, height, 20):
                    r, g, b = scrn.getpixel((x, y))
                    if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                        screen_x = window_rect[0] + x
                        screen_y = window_rect[1] + y
                        click(screen_x + 4, screen_y)
                        time.sleep(0.001)
                        pixel_found = True
                        break
                if pixel_found:
                    break

if __name__ == "__main__":
    main()