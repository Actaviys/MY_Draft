import webbrowser as wb
from WidowFile.PYWin import WindEY1, QtWindEY2
import psutil as pl



def pc_read_information(elementName:list):
    """ 
    Функція читання параметрів ПК. \n
    Приймає список з елементів які потрібно вивести. \n
    Доступні для читання елементи: \n
    [-CPU, -GPU, -MEMORY, -DISK, -NAME, -OS]
    """
    available_items = ["CPU", "DISK"]
    for elnm in elementName:
        if elnm in available_items:
            try:
                if elnm == "CPU":
                    print(f"Список ядер процесора: {pl.Process().cpu_affinity()}")
                    print(f"Кількість віртуальних ядер: {pl.cpu_count()}")
                    print(f"Частота процесора: {pl.cpu_freq().current}")
                    # print(elnm)
                
            except: print(f"Не виконано {elnm}")
            # print(elnm)
# pc_read_information(["123qw", "wer", "CPU", "234", "DISK"])



#-#################
from WidowFile.QTWindow import main_wind_ui, cmdEY_ui, QtWindTest_ui, WindSerialPort_ui
def basic_func_open_qt_window(FileNameWind):
    """ 
    Функція відкриття вікон QT. \n
    Вікна відкриваються по ключах. \n
    "L" - список ключів з назвами скриптів. \n
    "1" - Основне вікно QT \n
    """
    fnw = "".join(FileNameWind)
    
    # Перевизначення ключів на назви файлів
    if fnw == "1":
        WindEY1.open_window()
    if fnw == "2":
        QtWindEY2.open_window()
    
    # print(fnw)
##################
# basic_func_open_qt_window("2")





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


# def open_other_files():
#     """ 
#     Функція для відкриття файлів
#     """
#     print("OOOOOOOOO")












###
#-#################
# def connect_to_Arduino(args): # Приєднатись до Arduino
#     com = "".join(args)
    
#     if com == "L": list_serial_ports() # Список портів
#     # if com == 
#         # print(com)


# def list_serial_ports(): # Виводжу підключені Arduino
#     ports = serial.tools.list_ports.comports()
#     port_list = []
#     if ports:
#         print("Доступні порти:")
#         for port in ports:
#             port_list.append(port.device)
#             print(f"  - {port.device}: {port.description}")
#     else:
#         print("Серійні порти не знайдені.")
#     return port_list
##################

