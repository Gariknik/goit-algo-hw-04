# Ваше завдання - розробити функцію get_cats_info(path), 
# яка читає цей файл та повертає список словників з інформацією про кожного кота.
def get_cats_info(path: str) -> list[dict]:
    """
    Функція get_cats_info(path) приймає один аргумент в рядковому вигляді - шлях до текстового файлу (path).
    Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
    Функція повертає список словників, де кожен словник містить інформацію про одного кота.
    """
    keys = ['id', 'name', 'age'] # прописані ключі до словників
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = [item.strip().split(',') for item in file.readlines()] #обробка інформації
            result = [dict(zip(keys, value)) for value in data] #формується результат
            return result
    except FileNotFoundError:
        print("файл не знайдено")



if __name__ == "__main__":
    cats_info = get_cats_info("path/to/cats_file.txt")# перевірка виконання функції
    print(cats_info)