from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

from WidowFile.QTWindow import main_wind_ui
ui = main_wind_ui.Ui_MainWindow()
ui.setupUi(MainWindow) 




import Commands_Functions as cf
ui.ButtonPCoff.clicked.connect(cf.pc_off_func) # Вимикаю ПК

def openYouTube():
    cf.youtube_open_func([])
ui.ButtonYouTube.clicked.connect(openYouTube)


def openYouTubeMusic():
    cf.youtube_open_func(["M"])
ui.ButtonYouTubeMusic.clicked.connect(openYouTubeMusic)















def start_main():
    MainWindow.show()
    # app.exec_()
    sys.exit(app.exec_())
# start_main()