import psutil as pl


# print(pl.cpu_count()) # Кількість віртуальних ядер процесора (CPU)
# print(pl.cpu_freq()) # Загальна частота процесора (CPU)
# print(pl.cpu_percent(interval=1)) # Навантаження на процесор (CPU)
# print(pl.cpu_times_percent(interval=0.9)) # Процентний стан процесора з інтервалом (CPU)
# print(pl.cpu_stats()) # Статус процесів (CPU)
# print(pl.cpu_times()) # Час працювання (CPU)


# print(pl.disk_partitions()) # Список дисків на ПК
print(pl.disk_usage("/")) # Навантаження на диск



# print(pl.Process().username()) # Ім'я комп'ютера
# print(pl.Process().cmdline()) # Виводить посилання cmd на файл з відки запушенно файл
# print(pl.Process().cpu_affinity()) # Список ядер процесора
# print(pl.boot_time()) # Виводить час роботи процесора
#


# while True:
#     print(pl.cpu_percent(interval=1.5))