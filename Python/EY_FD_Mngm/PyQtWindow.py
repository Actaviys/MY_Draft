import sys
import random
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore, QtWidgets



class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.GridLay = QtWidgets.QGridLayout(self)
        self.GridLayB1 = QtWidgets.QGridLayout(self)
        
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.ButtonConnect = QtWidgets.QPushButton("Connect")
        self.ButtonSend = QtWidgets.QPushButton("Send")
        self.EditInputText = QtWidgets.QLineEdit("Write my name here")
        
        
        
        self.GridLay.addWidget(self.text, 0, 0)
        self.GridLay.addWidget(self.EditInputText, 1, 0)
        self.GridLayB1.addWidget(self.ButtonSend, 0, 0)
        self.GridLayB1.addWidget(self.ButtonConnect, 0, 1)
        
        self.GridLay.addLayout(self.GridLayB1, 3, 0)
        self.ButtonSend.clicked.connect(self.send_text_func)


    @QtCore.Slot()
    def send_text_func(self):
        self.text.setText(self.EditInputText.text())
        print(f"OK -> {self.EditInputText.text()}")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setFixedWidth(400) # Розмір вікна
    widget.setFixedHeight(250)
    widget.show()
    sys.exit(app.exec())
