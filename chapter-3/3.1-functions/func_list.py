import random

class Ball:
    def __init__(self):
        self.motion = None

def pass_ball(ball):
    ball.motion = 'flying' 

def shoot(ball):
    ball.motion = 'floating'

def dribble(ball):
    ball.motion = 'bouncing'

triple_threat = [pass_ball, shoot, dribble,]
orange = Ball()

triple_threat[random.randint(0,2)](orange)

print(orange.motion)