import os
import threading
import time

# Функція для пошуку ключових слів у файлах
def search_keywords_in_files(files, keyword, result):
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read().lower()  # Перетворюємо вміст файлу на нижній регістр
                if keyword.lower() in content:  # Перетворюємо ключове слово на нижній регістр
                    result[keyword].append(file)
        except Exception as e:
            print(f"Помилка при обробці файлу {file}: {e}")

# Функція для обробки файлів потоками
def threaded_search(files, keywords):
    threads = []
    result = {keyword: [] for keyword in keywords}
    file_chunks = [files[i::len(keywords)] for i in range(len(keywords))]  # Розподіл файлів між потоками

    for i, keyword in enumerate(keywords):
        t = threading.Thread(target=search_keywords_in_files, args=(file_chunks[i], keyword, result))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result

if __name__ == "__main__":
    start_time = time.time()

    # Вказуємо директорію, де зберігаються файли
    directory = "test_files"
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    keywords = ['keyword1', 'keyword2', 'keyword3']

    # Виведення результатів
    result = threaded_search(files, keywords)
    print("Результати пошуку з потоками:", result)

    print(f"Час виконання (threading): {time.time() - start_time} секунд")
