import pgzrun
import random

WIDTH=800
HEIGHT=400

r = Actor("rat")
r.x = 400
r.y = 200
msg = "Catch the rat!"
hit=0
miss=0

def draw():
    screen.fill("purple")
    r.draw()
    screen.draw.text(msg,center=(400,50))
    screen.draw.text("hit: "+str(hit),center=(100,50))
    screen.draw.text("miss: "+str(miss),center=(100,30))
    if msg=="Good shot!":
        screen.fill("green")
        r.draw()
        screen.draw.text(msg,center=(400,50))
        screen.draw.text("hit: "+str(hit),center=(100,50))
        screen.draw.text("miss: "+str(miss),center=(100,30))
    else:
        screen.fill("red")
        r.draw()
        screen.draw.text(msg,center=(400,50))
        screen.draw.text("hit: "+str(hit),center=(100,50))
        screen.draw.text("miss: "+str(miss),center=(100,30))
    
def on_mouse_down(pos):
    global msg,hit,miss
    if r.collidepoint(pos):
        r.x=random.randint(50,750)
        r.y=random.randint(50,350)
        msg="Good shot!"
        hit+=1
    else:
        msg="Next time hit the rat not air!"
        miss+=1

pgzrun.go()