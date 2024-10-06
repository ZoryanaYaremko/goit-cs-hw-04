import os
import multiprocessing
import time

# Функція для пошуку ключових слів у файлах
def search_keywords_in_files(files, keyword, queue):
    result = {keyword: []}
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read().lower()  # Перетворюємо вміст файлу на нижній регістр
                if keyword.lower() in content:  # Перетворюємо ключове слово на нижній регістр
                    result[keyword].append(file)
        except Exception as e:
            print(f"Помилка при обробці файлу {file}: {e}")
    queue.put(result)

# Функція для обробки файлів процесами
def multiprocessing_search(files, keywords):
    processes = []
    queue = multiprocessing.Queue()
    result = {keyword: [] for keyword in keywords}
    file_chunks = [files[i::len(keywords)] for i in range(len(keywords))]  # Розподіл файлів між процесами

    for i, keyword in enumerate(keywords):
        p = multiprocessing.Process(target=search_keywords_in_files, args=(file_chunks[i], keyword, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Збір результатів з черги
    while not queue.empty():
        res = queue.get()
        for keyword, files in res.items():
            result[keyword].extend(files)

    return result

if __name__ == "__main__":
    start_time = time.time()

    # Вказуємо директорію, де зберігаються файли
    directory = "test_files"
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    keywords = ['keyword1', 'keyword2', 'keyword3']

    # Виведення результатів
    result = multiprocessing_search(files, keywords)
    print("Результати пошуку з процесами:", result)

    print(f"Час виконання (multiprocessing): {time.time() - start_time} секунд")
