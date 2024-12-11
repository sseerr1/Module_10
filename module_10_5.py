import time
from datetime import timedelta
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':

    # Линейный вызов
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    end_time = time.monotonic()
    duration = timedelta(seconds=end_time - start_time)
    print(f"{duration} (Линейный)")

    # Многопроцессный вызов
    start_time = time.monotonic()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.monotonic()
    duration = timedelta(seconds=end_time - start_time)
    print(f"{duration} (Многопроцессный)")
