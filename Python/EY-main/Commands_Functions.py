import webbrowser as wb
from WidowFile.PYWin import WindEY1, QtWindEY2


def open_other_files():
    """ 
    Функція для відкриття файлів
    """
    print("OOOOOOOOO")



#-#################
# from QTWindow import open_window as ow
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

