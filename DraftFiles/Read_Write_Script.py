import subprocess as sp
from os import rename
#-#################
def script_comand_read(file:str): # Читаю файл з скриптами
    """ 
    Функція для виконання скриптів (.bat). \n  
    """
    sr = "".join(file)
    file_path = "Skripts\\" + sr + ".bat"
    try:
        # Виконуємо .bat файл за допомогою subprocess
        sp.run(file_path, shell=True, check=True)
        print(f"Файл {file_path} виконано успішно.")
        
    except sp.CalledProcessError as e:
        print(f"Помилка при виконанні файлу {file_path}: {e}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")


def create_and_save_as_bat(args:list): # Створюю скріпти (.bat)
    """ 
    Функція для створення файлів формату (.bat) \n
    Приймає список аргументів. \n
    Де перший елементи в списку це назва файлу (без пробілів). \n
    А наступні елементи списку об'єднуються в рядок та 
    будуть записані в файл.
    """
    content = "" # Змінна для тексту 
    filename = args.pop(0) # Змінна для назви файлу
    for csb in args: # Цикл для об'єднання елементів списку (без першого)
        content += csb
        content += " "
    
    # Додаємо розширення .txt до файлу
    txt_filename = f"Skripts/{filename}.txt"
    
    # Записуємо дані у файл
    with open(txt_filename, 'w', encoding='utf-8') as file:
        file.write(content)
    
    # Змінюємо розширення файлу на .bat
    bat_filename = f"Skripts/{filename}.bat"
    rename(txt_filename, bat_filename)
    
    print(f"Файл успішно створено і збережено як {filename}")
##################








#-#################
# from QTWindow import open_window as ow
def basic_func_open_qt_window(FileNameWind:str):
    """ 
    Функція для виконання скриптів .bat для відкриття вікон QT
    Скрипти виконуються по ключах. \n
    "L" - список ключів з назвами скриптів. \n
    "1" - Основне вікно QT
    """
    fnw = "".join(FileNameWind)
    if fnw == "1": fnw = "LoadQTWindow" # Перевизначення назв файлів .bat
    
    file_path = "QTWindow\\" + fnw + ".bat"
    try:
        # Виконуємо .bat файл за допомогою subprocess
        sp.run(file_path, shell=True, check=True)
        print(f"Файл {fnw} виконано успішно.")
        
    except sp.CalledProcessError as e:
        print(f"Помилка при виконанні файлу {fnw}: {e}")
    except FileNotFoundError:
        print(f"Файл {fnw} не знайдено.")
##################

