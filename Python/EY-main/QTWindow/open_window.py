from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication([]) #Створюємо об'єкт додатку
ui = uic.loadUi("WindEY.ui") #Створюємо інтерфейс(назва файлу) (для .bat -> "WindEY.ui") (для тесту -> "QTWindow\WindEY.ui") 




ui.show() #Відтворюємо інтерфейс
app.exec() #Запускаємо програму
