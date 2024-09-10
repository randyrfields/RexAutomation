import serial
import time
from cobs import cobs



def ScanBus():

    port = '/dev/ttyS1'
    baudrate = 115200
    timeout = 1
  
    # ser = serial.Serial(port, baudrate, timeout=timeout)

    # encoded = cobs.encode("RX:SCANBUS.")
    # # port.write(encoded)
    # # port.write(b'\x00')
    # time.sleep(1)
    # response = port.readline()
    response = 37373

    print("Made it here")

    
    return response

