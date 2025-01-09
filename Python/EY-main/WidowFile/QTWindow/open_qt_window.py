from PyQt5 import QtCore, QtGui, QtWidgets
import sys



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


import main_wind_ui, cmdEY_ui, QtWindTest_ui, WindSerialPort_ui
def func_open_window_py(UiMainWind): # Функція для відкриття вікна
    ui = UiMainWind
    ui.setupUi(MainWindow) 
    MainWindow.show()
    app.exec_()

# func_open_window_py(main_wind_ui.Ui_MainWindow())
# func_open_window_py(cmdEY_ui.Ui_MainWindow())
# func_open_window_py(QtWindTest_ui.Ui_MainWindow())
# func_open_window_py(WindSerialPort_ui.Ui_MainWindow())



###
# import sys
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow) 


# def open_window(): # Функція для відкриття вікна
#     MainWindow.show()
#     app.exec_()
# open_window()


# import sys
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show() #Відтворюємо інтерфейс
# app.exec() #Запускаємо програму
######