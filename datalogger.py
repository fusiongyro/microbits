import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    print(ser.readline(1000).decode('utf8'))
