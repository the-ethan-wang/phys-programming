import random
from pathlib import Path
import pygame, os


pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
running = True
bg = "#27187E"
fg = "#F38375"

root=Path(__file__).resolve().parent
particle = os.path.join(root, "particle.png")
p_surface=pygame.image.load(particle).convert_alpha()

my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Particle sim', False, fg)

def handle_collisions(particles, time, last_hit):
    for i, p1 in enumerate(particles):
        if time-last_hit[i]<20:
            continue
        for j, p2 in enumerate(particles[i+1:]):
            if time-last_hit[j]<20:
                continue
            if (p2[0]-p1[0])**2+(p2[1]-p1[1])**2<=128:
                print(p1, p2)
                last_hit[i]=time
                last_hit[j]=time
                particles[i][2],particles[j][2]=particles[j][2],particles[i][2]
                particles[i][3],particles[j][3]=particles[j][3],particles[i][3]
                break
    return last_hit

def run_physics(particle):
    x,y,vx,vy=particle
    if x<8 and vx<0 or x>WIDTH-8 and vx>0:
        vx*=-1
    if y<8 and vy<0 or y>HEIGHT-9 and vy>0:
        vy*=-1
    y+=vy/6
    x+=vx/6
    particle[0]=x
    particle[1]=y
    particle[2]=vx
    particle[3]=vy
    return particle

def get_random_particle(max_speed=10):
    return [random.random()*WIDTH, random.random()*HEIGHT, random.random()**0.5*max_speed*random.choice([-1,1]), random.random()**0.5*max_speed*random.choice([-1,1])]

particles = [get_random_particle() for i in range(20)]
mytime=0
last_hit = [0 for i in range(20)]

while running:
    mytime+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
    screen.fill(bg)

    last_hit = handle_collisions(particles, mytime, last_hit)

    for i, particle in enumerate(particles):
        run_physics(particle)
        screen.blit(p_surface, ((particle[0], particle[1])))

    screen.blit(text_surface, ((WIDTH-text_surface.get_width())//2, 100))
    pygame.display.flip()

    clock.tick(360) 

pygame.quit()