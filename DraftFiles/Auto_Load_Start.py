import subprocess as sp



def script_comand_read(file:str): # Читаю файл з скриптами
    """ 
    Виконую скрипти .bat
    """
    sr = "".join(file)
    file_path = sr + ".bat"
    try:
        # Виконуємо .bat файл за допомогою subprocess
        sp.run(file_path, shell=True, check=True)
        print(f"Файл {file_path} виконано успішно.")
        
    except sp.CalledProcessError as e:
        print(f"Помилка при виконанні файлу {file_path}: {e}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
script_comand_read("AutoLoad")