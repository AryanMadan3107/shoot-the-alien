import pgzrun
import random

WIDTH=800
HEIGHT=400

a = Actor("alien")
a.x = 400
a.y = 200
msg = "Catch the alien!"
score=0

def draw():
    screen.fill("purple")
    a.draw()
    screen.draw.text(msg,center=(400,50))
    screen.draw.text("score: "+str(score),center=(100,50))
    if msg=="Good shot!":
        screen.fill("green")
        a.draw()
        screen.draw.text(msg,center=(400,50))
        screen.draw.text("score: "+str(score),center=(100,50))
    else:
        screen.fill("red")
        a.draw()
        screen.draw.text(msg,center=(400,50))
        screen.draw.text("score: "+str(score),center=(100,50))
    
def on_mouse_down(pos):
    global msg,score
    if a.collidepoint(pos):
        a.x=random.randint(50,750)
        a.y=random.randint(50,350)
        msg="Good shot!"
        score+=1
    else:
        msg="Next time hit the alien not air!"
        score-=1

pgzrun.go()