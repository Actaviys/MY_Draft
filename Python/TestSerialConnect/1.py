import serial
import time

serialPort = serial.Serial("/dev/ttyUSB0", 115200)
serialPort.timeout = 1

while True:
    inst = input(">>>")
    serialPort.write(inst.encode())
    # comm = serialPort.readline().decode("ascii")
    # print(comm)

serialPort.close()