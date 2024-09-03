import threading
import pyscreeze
from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
from colorama import Fore, Style, init
from PIL import ImageGrab

init(autoreset=True)

def moving_header():
    colors = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    header = """
██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗ █████╗ ██████╗ ███╗   ███╗
██╔══██╗██║     ██║   ██║████╗ ████║██╔════╝██╔══██╗██╔══██╗████╗ ████║
██████╔╝██║     ██║   ██║██╔████╔██║█████╗  ███████║██████╔╝██╔████╔██║
██╔══██╗██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║
██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚══════╝  ╚═╝╚═╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝                                         
"""
    footer = """
Max-v2 © 2024 
GitHub: https://github.com/Max-v2
Telegram: https://t.me/Max_A26
Instagram: https://www.instagram.com/Max26.uy 
"""
    color = colors[int(time.time()) % len(colors)]
    for line in header.splitlines():
        print(color + Style.BRIGHT + line + Style.RESET_ALL)
    for line in footer.splitlines():
        print(Fore.CYAN + Style.BRIGHT + line + Style.RESET_ALL)

def click(x, y):
    mouse = Controller()
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def main():
    # Ejecutar moving_header en un hilo separado
    header_thread = threading.Thread(target=moving_header)
    header_thread.start()

    time.sleep(0.5)
    print(Fore.CYAN + "\nSeleccione el idioma:")
    print(Fore.GREEN + "1. English")
    print(Fore.YELLOW + "2. Español")
    print(Fore.BLUE + "3. 中文 (Chino)")
    print(Fore.MAGENTA + "4. Русский (Ruso)")

    while True:
        try:
            language_choice = int(input(Fore.CYAN + "Ingrese su elección: "))
            if language_choice in [1, 2, 3, 4]:
                break
            else:
                print(Fore.RED + "Selección incorrecta. Por favor, ingrese 1, 2, 3 o 4.")
        except ValueError:
            print(Fore.RED + "Entrada incorrecta. Por favor, ingrese un número.")

    if language_choice == 1:
        window_input = "\nEnter the window name (1 - TelegramDesktop): "
        window_not_found = "[❌] | Window - {} not found!"
        window_found = "[✅] | Window found - {}\nPress 'q' to pause."
        pause_message = "Paused\nPress 'q' again to continue"
        continue_message = "Continue working."
    elif language_choice == 2:
        window_input = "\nIngrese el nombre de la ventana (1 - TelegramDesktop): "
        window_not_found = "[❌] | Ventana - {} no encontrada!"
        window_found = "[✅] | Ventana encontrada - {}\nPresione 'q' para pausar."
        pause_message = "Pausa\nPresione 'q' nuevamente para continuar"
        continue_message = "Continuar trabajando."
    elif language_choice == 3:
        window_input = "\n输入窗口名称 (1 - TelegramDesktop): "
        window_not_found = "[❌] | 窗口 - {} 未找到!"
        window_found = "[✅] | 找到窗口 - {}\n按 'q' 暂停."
        pause_message = "暂停\n再次按 'q' 继续"
        continue_message = "继续工作."
    elif language_choice == 4:
        window_input = "\nВведите название окна (1 - TelegramDesktop): "
        window_not_found = "[❌] | Окно - {} не найдено!"
        window_found = "[✅] | Окно найдено - {}\нНажмите 'q' для паузы."
        pause_message = "Пауза\nНажмите 'q' снова, чтобы продолжить"
        continue_message = "Продолжить работу."

    window_name = input(Fore.CYAN + window_input)
    if window_name == '1':
        window_name = "TelegramDesktop"

    telegram_window = gw.getWindowsWithTitle(window_name)
    if not telegram_window:
        print(Fore.RED + window_not_found.format(window_name))
    else:
        print(Fore.GREEN + window_found.format(window_name))

    paused = False
    while True:
        if keyboard.is_pressed('q'):
            paused = not paused
            if paused:
                print(Fore.YELLOW + pause_message)
            else:
                print(Fore.GREEN + continue_message)
            time.sleep(0.2)  # Pequeña pausa para evitar múltiples detecciones

        if keyboard.is_pressed('x'):
            print(Fore.RED + "Exiting program.")
            break

        if paused:
            continue

        telegram_window = gw.getWindowsWithTitle(window_name)
        if telegram_window:
            telegram_window = telegram_window[0]
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

            # Verificar las coordenadas antes de capturar la pantalla
            left, top, right, bottom = telegram_window.left, telegram_window.top, telegram_window.left + telegram_window.width, telegram_window.top + telegram_window.height
            if right > left and bottom > top:
                scrn = ImageGrab.grab(bbox=(left, top, right, bottom))
                width, height = scrn.size
                pixel_found = False

                for x in range(0, width, 20):
                    for y in range(0, height, 20):
                        r, g, b = scrn.getpixel((x, y))
                        if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                            screen_x = left + x
                            screen_y = top + y
                            click(screen_x + 4, screen_y)
                            time.sleep(0.001)
                            pixel_found = True
                            break
                    if pixel_found:
                        break
            else:
                print(Fore.RED + "Invalid window dimensions detected.")

if __name__ == "__main__":
    main()