from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication([]) #Створюємо об'єкт додатку

ui = uic.loadUi("WidowFile/QTWindow/WindEY.ui") #Створюємо інтерфейс(назва файлу)

# def run_qt_window(nameWind):
#     # print("*"*10, nameWind)
#     path_name = "WidowFile\\QTWindow\\" + nameWind

ui.show() #Відтворюємо інтерфейс
app.exec() #Запускаємо програму
