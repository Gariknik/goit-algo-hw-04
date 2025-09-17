from colorama import Fore, init
# Ініціалізуємо colorama
init(autoreset=True) 

def log_directories(indent, message):
    print(f"{indent} {Fore.BLUE} {message}")

def log_files(indent, message):
    print(f"{indent+ "    "} {Fore.GREEN} {message}")

def log_error(message):
    print(f"{Fore.RED} {message}")