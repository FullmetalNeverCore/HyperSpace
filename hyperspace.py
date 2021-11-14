import pygame as pg 
import random 
import math 
res = w,h = 1600,900
n_star = 4000
vec,vec2 = pg.math.Vector2,pg.math.Vector3 
center = vec(w//2,h//2)
clrs = 'blue magenta purple cyan'.split()
z_dis = 40 
alph=50
class SR:
    def __init__(self,app):
        self.screen = app.screen
        self.pos = self.get_pos()
        self.vel = random.uniform(0.05,0.25)
        self.color = random.choice(clrs)
        self.screen_pos = vec(0,0)
        self.size = 3 
    def get_pos(self,scale_pos=15): 
        ang = random.uniform(0,2*math.pi)
        rad = random.randrange(h//scale_pos,h)*scale_pos
        x = rad*math.sin(ang)
        y = rad*math.cos(ang)
        return vec2(x,y,z_dis)
    def update(self):
        self.pos.z -= self.vel 
        self.pos = self.get_pos() if self.pos.z < 1 else self.pos 
        self.screen_pos = vec(self.pos.x,self.pos.y)/self.pos.z + center
        self.size = (z_dis - self.pos.z)/(0.2*self.pos.z)
        self.pos.xy = self.pos.xy.rotate(0.2)
        m_pos = center - vec(pg.mouse.get_pos())
        self.screen_pos += m_pos 
    def draw(self):
        pg.draw.rect(self.screen,self.color,(*self.screen_pos,self.size,self.size))


class SRfield: 
    def __init__(self,app): 
        self.sr = [SR(app) for x in range(n_star)]

    def run(self):
        [x.update() for x in self.sr]
        self.sr.sort(key=lambda star:star.pos.z,reverse=True)
        [y.draw() for y in self.sr]
class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res) 
        self.alph_sur = pg.Surface(res)
        self.alph_sur.set_alpha(alph)
        self.clock = pg.time.Clock()
        self.srf = SRfield(self) 
    def run(self): 
        while True: 
            #self.screen.fill('black')
            self.screen.blit(self.alph_sur,(0,0)) 
            self.srf.run()
            pg.display.flip()
            [exit() for x in pg.event.get() if x.type == pg.QUIT]
            self.clock.tick(60) 
if __name__ == '__main__':
    app = App() 
    app.run()

    