import psutil as pl


# print(pl.cpu_count()) # Кількість віртуальних ядер процесора (CPU)
# print(pl.cpu_freq()) # Загальна частота процесора (CPU)
# print(pl.cpu_percent(interval=1)) # Навантаження на процесор (CPU)
print(pl.Process().username()) # Ім'я комп'ютера
    