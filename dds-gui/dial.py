
from tkinter import *
import math

#
# This file implments the custom dial control for tkinter
#

class Dial(Canvas):
    width = 240
    height = 240
    dialDiam = 200
    knobDiam = 40
    dialColor = 'lightgrey'
    knobColorSelected = 'red'
    knobColorUnselected = 'darkgray'
    knobColor = knobColorUnselected
    dialX = width/2
    dialY = height/2
    knobOffset = height/4
    knobX = dialX
    knobY = dialY-knobOffset
    knobSelected = False
    knobTheta = -math.pi/2

    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,width=self.width,height=self.height,**kwargs)
        self.bind('<ButtonPress-1>',self.mouseButtonPressEvent)
        self.bind('<ButtonRelease-1>',self.mouseButtonReleaseEvent)
        self.bind('<B1 Motion>',self.mouseMotionEvent)
        self.draw()

    def draw(self):
        self.fillCircle(self.dialX,self.dialY,self.dialDiam,self.dialColor)
        self.drawShadowedCircle(self.dialX,self.dialY,self.dialDiam,self.dialColor)
        self.fillCircle(self.knobX,self.knobY,self.knobDiam,self.knobColor)
        self.drawShadowedCircle(self.knobX,self.knobY,self.knobDiam,self.knobColor)

    def fillCircle(self,x,y,diam,color):
        self.create_oval(x-diam/2,y-diam/2,x+diam/2,y+diam/2,fill=color,width=0)

    def drawShadowedCircle(self,x,y,diam,color):
       self.create_arc(x-diam/2,y-diam/2,x+diam/2,y+diam/2,width=1,outline='white',style=ARC,start=45,extent=180)
       self.create_arc(x-diam/2,y-diam/2,x+diam/2,y+diam/2,width=1,outline='darkgrey',style=ARC,start=225,extent=180)

    def mouseButtonPressEvent(self,event):
        if abs(event.x - self.knobX) < self.knobDiam/2 and abs(event.y - self.knobY) < self.knobDiam/2 :
            self.knobColor = self.knobColorSelected
            self.knobSelected = True
            self.draw()

    def mouseButtonReleaseEvent(self,event):      
        self.knobColor = self.knobColorUnselected
        self.knobSelected = False
        self.draw()

    def mouseMotionEvent(self,event):
        if self.knobSelected :
            y = event.y - self.dialY
            x = event.x - self.dialX
            if x == 0: x = .001 
            theta = math.atan(y/x)
            if x < 0 : theta += math.pi
            self.knobX = self.dialX + self.knobOffset * math.cos(theta)
            self.knobY = self.dialY + self.knobOffset * math.sin(theta)

            if (theta - self.knobTheta) > math.pi/16 :
                self.event_generate('<<DialIncrement>>')
                self.knobTheta = theta

            if ( self.knobTheta - theta) > math.pi/16 :
                self.event_generate('<<DialDecrement>>')
                self.knobTheta = theta

            self.draw()
