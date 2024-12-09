import time
from threading import Thread

# Функция для записи слов в файл
def write_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения функций
start_time = time.time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Измерение времени выполнения потоков
start_time = time.time()

# Создание и запуск потоков
threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Работа потоков {end_time - start_time:.6f} секунд")

