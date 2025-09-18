import sys
from pathlib import Path
from log import log_files, log_directories, log_error


# Функція для відображення вмісту директорії
def print_directory_structure(path: Path, indent: str = ""):
    # Перевірка, чи є це директорією
    if path.is_dir():
        # Виводимо саму директорію (синій колір)
        log_directories(indent,f"{path.name}/")
        # Рекурсивно відображаємо вміст
        for item in path.iterdir():
            if item.is_dir():
                print_directory_structure(item, indent + "    ")
            else:
                # Виводимо файл (зелений колір)
                log_files(indent, item.name)
    else:
        print(f"Шлях {path} не є директорією!")

# Основна частина програми
def main():
    # Перевіряємо, чи передано аргумент
    if len(sys.argv) != 2:
        log_error("Помилка: потрібно вказати шлях до директорії!")
        return
    
    # Отримуємо шлях до директорії з аргументів
    directory_path = sys.argv[1]
    
    # Вивести отриманий шлях для перевірки
    print(f"Отриманий шлях: {directory_path}")
    
    path = Path(directory_path)
    
    # Перевірка, чи існує вказаний шлях і чи це директорія
    if not path.exists():
        log_error(f"Помилка: вказаний шлях не існує!")
        return
    
    if not path.is_dir():
        log_error(f"Помилка: вказаний шлях не є директорією!")
        return
    
    # Виводимо структуру директорії
    print_directory_structure(path)




if __name__ == "__main__":
    main()
