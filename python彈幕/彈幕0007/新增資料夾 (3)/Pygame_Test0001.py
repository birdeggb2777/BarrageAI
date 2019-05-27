import math
import random
import pygame as pg

power=5#7
Balltimes=0
BallSize=50
danger=10#20#60
distance=50#90

cl=pg.time.Clock()

pg.init()
screen=pg.display.set_mode([1024,768])
white=pg.color.Color('#FFFFFF')
black=pg.color.Color('#000000')
gray=pg.color.Color('#888888')
red=pg.color.Color('#882222')
yellow=pg.color.Color('#FFFF00')

Now_Move=0
My_image=pg.image.load('triangle0001.png')
Ball_image=pg.image.load('yellowball.png')
Whool_image=pg.image.load('whool.png')
My_X=512
My_Y=710
My_Speed=1
My_Size=20
class they():
    def __init__(self):
        self.they_Speed=1
        self.they_Angel=0
        self.they_Size=20
        self.they_Y=500
        self.they_X=150
    def SetAngel(self,n):
        self.they_Angel=n
    def SetXY(self,x,y):
        self.they_X=x
        self.they_Y=y
    def going(self):
        self.they_X += self.they_Speed * math.sin(math.radians(self.they_Angel))
        self.they_Y -= self.they_Speed * math.cos(math.radians(self.they_Angel))
    def tempX(self):
        return self.they_X +(self.they_Speed * math.sin(math.radians(self.they_Angel)))*danger
    def tempY(self):
        return self.they_Y -(self.they_Speed * math.cos(math.radians(self.they_Angel)))*danger
        '''if 1024>self.they_X>0 or 768>self.they_Y>0:
            self.they_X=0
            self.they_Y=0'''
They_Array=[]
They2_Array=[]
tempX=512-150
tempY=380-150
for i in range(0,24000):
    tempX=tempX+random.randint(-5,5)
    tempY=tempY+random.randint(-5,5)
    obj=they()
    They_Array.append(obj)
    They_Array[i].SetAngel(i**2.1)   
    They_Array[i].SetXY(tempX,tempY)
    obj2=they()
    They2_Array.append(obj2)
    They2_Array[i].SetAngel((i)**1.5)
    They2_Array[i].SetXY(tempX,tempY)
pass
rotateAngel=0
EndCheck=0
xx=0
yy=0
j=0
Now_flag=0
while (EndCheck==0):
    Balltimes+=1
    pg.display.flip()
    screen.fill(black)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            EndCheck=1
        pass
    pass
    keys=pg.key.get_pressed()
    if keys[pg.K_w]:
        My_Y-=My_Speed
    if keys[pg.K_a]:
        My_X-=My_Speed
    if keys[pg.K_s]:
        My_Y+=My_Speed
    if keys[pg.K_d]:
        My_X+=My_Speed
        
    if Now_Move==1:
        My_X-=My_Speed
    if Now_Move==2:
        My_X+=My_Speed
	
    if My_X<0:
        My_X=0
    if My_Y<0:
        My_Y=0
    if My_X>980:
        My_X=980
    if My_Y>700:
        My_Y=700
    screen.blit(My_image,(My_X,My_Y))
    Now_flag=0
    for i in range(0,24000,power):      
        if i==0:
            
            j+=1
            if j>=30:
                j=0
                rotateAngel+=random.randint(90,90)
            pass         
            pg.draw.ellipse(screen,red,[xx-25+random.randint(-5,5),yy-25+random.randint(-5,5),200,200])
            #screen.blit(pg.transform.rotate(Whool_image,rotateAngel),(xx+,yy))
        if Balltimes>=(i)*power:
            #if math.sqrt(((They_Array[i].they_X-(My_X))**2+(They_Array[i].they_Y-(My_Y))**2))<=distance:
                #EndCheck=1
            #if math.sqrt(((They2_Array[i].they_X-(My_X))**2+(They2_Array[i].they_Y-(My_Y))**2))<=distance:
                #EndCheck=1
            
            if math.sqrt(((They_Array[i].tempX()-My_X)**2+(They_Array[i].tempY()-My_Y)**2))<=distance:
                if They_Array[i].tempX()>My_X:
                    Now_Move=1
                elif They_Array[i].tempX()<My_X:
                    Now_Move=2
                else:
                    Now_Move=0
                Now_flag=1
            if math.sqrt(((They2_Array[i].tempX()-My_X)**2+(They2_Array[i].tempY()-My_Y)**2))<=distance:
                if They2_Array[i].tempX()>My_X:
                    Now_Move=1
                elif They2_Array[i].tempX()<My_X:
                    Now_Move=2
                else:
                    Now_Move=0
                Now_flag=1
            They_Array[i].going()
            They2_Array[i].going()
            #screen.blit(Ball_image,(They_Array[i].they_X,They_Array[i].they_Y))
            #screen.blit(Ball_image,(They2_Array[i].they_X,They_Array[i].they_Y))
            if 1024>They_Array[i].they_X>0 and 768>They_Array[i].they_Y>0:
                pg.draw.ellipse(screen,yellow,[They_Array[i].they_X,They_Array[i].they_Y,BallSize,BallSize])
            if 1024>They2_Array[i].they_X>0 and 768>They2_Array[i].they_Y>0:
                pg.draw.ellipse(screen,yellow,[They2_Array[i].they_X,They2_Array[i].they_Y,BallSize,BallSize])
            #pg.draw.ellipse(screen,red,[xx+20+random.randint(-10,10),yy+20+random.randint(-10,10),150,150])
        else:
            xx=They_Array[i+1].they_X
            yy=They_Array[i+1].they_Y
            break
        pass
    pass
    if Now_flag==0:
        if My_X<xx-150:
            Now_Move=2
        elif My_X>xx+150:
            Now_Move=1
        else:
            Now_Move=0
    screen.blit(pg.transform.rotate(Whool_image,rotateAngel),(xx-0,yy-0))
    #cl.tick(300)
pg.quit()
