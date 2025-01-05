from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import time


class SerialConnection:
    def __init__(self, port_name, baudrate=115200):
        self.serial = QSerialPort()
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(baudrate)

    def connect(self):
        if self.serial.open(QIODevice.ReadWrite):
            print(f"Підключено до порту {self.serial.portName()} зі швидкістю {self.serial.baudRate()}.")
            time.sleep(2)  # Затримка для скидання Arduino
            return True
        else:
            print(f"Не вдалося підключитися до порту {self.serial.portName()}.")
            return False

    # def send_data(self, message):
    #     if self.serial.isOpen():
    #         self.serial.write(message.encode('utf-8'))
    #         print(f"Відправлено: {message}")
    #     else:
    #         print("Порт не відкритий для запису.")

    def read_data(self):
        if self.serial.isOpen():
            dat = self.serial.readAll().data()
            print(dat)


    def disconnect(self):
        if self.serial.isOpen():
            self.serial.close()
            print("Підключення закрито.")


# Використання функції
if __name__ == "__main__":
    # Отримуємо список доступних портів
    available_ports = [port.portName() for port in QSerialPortInfo.availablePorts()]
    print("Доступні порти:", available_ports)

    port = "COM4"  # Вкажіть ваш порт
    baudrate = 115200

    connection = SerialConnection(port, baudrate)
    
    if connection.connect():
        print("Чекаємо дані від Arduino...")
        
        # Читання даних у циклі
        try:
            while True:
                data = connection.read_data()
                if data:
                    print(f"Arduino: {data}")
        except KeyboardInterrupt:
            print("Роботу перервано користувачем.")
        finally:
            connection.disconnect()
