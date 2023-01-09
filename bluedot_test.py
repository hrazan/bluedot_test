from bluedot import BlueDot
from signal import pause
import time
from PCA9685 import PCA9685



class Motor:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)
    def duty_range(self,duty1,duty2,duty3,duty4):
        if duty1>4095:
            duty1=4095
        elif duty1<-4095:
            duty1=-4095        
        
        if duty2>4095:
            duty2=4095
        elif duty2<-4095:
            duty2=-4095
            
        if duty3>4095:
            duty3=4095
        elif duty3<-4095:
            duty3=-4095
            
        if duty4>4095:
            duty4=4095
        elif duty4<-4095:
            duty4=-4095
        return duty1,duty2,duty3,duty4
        
    def left_Upper_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(0,0)
            self.pwm.setMotorPwm(1,duty)
        elif duty<0:
            self.pwm.setMotorPwm(1,0)
            self.pwm.setMotorPwm(0,abs(duty))
        else:
            self.pwm.setMotorPwm(0,4095)
            self.pwm.setMotorPwm(1,4095)
    def left_Lower_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(3,0)
            self.pwm.setMotorPwm(2,duty)
        elif duty<0:
            self.pwm.setMotorPwm(2,0)
            self.pwm.setMotorPwm(3,abs(duty))
        else:
            self.pwm.setMotorPwm(2,4095)
            self.pwm.setMotorPwm(3,4095)
    def right_Upper_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(6,0)
            self.pwm.setMotorPwm(7,duty)
        elif duty<0:
            self.pwm.setMotorPwm(7,0)
            self.pwm.setMotorPwm(6,abs(duty))
        else:
            self.pwm.setMotorPwm(6,4095)
            self.pwm.setMotorPwm(7,4095)
    def right_Lower_Wheel(self,duty):
        if duty>0:
            self.pwm.setMotorPwm(4,0)
            self.pwm.setMotorPwm(5,duty)
        elif duty<0:
            self.pwm.setMotorPwm(5,0)
            self.pwm.setMotorPwm(4,abs(duty))
        else:
            self.pwm.setMotorPwm(4,4095)
            self.pwm.setMotorPwm(5,4095)
            
 
    def setMotorModel(self,duty1,duty2,duty3,duty4):
        duty1,duty2,duty3,duty4=self.duty_range(duty1,duty2,duty3,duty4)
        self.left_Upper_Wheel(-duty1)
        self.left_Lower_Wheel(-duty2)
        self.right_Upper_Wheel(-duty3)
        self.right_Lower_Wheel(-duty4)


status = 0
prev_status = 0
    
def stop(pos):
    global status
    global prev_status
    status = 0
    PWM.setMotorModel(0,0,0,0)                   #Stop
    prev_status = status

def forward(pos):
    global status
    global prev_status
    status = 1
    print("forward")
    move_motor()
    prev_status = status
    
def back(pos):
    global status
    global prev_status
    status = 2
    print("back")
    move_motor()
    prev_status = status
    
def left(pos):
    global status
    global prev_status
    status = 3
    print("left")
    move_motor()
    prev_status = status
    
def right(pos):
    global status
    global prev_status
    status = 4
    print("right")
    move_motor()
    prev_status = status

def move_motor():
    if status != prev_status:
        if status == 1:
            PWM.setMotorModel(2000,2000,2000,2000)       #Forward
        elif status == 2:
            PWM.setMotorModel(-2000,-2000,-2000,-2000)   #Back
        elif status == 3:
            PWM.setMotorModel(-500,-500,2000,2000)       #Left
        elif status == 4:
            PWM.setMotorModel(2000,2000,-500,-500)       #Right

PWM=Motor()
bd = BlueDot(cols=3, rows=3)

if __name__ == '__main__':
    PWM.setMotorModel(0,0,0,0)
    bd[0,0].visible = False
    bd[1,0].when_pressed = forward
    bd[1,0].when_released = stop
    bd[2,0].visible = False
    bd[0,1].when_pressed = left
    bd[0,1].when_released = stop
    bd[1,1].visible = False
    bd[2,1].when_pressed = right
    bd[2,1].when_released = stop
    bd[0,2].visible = False
    bd[1,2].when_pressed = back
    bd[1,2].when_released = stop
    bd[2,2].visible = False
    
    
