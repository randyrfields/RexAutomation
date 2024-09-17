import serial
import time
import unicodedata
from cobs import cobs
from channels.generic.websocket import AsyncWebsocketConsumer
import json


def ScanBus():

    port = '/dev/ttyS1'
    baudrate = 115200
    timeout = 1
  
    ser = serial.Serial(port, baudrate, timeout=timeout)

    unicode_string = "RX:SCANBUS."
    utfvalue = unicode_string.encode('utf-8')
    encoded = cobs.encode(utfvalue)
    ser.write(encoded)
    ser.write(b'\x00')
    time.sleep(1)
    # response = port.readline()
    response = 37373

    print("Made it here")

    
    return response


def main():
    ScanBus()

if __name__=="__main__":
    main()

