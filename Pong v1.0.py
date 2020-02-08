from math import *
import pygame
from random import *

pygame.init()

winwidth,winheight,rackwidth,rackheight,radius = 1300,650,26,130,24

xrack,x2rack= 0, winwidth-rackwidth

x2=990
frames = 80

clock = pygame.time.Clock()
win= pygame.display.set_mode((winwidth,winheight))



def drawings():

    racket1 = pygame.draw.rect(win, (255, 255, 255), (xrack, p.yrack, rackwidth, rackheight))
    racket2 = pygame.draw.rect(win, (255, 255, 255), (x2rack, p.y2rack, rackwidth, rackheight))
    ball = pygame.draw.circle(win, (255,0,0), (p.xball, p.yball), radius, 0)
    pygame.display.update()
    win.fill((0, 0, 0))

class Pong():
    Launch = False      # launching the ball
    xball = winwidth//2
    yball = winheight//2
    yrack = winheight // 2 - rackheight // 2
    y2rack = winheight // 2 - rackheight // 2

    # coordinates for the left racket
    xracktopleft, yracktopleft = rackwidth, 0
    yrackbottomleft = 0 +rackheight

    # coordinates for the right racket
    yracktopright = 0
    yrackbottomright = 0+rackheight

    vel = 6
    speed = 8
    i = 0
    j = 0
    neg = 1
    angle = radians(45)   # starting angle
    def IA(self):

        if 0 <= self.y2rack <= winheight - rackheight and self.xball > winwidth /2 :
            if self.yrackbottomright < self.yball :
                self.y2rack += self.vel
            elif self.yracktopright > self.yball :
                self.y2rack -= self.vel
        else:
            if self.y2rack +rackheight/2 < winheight/2 - self.vel:
                self.y2rack += self.vel
            elif self.y2rack+rackheight/2 > winheight/2 + self.vel:
                self.y2rack -= self.vel
    def random_angle(self):
        list = [120,135,150,210,225,240,60,30,-60,-30,45,-45]
        #list = [30,45,60,120,135,150,210,225,240,300,315,330]    # making a random angle starting left or right
        self.angle = radians(choice(list))    # choosing left or right
    def collisions(self):
        self.xball += int(self.speed * cos(self.angle))
        self.yball += int(self.speed * sin(self.angle))

        #call IA
        self.IA()

        #rackets hitbox:
        if self.yrackbottomleft >= self.yball >= self.yracktopleft  \
                and radius + self.xracktopleft >= self.xball >= self.xracktopleft:
            self.angle = pi - self.angle
        if self.yrackbottomright >= self.yball >= self.yracktopright  \
                and x2rack >= self.xball >= x2rack - radius:
            self.angle = pi - self.angle

        # EACH CORNER : bottom right/ bottom left / top right/ top left
        if winheight - radius <= self.yball \
                and winwidth - radius <= self.xball \
                or winheight - radius <= self.yball \
                and self.xball <= 0 + radius \
                or self.yball <= 0 + radius \
                and winwidth - radius <= self.xball \
                or self.yball <= 0 + radius \
                and self.xball <= 0 + radius:
            self.angle += pi

        # top and bottom wall
        elif winheight - radius <= self.yball or self.yball <= 0 + radius:
            self.angle = -1 * self.angle

        # left and right wall
        elif winwidth - radius <= self.xball or self.xball <= 0 + radius:
            self.angle = pi - self.angle
            self.xball = winwidth // 2
            self.yball = winheight // 2
            self.random_angle()


    def running(self):      #the loop of pygame
        #vel of the rackets
        run = True
        while run :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.Launch = True      #pressing space to start


            if 0<= self.yrack <= 1000-rackheight:

                if keys[pygame.K_UP] and self.yrack > self.vel:
                    self.yrack -= self.vel
                if keys[pygame.K_DOWN] and self.yrack < winheight -rackheight - self.vel:
                    self.yrack += self.vel

                self.yrackbottomleft = self.yrack + rackheight
                self.yracktopleft = self.yrack



            self.yrackbottomright = self.y2rack + rackheight
            self.yracktopright = self.y2rack

            if self.Launch:
                self.collisions()





            clock.tick(frames)
            drawings()
        pygame.quit()

p = Pong()
p.running()
