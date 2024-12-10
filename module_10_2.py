import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__(name=name)
        # threading.Thread.__name__(self)
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        remaining_enemies = 100
        while remaining_enemies > 0:
            time.sleep(1)
            self.days += 1
            remaining_enemies -= self.power
            if remaining_enemies < 0:
                remaining_enemies = 0
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

        #########################


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
