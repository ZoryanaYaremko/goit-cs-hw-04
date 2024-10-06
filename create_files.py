import os

# Створення директорії для файлів (опціонально)
directory = "test_files"
if not os.path.exists(directory):
    os.makedirs(directory)

# Функція для створення текстових файлів з ключовими словами
def create_test_files(num_files):
    keywords = ['keyword1', 'keyword2', 'keyword3']
    
    for i in range(1, num_files + 1):
        filename = os.path.join(directory, f'file{i}.txt')
        with open(filename, 'w', encoding='utf-8') as file:
            # Розподіляємо ключові слова по файлах (наприклад, keyword1 у файл1, keyword2 у файл2 і т.д.)
            content = f'Це файл номер {i}. Він містить ключове слово {keywords[i % 3]}.\n'
            file.write(content)
    print(f"{num_files} файлів успішно створено в папці '{directory}'")

# Введіть кількість файлів, яку хочете створити
if __name__ == "__main__":
    num_files = int(input("Введіть кількість файлів для створення: "))
    create_test_files(num_files)
