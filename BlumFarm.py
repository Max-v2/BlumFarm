try:
    import pyscreeze
except ImportError:
    print("pyscreeze is not installed. Please install it using 'pip install pyscreeze'.")
    exit(1)

from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

mouse = Controller()
time.sleep(0.5)

print(f"{Fore.CYAN}Max-v2 © 2024")

print(f"\n{Fore.YELLOW}Seleccione el idioma:")
print(f"{Fore.YELLOW}1. English")
print(f"{Fore.YELLOW}2. Español")
print(f"{Fore.YELLOW}3. 中文 ")
print(f"{Fore.YELLOW}4. Русский")

while True:
    try:
        language_choice = int(input(f"{Fore.YELLOW}Ingrese el número de su idioma: "))
        if language_choice in [1, 2, 3, 4]:
            break
        else:
            print(f"{Fore.RED}Selección incorrecta. Por favor, ingrese 1, 2, 3 o 4.")
    except ValueError:
        print(f"{Fore.RED}Entrada incorrecta. Por favor, ingrese un número.")

if language_choice == 1:
    window_input = f"\n{Fore.GREEN}Enter window name (1 - TelegramDesktop): "
    window_not_found = f"{Fore.RED}[❌] | Window - {{}} not found!"
    window_found = f"{Fore.GREEN}[✅] | Window found - {{}}\nPress 'q' to pause."
    pause_message = f"{Fore.YELLOW}Pause\nPress 'q' again to continue"
    continue_message = f"{Fore.GREEN}Continue working."
elif language_choice == 2:
    window_input = f"\n{Fore.GREEN}Ingrese el nombre de la ventana (1 - TelegramDesktop): "
    window_not_found = f"{Fore.RED}[❌] | Ventana - {{}} no encontrada!"
    window_found = f"{Fore.GREEN}[✅] | Ventana encontrada - {{}}\nPresione 'q' para pausar."
    pause_message = f"{Fore.YELLOW}Pausa\nPresione 'q' nuevamente para continuar"
    continue_message = f"{Fore.GREEN}Continuar trabajando."
elif language_choice == 3:
    window_input = f"\n{Fore.GREEN}输入窗口名称 (1 - TelegramDesktop): "
    window_not_found = f"{Fore.RED}[❌] | 窗口 - {{}} 未找到!"
    window_found = f"{Fore.GREEN}[✅] | 找到窗口 - {{}}\n按 'q' 暂停."
    pause_message = f"{Fore.YELLOW}暂停\n再次按 'q' 继续"
    continue_message = f"{Fore.GREEN}继续工作."
elif language_choice == 4:
    window_input = f"\n{Fore.GREEN}Введите имя окна (1 - TelegramDesktop): "
    window_not_found = f"{Fore.RED}[❌] | Окно - {{}} не найдено!"
    window_found = f"{Fore.GREEN}[✅] | Окно найдено - {{}}\nНажмите 'q' для паузы."
    pause_message = f"{Fore.YELLOW}Пауза\nНажмите 'q' снова, чтобы продолжить"
    continue_message = f"{Fore.GREEN}Продолжить работу."

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
else:
    print(window_found.format(window_name))

telegram_window = check[0]
paused = False

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print(pause_message)
        else:
            print(continue_message)
        time.sleep(0.2)

    if keyboard.is_pressed('x'):
        print(f"{Fore.RED}Exiting program.")
        break

    if paused:
        continue

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False
    if pixel_found == True:
        break

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