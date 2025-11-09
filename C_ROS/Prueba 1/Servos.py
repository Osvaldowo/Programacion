from simplecontroller import Board 

servo = (12, 13)
puerto = "COM4"

class Servo:
    def __init__(self):
        self.board = Board(puerto)
        self.board.assignServo()

    def assign_servo(self, pin: int):
        self.board.attachServo(pin)

    def setpossition(self, angle: int):
        self.board.servoWrite(angle)
        
    
def main():
    tarjeta = servo.__init__()
    
    while True: 
        servoM = input("Seleccione el servo (s para salir): ")
        
        if servoM == "s":
            
            break
        
        elif servoM in ("1", "2"): 
            if servoM == "1":
                pin = int (servo[0])
            elif servoM == "2":
                pin = int (servo[1])
            
            tarjeta.assign_servo(pin)

            angulo = int (input("Ingrese el angulo del servo: "))
            tarjeta.setpossition(angulo)
        
if __name__ == "__main__":
    main()
    