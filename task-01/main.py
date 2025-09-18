# Ваше завдання - розробити функцію total_salary(path), 
# яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
def total_salary(path: str) -> tuple[int|float]:
    """
    Функція total_salary(path) приймає один аргумент рядкового типу - шлях до текстового файлу (path).
    Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
    Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
    Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
    """
    try:
        with open(path, 'r',encoding="utf-8") as file:
            data = list(map(lambda x: float(x.strip().split(',')[1]), file.readlines())) #получаєм та обробляємо дані
            total = sum(data) #Знаходимо суму заробітних плат
            average = round(total / len(data)) #Знаходимо середню заробітну плату
            return total, average
    except FileNotFoundError:
        print("Не можу знайти файл")
        return None, None
    except ZeroDivisionError:
        print("Відсутні дані для обробки. Обробка винятку ділення на нуль")
        return None, None

if __name__ == "__main__":                
    total, average = total_salary("path/to/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")