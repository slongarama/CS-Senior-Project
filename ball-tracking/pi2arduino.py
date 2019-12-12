import serial # sudo pip install pyserial
import time

# ser = serial.Serial('/dev/ttyUSB0', 115200)
ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 9600)

message = 0

while True:
    message += 1
    if message > 180:
        message = 0
    str_msg = str(message)


    try:
        start = "<".encode('utf-8')
        end = ">".encode('utf-8')

        ser.write(start)
        ser.write(str_msg.encode('utf-8'))
        ser.write(end)

        # print(encoded)
        # new = encoded - '0'
        print(message)
        time.sleep(.1)

    except Exception as e:
        print(e)
	# 		serialData = ser.readline()
	# 		prevStates = currStates
