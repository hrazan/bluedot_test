from bluedot import BlueDot
from signal import pause

def front(pos):
    print("front")
    
def back(pos):
    print("back")
    
def left(pos):
    print("left")
    
def right(pos):
    print("right")

bd = BlueDot(cols=3, rows=3)

bd[0,0].visible = False
bd[1,0].when_pressed = front
bd[2,0].visible = False
bd[0,1].when_pressed = left
bd[1,1].visible = False
bd[2,1].when_pressed = right
bd[0,2].visible = False
bd[1,2].when_pressed = back
bd[2,2].visible = False