## 1
import psutil_EY as plM

# print(plM.cpu_count()) # Кількість віртуальних ядер процесора (CPU)
# print(plM.cpu_freq()) # Загальна частота процесора (CPU)
# print(plM.cpu_percent(interval=1)) # Навантаження на процесор (CPU)
# print(plM.cpu_times_percent(interval=0.9)) # Процентний стан процесора з інтервалом (CPU)
# print(plM.cpu_stats()) # Статус процесів (CPU)
# print(plM.cpu_times()) # Час працювання (CPU)
# print(plM.Process().cpu_affinity()) # Список ядер процесора
# print(plM.boot_time()) # Виводить час роботи процесора
#


# print(plM.disk_partitions()) # Список дисків на ПК
# print(plM.disk_usage("/")) # Навантаження на диск


# print(plM.Process().username()) # Ім'я комп'ютера
# print(plM.Process().cmdline()) # Виводить посилання cmd на файл з відки запушенно файл

# print(plM.Process().cpu_affinity()) # Список ядер процесора
# print(plM.boot_time()) # Виводить час роботи процесора

# 
# print(pl.Process().threads())
# print(pl.Process().as_dict())




# while True:
#     print(plM.cpu_percent(interval=1.5))




## 2
import platform as pf

pc = pf.uname()
# print(pc.system) # Інформація про OS
# print(pc.node) # Назва ПК
# print(pc.machine) # Назва процесора
# print(pc.release) # Реліз
# print(pc.processor) # Опис процесора
print(pc.version)