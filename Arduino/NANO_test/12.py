from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox, QTextEdit, QLabel
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import sys


class SerialApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Connection")
        self.setGeometry(100, 100, 400, 300)

        self.serial = QSerialPort()
        self.serial.readyRead.connect(self.read_data)

        # Елементи інтерфейсу
        self.port_label = QLabel("Select Port:")
        self.port_combo = QComboBox()
        self.refresh_ports()

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_port)

        self.send_button = QPushButton("Send")
        self.send_button.setEnabled(False)
        self.send_button.clicked.connect(self.send_data)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter message to send...")

        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Received messages...")
        self.output_text.setReadOnly(True)

        # Розташування елементів
        layout = QVBoxLayout()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_combo)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.input_text)
        layout.addWidget(self.send_button)
        layout.addWidget(self.output_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def refresh_ports(self):
        self.port_combo.clear()
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.port_combo.addItem(port.portName())

    def connect_to_port(self):
        if self.serial.isOpen():
            self.serial.close()
            self.connect_button.setText("Connect")
            self.send_button.setEnabled(False)
            self.output_text.append("Disconnected.")
        else:
            selected_port = self.port_combo.currentText()
            self.serial.setPortName(selected_port)
            self.serial.setBaudRate(115200)

            if self.serial.open(QIODevice.ReadWrite):
                self.connect_button.setText("Disconnect")
                self.send_button.setEnabled(True)
                self.output_text.append(f"Connected to {selected_port}.")
            else:
                self.output_text.append(f"Failed to connect to {selected_port}.")

    def send_data(self):
        if self.serial.isOpen():
            message = self.input_text.toPlainText()
            if message:
                self.serial.write(message.encode('utf-8'))
                self.output_text.append(f"Sent: {message}")
                self.input_text.clear()

    def read_data(self):
        if self.serial.isOpen():
            data = self.serial.readAll().data().decode('utf-8').strip()
            self.output_text.append(f"Received: {data}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialApp()
    window.show()
    sys.exit(app.exec_())