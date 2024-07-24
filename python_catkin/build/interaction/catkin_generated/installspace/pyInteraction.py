from telemetrix import telemetrix
import time
import sys
import threading

class pyInteraction:
    def __init__(self):
        # set up board
        self.board = telemetrix.Telemetrix(com_port = '/dev/ttyUSB0')
        self.ledPin = 2
        self.conn2Pin = 8
        self.interact = False
        self.set_up_pin()
        self.__detect = threading.Thread(target = self.detect, daemon = True)
        self.__detect.start()
    
    def set_up_pin(self):
        # set up pin
        self.board.set_pin_mode_digital_output(self.ledPin)
        self.board.set_pin_mode_digital_input_pullup(self.conn2Pin, self.callback)
         
    def getInteract(self):
        return self.interact

    def setInteract(self, value):
        self.interact = value

    def detect(self):
        try:
            while True:
                time.sleep(0.001)
                
        except KeyboardInterrupt:
            self.board.shutdown()
            sys.exit(0)
     
    def callback(self, data):
        if data[2] == 0:
            self.board.digital_write(self.ledPin, 1)
            self.setInteract(True)
        else:
            self.board.digital_write(self.ledPin, 0)
            self.setInteract(False)

def main():
    itr = pyInteraction()
    while True:
        print(itr.getInteract())
        time.sleep(0.1)

if __name__ == "__main__":
    main()
