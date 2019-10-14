import serial
import time
import bluetooth_comm
from subprocess import call

# voice command functions
def empty(power):
    return power
    pass

def connect(power):    
    #print('connected')
    return power

def light_please(power):
    print('light please')
    power = 70
    bluetooth_comm.sendPower(bluetoothSerial, str(power))
    return power
    
def off_please(power):
    print('off please')
    power = 8
    bluetooth_comm.sendPower(bluetoothSerial, str(power))
    return power
    
def more(power):
    print('more')
    power += 20
    bluetooth_comm.sendPower(bluetoothSerial, str(power))
    return power
    
def less(power):
    print('less')
    power -= 20
    bluetooth_comm.sendPower(bluetoothSerial, str(power))
    return power

power = 70

if __name__ == '__main__':
        
    # integers mapped to voice command functions
    commands = {0:empty,
                17:connect,
                18:light_please,
                19:off_please,
                20:more,
                21:less}
    
    # bluetooth
    bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
    
    # serial settings
    serialInterface = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    serialInterface.flushInput()
    
    
    for i in range(2):
        serialInterface.write(serial.to_bytes([0xAA])) # head        
        serialInterface.write(serial.to_bytes([0x37])) # set compact mode
        time.sleep(1)
        serialInterface.write(serial.to_bytes([0xAA])) # head        
        serialInterface.write(serial.to_bytes([0x21])) # import group 1 and wait for voice input
        time.sleep(1)
    print('init complete')
          
    try:
        while True:
            data_byte = serialInterface.readline()
            int_val = int.from_bytes(data_byte, byteorder='big')
            power = commands[int_val](power)
            
            
    except KeyboardInterrupt:
        print('Quit')
            
    
    
    
    
    

