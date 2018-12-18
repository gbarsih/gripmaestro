import sys
#sys.path.insert(0, 'C:/Users/Tor/Desktop/Programming/Packages/Maestro-master')
import maestro
servo = maestro.Controller('ttyS0')
servo.setAccel(0,0)
servo.setAccel(1,0)
servo.setSpeed(0,0)
servo.setSpeed(1,0)

def drop():
    servo.setTarget(0,1000)
    servo.setTarget(1,1000)

def grip():
    servo.setTarget(0,7700)
    servo.setTarget(1,8100)

#input("go")
#drop()
#input("go")
grip()
