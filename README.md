<p align="center">
  <img src="https://github.com/Max-v2/BlumFarm_v2.0/blob/main/Img/logo.svg" width="200"/>
  <h1 align="center">Max-v2</h1>
</p>

def moving_header():
    colors = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    header = """
██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗ █████╗ ██████╗ ███╗   ███╗
██╔══██╗██║     ██║   ██║████╗ ████║██╔════╝██╔══██╗██╔══██╗████╗ ████║
██████╔╝██║     ██║   ██║██╔████╔██║█████╗  ███████║██████╔╝██╔████╔██║
██╔══██╗██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║
██████╔╝███████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚══════╝  ╚═╝╚═╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝                                         
"""
    footer = """
Max-v2 © 2024 
GitHub: https://github.com/Max-v2
"""
    color = colors[int(time.time()) % len(colors)]
    for line in header.splitlines():
        print(color + Style.BRIGHT + line + Style.RESET_ALL)
    for line in footer.splitlines():
        print(Fore.CYAN + Style.BRIGHT + line + Style.RESET_ALL)
