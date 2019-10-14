#! /usr/bin/python

import serial

def sendPower(bluetoothSerial, power):
                        
    bluetoothSerial.write(str.encode(power))
    print(power)    