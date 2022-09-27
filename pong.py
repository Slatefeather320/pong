import pygame, random, sys
window = pygame.display.set_mode((1000,700))
pygame.init()
pygame.display.set_caption('EPIC PONGERS')

class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xsize = 20
        self.ysize = 200

class ball():
    def __init__(self):
        self.x = 500
        self.y = 350
        self.vx = 0.5
        self.vy = 0
        self.colour = (255,255,255)

font = pygame.font.Font("C:\Windows\Fonts\8514oem.fon",20)
text = font.render("TEMPORARY",True,(255,255,255))
score = 0


player = paddle(100,150)
enemy = paddle(900, 250)
ball = ball()

def drawframe():
    window.fill((0,0,0))
    pygame.draw.rect(window,(255,255,255),(player.x, player.y, player.xsize, player.ysize))
    pygame.draw.rect(window, (255,255,255), (enemy.x, enemy.y, enemy.xsize, enemy.ysize))
    pygame.draw.circle(window, ball.colour, (ball.x, ball.y), 30)
    window.blit((text),(20,20))
    pygame.display.update()

def movepaddle():
    #moves player paddle
    mousepos = pygame.mouse.get_pos()
    player.y = mousepos[1] - (player.ysize/2)

    #moves enemy paddle
    if ball.y > (enemy.y + enemy.ysize/2):
        enemy.y += 0.3
    if ball.y < (enemy.y + enemy.ysize/2):
        enemy.y -= 0.3

def ballphysics():
    global score

    #mover
    ball.x += ball.vx
    ball.y += ball.vy

    #paddle colisions
    if ball.x > (enemy.x - 30) and ball.y < enemy.y + enemy.ysize and ball.y > enemy.y:
        ball.vx = -1 * abs(ball.vx) - 0.01
        ball.vy += random.randint(0,10)/50
    if ball.x < (player.x + 30) and ball.y < player.y + player.ysize and ball.y > player.y:
        ball.vx = abs(ball.vx) + 0.01
        ball.vy += random.randint(0,10)/50
        score += 1
    
    #resetter
    if ball.x > 900 or ball.x < 100:
        pygame.time.delay(1000)
        ball.x = 500
        ball.y = 350
        ball.vx = 0.5
        ball.vy = 0
        score = 0
    
    #side colisions 
    if ball.y + 30 > 700:
        ball.vy = abs(ball.vy) * -1
    if ball.y - 30 < 0:
        ball.vy = abs(ball.vy)
    
    #rounder
    ball.vx = round(ball.vx,2)

def updatescore():
    global text, score
    scoretext = str("score: " + str(score))
    text = font.render(scoretext,True,(255,255,255))     

#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    

   #main game loop
   
   drawframe()
   movepaddle()
   ballphysics()
   updatescore()
