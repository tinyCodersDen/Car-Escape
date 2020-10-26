import pygame
from pygame.locals import *
import random
import time
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Escape")
bg=pygame.image.load("bg2.png")
bgy=-600
bgspeed=1
lives=0
score=0
counter=0
class Car():
    def __init__(self):
        self.image=pygame.image.load("png/mycar.png")
        self.image=pygame.transform.rotozoom(self.image,0,0.1)
        self.x=300
        self.y=450
        self.right=0
        self.left=0
        self.rect=None
    def draw(self):
        self.rect=screen.blit(self.image,(self.x,self.y))
        if self.right==1:
            if self.x<=550:
                self.x=self.x+3
        if self.left==1:
            if self.x>=0:
                self.x=self.x-3
class Enemy():
    def __init__(self):
        self.image=pygame.image.load("png/other-car-new.png")
        self.image=pygame.transform.rotozoom(self.image,0,0.1)
        self.x=random.randint(1,550)
        self.y=bgy
        self.start=time.time()
        self.stop=time.time()
        self.carspeed=5
        self.rect=None
    def reset(self):
        self.x=random.randint(1,550)
        self.y=bgy
    def draw(self):
        self.rect=screen.blit(self.image,(self.x,self.y))
        self.y=self.y+self.carspeed
        if self.y>=600:
            self.stop=time.time()
        if self.stop-self.start>5:
            self.y=bgy
            self.start=time.time()
            self.x=random.randint(1,450)
class Cone():
    def __init__(self):
        self.image=pygame.image.load("png/cone.png")
        self.image=pygame.transform.rotozoom(self.image,0,0.18)
        self.x=random.randint(1,450)
        self.y=bgy
        self.start=time.time()
        self.stop=time.time()
        self.faster=False
        self.rect=None
    def reset(self):
        self.x=random.randint(1,450)
        self.y=bgy
    def draw(self):
        self.rect=screen.blit(self.image,(self.x,self.y))
        if self.faster==True:
            self.y=self.y+3
        elif self.faster==False:
            self.y=self.y+2
        x=0
        if self.y>=600:
            self.stop=time.time()
        if self.stop-self.start>5:
            self.y=bgy
            self.start=time.time()
            self.x=random.randint(1,450)
class Gas():
    def __init__(self):
        self.image=pygame.image.load("png/Gas.png")
        self.image=pygame.transform.rotozoom(self.image,0,0.15)
        self.x=random.randint(1,450)
        self.y=bgy
        self.start=time.time()
        self.stop=time.time()
        self.faster=False
        self.rect=None
    def reset(self):
        self.x=random.randint(1,450)
        self.y=bgy
    def draw(self):
        self.rect=screen.blit(self.image,(self.x,self.y))
        if self.faster==True:
            self.y=self.y+4
        elif self.faster==False:
            self.y=self.y+2
        x=0
        if self.y>=600:
            self.stop=time.time()
        if self.stop-self.start>10:
            self.y=bgy
            self.start=time.time()
            self.x=random.randint(1,450)
        
EnemyCar=Enemy()
cone1=Cone()
car1=Car()
gas=Gas()
imageLives=pygame.image.load("png/mycar.png")
imageLives=pygame.transform.rotozoom(imageLives,0,0.05)
font=pygame.font.Font("freesansbold.ttf",32)
scoretxt=font.render("Score:%d"%score,True,(0,0,255))
pygame.mixer.music.load('Low_Life_High_Life (3).mp3')
pygame.mixer.music.play(-1)
while True:
    screen.blit(bg,(0,bgy))
    for x in range(lives,3):
        screen.blit(imageLives,(450+x*50,0))
    screen.blit(scoretxt,(0,0))
    scoretxt=font.render("Score:%d"%score,True,(0,0,255))
    car1.draw()
    EnemyCar.draw()
    gas.draw()
    cone1.draw()
    bgy=bgy+bgspeed
    if bgy>=0:
        bgy=-600
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    car1.right=1
                if event.key==K_LEFT:
                    car1.left=1
                if event.key==K_UP:
                    EnemyCar.carspeed=EnemyCar.carspeed+2
                    bgspeed=bgspeed+2
                    cone1.faster=True
            elif event.type==KEYUP:
                if event.key==K_RIGHT:
                    car1.right=0
                if event.key==K_LEFT:
                    car1.left=0
                if event.key==K_UP:
                    if bgspeed>1:
                        EnemyCar.carspeed=EnemyCar.carspeed-2
                        bgspeed=bgspeed-2
                        cone1.faster=False
                    elif bgspeed<=1:
                        bgspeed==1
    pygame.display.update()
    if car1.rect.colliderect(EnemyCar.rect):
        lives=lives+1
        if score>0:
            score=score-50
        EnemyCar.reset()
        if lives==3:
            screen.fill((0,0,0))
            font=pygame.font.Font("freesansbold.ttf",50)
            text=font.render("Game Over!",True,(0,0,255))
            screen.blit(text,(150,300))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            break
    if car1.rect.colliderect(cone1.rect):
        lives=lives+1
        if score>0:
            score=score-50
        cone1.reset()
        if lives==3:
            screen.fill((0,0,0))
            font=pygame.font.Font("freesansbold.ttf",50)
            text=font.render("Game Over!",True,(0,0,255))
            screen.blit(text,(150,300))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            break
    if car1.rect.colliderect(gas.rect):
        counter=counter+1
        if counter==2:
            lives=lives-1
            counter=0
        gas.reset()
        score=score+50
        if score==500:
            screen.fill((0,0,0))
            font=pygame.font.Font("freesansbold.ttf",50)
            text=font.render("You Win!",True,(0,0,255))
            screen.blit(text,(150,300))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            break
