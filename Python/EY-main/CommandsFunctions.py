import subprocess as sp
import webbrowser as wb
from os import rename
import serial
import serial.tools.list_ports


#-#################
def youtube_open_func(args): # Відкриває ютуб по командах
    if args:
        ytc = "".join(args)
        if ytc == "M" or ytc == "Музика": 
            wb.open("https://www.youtube.com/watch?v=V7HhLEOKrlc&list=PL6yK8n0u0pOcGgnm-8kYnD3UNmFAr2ZQT") # Посилання на плейліст
        if ytc == "P" or ytc == "Списки":
            wb.open("https://www.youtube.com/feed/playlists")
                
    else: wb.open("https://www.youtube.com/") # Якщо небуло команди то на головну
##################




#-#################
def script_comand_read(file:str): # Читаю файл з скриптами
    """ 
    Виконую скрипти .bat
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
def connect_to_Arduino(args): # Приєднатись до Arduino
    com = "".join(args)
    
    if com == "L": list_serial_ports() # Список портів
    # if com == 
        # print(com)


def list_serial_ports(): # Виводжу підключені Arduino
    ports = serial.tools.list_ports.comports()
    port_list = []
    if ports:
        print("Доступні порти:")
        for port in ports:
            port_list.append(port.device)
            print(f"  - {port.device}: {port.description}")
    else:
        print("Серійні порти не знайдені.")
    return port_list
##################

