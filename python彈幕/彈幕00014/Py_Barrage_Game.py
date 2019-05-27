import math
import random
import pygame as pg

power=5#5
Balltimes=0
BallSize=45#50
danger=20#10
distance=45#50
Red_Count=5
AllBall=7200
HP=100

#90#60#195#100#300
#1250
hit=3
cl=pg.time.Clock()

pg.init()
screen=pg.display.set_mode([1024,768])
white=pg.color.Color('#FFFFFF')
black=pg.color.Color('#000000')
gray=pg.color.Color('#888888')
red=pg.color.Color('#882222')
yellow=pg.color.Color('#FFFF00')

seed=random.choice([90,60,195,100,300])
random.seed(seed)

My_image=pg.image.load('triangle0001.png')
Whool_image=pg.image.load('whool.png')

sound1=pg.mixer.music.load('laser2.mp3')
sound2 = pg.mixer.Sound('explosion1.wav')
sound3=pg.mixer.Sound('clapping_short.wav')
sound4=pg.mixer.Sound('explosion2.wav')

My_X=100
My_Y=710
My_Speed=1
My_Size=20

Shoot_X=My_X
Shoot_Y=My_Y
final=0


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
for i in range(0,AllBall):
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
    if xx<100:
        xx=100
    if yy<100:
        yy=100
    if xx>800:
        xx=800
    if yy>300:
        yy=300
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
    for i in range(0,AllBall,power):      
        if i==0:
            
            j+=1
            if j>=30:
                j=0
                rotateAngel+=random.randint(90,90)
            pass         
            pg.draw.ellipse(screen,red,[xx-25+random.randint(-5,5),yy-25+random.randint(-5,5),200,200])
        if Balltimes>=(i)*power:
            They_Array[i].going()
            They2_Array[i].going()
            if 1024>They_Array[i].they_X>0 and 768>They_Array[i].they_Y>0:
                pg.draw.ellipse(screen,yellow,[They_Array[i].they_X,They_Array[i].they_Y,BallSize,BallSize])
            if 1024>They2_Array[i].they_X>0 and 768>They2_Array[i].they_Y>0:
                pg.draw.ellipse(screen,yellow,[They2_Array[i].they_X,They2_Array[i].they_Y,BallSize,BallSize])
            if They_Array[i].they_X>=My_X-20 and They_Array[i].they_X<=My_X+20 and They_Array[i].they_Y>=My_Y-20 and They_Array[i].they_Y<=My_Y+20:
                EndCheck=1
                final=2
            if They2_Array[i].they_X>=My_X-20 and They2_Array[i].they_X<=My_X+20 and They2_Array[i].they_Y>=My_Y-20 and They2_Array[i].they_Y<=My_Y+20:
                EndCheck=1
                final=2
        else:
            xx=They_Array[i+1].they_X
            yy=They_Array[i+1].they_Y
            break
        pass
    pass
    
    Shoot_Y-=1
    if HP<=0:
        EndCheck=1
        final=1
    if yy<Shoot_Y<yy+100 and xx+150>Shoot_X>xx-30:
        Shoot_Y=My_Y
        Shoot_X=My_X+20
        Red_Count=0
        red=pg.color.Color('#996666')
        HP-=hit
        sound2.play()
    elif Shoot_Y<0:
        Shoot_Y=My_Y
        Shoot_X=My_X+20
    pg.draw.rect(screen,red,[0,0,HP*10,30])
    pg.draw.rect(screen,white,[Shoot_X,Shoot_Y,10,30])
    screen.blit(pg.transform.rotate(Whool_image,rotateAngel),(xx-0,yy-0))
    if Red_Count<30:
        Red_Count+=1
        
    else:
        
        red=pg.color.Color('#882222')
    #cl.tick(300)

    pg.mixer.music.play()
    
if final==0:
    pg.quit()
elif final==1:
    sound4.play()
    yellowEnd=[pg.color.Color('#FFFF00'),pg.color.Color('#FFFF20'),pg.color.Color('#FFFF40'),pg.color.Color('#FFFF60'),pg.color.Color('#FFFF80')]
    for i3 in range(100):
        pg.display.flip()
        pg.draw.ellipse(screen,yellowEnd[i3//20],[xx-i3+70,yy-i3+70,i3*2,i3*2])
        cl.tick(100) 
    pass
    sound3.play()
    for i3 in range(500):
        pg.display.flip()
        pg.draw.ellipse(screen,black,[xx-120+70,yy-120+70,240,240])
        cl.tick(100) 
    pass
    pass
elif final==2:
    sound4.play()
    yellowEnd=[pg.color.Color('#FFFF00'),pg.color.Color('#FFFF20'),pg.color.Color('#FFFF40'),pg.color.Color('#FFFF60'),pg.color.Color('#FFFF80')]
    for i3 in range(100):
        pg.display.flip()
        pg.draw.ellipse(screen,yellowEnd[i3//20],[My_X-i3,My_Y-i3,i3*2,i3*2])
        cl.tick(100) 
    pass
    for i3 in range(100):
        pg.display.flip()
        pg.draw.ellipse(screen,black,[My_X-100,My_Y-100,200,200])
        cl.tick(100) 
    pass
