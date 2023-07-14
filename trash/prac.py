import pygame
import random
import math
from tkinter import *
import pickle
# INITIATING PYGAME
pygame.init()

# TITLE AND LOGO
#pygame.display.set_caption("BikeStorm")

#pygame.display.set_icon(pygame.image.load("Photos/icon.png"))
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

log=0
# COLOURS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (40, 161, 10)
grey = (119, 118, 110)
blue = (0, 0, 255)
magenta = (104, 19, 106)
orange = (226, 88, 34)
lightblue = (40, 108, 130)
yellow=(253,193,5)

#images
t1=pygame.image.load('Photos/track/1.png')
t2=pygame.image.load('Photos/track/2.png')
t3=pygame.image.load('Photos/track/3.png')
t4=pygame.image.load('Photos/track/4.png')
t5=pygame.image.load('Photos/track/5.png')
t6=pygame.image.load('Photos/track/6.png')
t7=pygame.image.load('Photos/track/7.png')
t8=pygame.image.load('Photos/track/8.png')
t9=pygame.image.load('Photos/track/9.png')
t10=pygame.image.load('Photos/track/10.png')
t11=pygame.image.load('Photos/track/11.png')
t12=pygame.image.load('Photos/track/12.png')

background = pygame.image.load("Photos/background1.jpg")
power = pygame.image.load("Photos/power.png")
title = pygame.image.load("Photos/title.png")
life_heart = pygame.image.load("Photos/heart.png")
bike1 = pygame.image.load("Photos/motorbike.png")
bike1 = pygame.transform.scale(bike1, (100, 100))
pointer=pygame.image.load("Photos/pointer.png")
rules = pygame.image.load("Photos/rules.jpg")
control = pygame.image.load("Photos/controls.png")

player=pygame.image.load('Photos/p1.png')
pl_left=pygame.image.load('Photos/p2.png')
pl_right=pygame.image.load('Photos/p3.png')

obs1=pygame.image.load('Photos/obs1.png')
obs2=pygame.image.load('Photos/obs2(1).png')
obs22=pygame.image.load('Photos/obs2(2).png')
#road=pygame.image.load('Photos/road_divide.png')

tr_l=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12]


# FONTS
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

#POINTER
pointer_x=0
pointer_y=0
pygame.mouse.set_visible(False)


# MUSIC
def crash():
    explosionSound = pygame.mixer.Sound("Music/crash.wav")
    explosionSound.play()


def music():
    pygame.mixer.music.load("Music/background.wav")
    pygame.mixer.music.play(-1)


def motor():
    pygame.mixer.music.load("Music/moto.wav")
    pygame.mixer.music.play(-1)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (190, 250))


def lives(x, y):
    score = font.render("LIVES: ", True, (255, 255, 255))
    screen.blit(score, (x, y))


def score(x, y, points, colour):
    score = font.render("SCORE: " + str(points), True, colour)
    screen.blit(score, (x, y))

def Message(size, mess, x_pos, y_pos, colour):

    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, colour)
    screen.blit(render, (x_pos, y_pos))


def heart(x, y):
    screen.blit(power, (x, y))


x_obs1=395
y_obs1=273
x_obs2=395
y_obs2=273
sizex2=1
sizey2=1
sizex1=1
sizey1=1


def isCollision(varA, varB, varC, varD, disx, disy):
    distancex = math.sqrt(math.pow(varA - varC, 2))
    distancey = math.sqrt(math.pow(varB - varD, 2))
    if distancex < disx and distancey < disy:
        return True
    else:
        return False
#x,y,xo,yo,sx,sy
def isCollision2(varA, varB, varC, varD, disx, disy):
    global sizex2,sizey2
    distancex = math.sqrt(math.pow(varA - varC, 2))#+sizex2
    distancey = math.sqrt(math.pow(varB - varD, 2))#+sizey2
    if distancex < disx and distancey <disy:
        return True
    else:
        return False
sco = 0

l_maxsco=[]
max_sco=0

def start():
    global obs1,obs2
    global y_obs1,y_obs2
    global x_obs1,x_obs2
    global sizex1,sizex2
    global sizey1,sizey2
    global sco
    global l_maxsco
    global max_sco
    
    i=0
    x=200
    y=417
    x_change=0
    y_change=0
    play=0
    n=0
    obs2_11=0
    r_obs=0
    count = 3
    l_sco=[]
    sco=0
    max_sco=0

    #file=open('score.txt','w+')
    while True:
        sco+=1
        
        
        #print(sco)
        
        for i in range(24):
            
            screen.blit(tr_l[i],(0,0))
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Rule3 = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause()                        
                    if event.key == pygame.K_LEFT:
                        x_change = -15
                        play=1
                    if event.key == pygame.K_RIGHT:
                        x_change = 15
                        play=2
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                        play=0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
                        play=0
                

            x += x_change
            y += y_change
            if x <= 0:
                x = 0
                
            if x >= 600:
                x = 600
            if y >= 500:
                y = 500
            if y <= 0:
                y = 0
            
                
            sizex1+=6
            sizey1+=5
            y_obs1+=2
            x_obs1-=7
            
            obs1_1=pygame.transform.scale(obs1,(sizex1,sizey1))
            obs2_1=pygame.transform.scale(obs2,(sizex2,sizey2))
                
            '''
                if play==0:
                    screen.blit(player,(x,y))
                    
                elif play==2:
                    screen.blit(pl_left,(x,y))
                   
                elif play==1:
                    screen.blit(pl_right,(x,y))
            '''
            for i in range(1):
                screen.blit(obs1_1,(x_obs1,y_obs1))
                if y_obs1>=400:
                    sizex2+=8
                    sizey2+=5
                    x_obs2+=1
                    y_obs2+=3
                    screen.blit(obs1_1,(x_obs1,y_obs1))
                    screen.blit(obs2_1,(x_obs2,y_obs2))
                    n=1
                elif n!=0:
                    sizex2+=8
                    sizey2+=5
                    x_obs2+=1
                    y_obs2+=3
                    screen.blit(obs2_1,(x_obs2,y_obs2))
                
                if play==0:
                       
                    screen.blit(player,(x,y))
                    
                elif play==2:
                       
                    screen.blit(pl_left,(x,y))
                   
                elif play==1:
                        
                       
                    screen.blit(pl_right,(x,y))
                
                    #pygame.display.update()
                
            
                if y_obs1>=800:
                    sizex1=1
                    sizey1=1
                    x_obs1=395
                    y_obs1=273
                
                if y_obs2>=700:
                    sizex2=1
                    sizey2=1
                    x_obs2=395
                    y_obs2=273

            #pygame.display.update()
            
            if y_obs1<=490:
                if isCollision(x,y+70,x_obs1-10,y_obs1+10,sizex1,sizey1):
                    sizex1=1
                    sizey1=1
                    x_obs1=395
                    y_obs1=600
                    count-=1
                    
            else:
                pass
            if y_obs2<=490:
                
                if isCollision2(x+65,y+172,x_obs2+sizex2+30,y_obs2+sizey2,sizex2,sizey2):
                    sizex2=1
                    sizey2=1
                    x_obs2=1000
                    y_obs2=600
                    #print('a')
                    count-=1
            else:
                pass
            if count >= 3:
                heart(110, 15)
                heart(145, 15)
                heart(180, 15)
            if count == 2:
                heart(110, 15)
                heart(145, 15)
            if count == 1:
                heart(110, 15)
            
            if count <= 0:
                gameover()
                
                Rule3=False
                #count2=0
            
            score(550, 10, sco, white)
            lives(10, 10)    
            l_sco.append(sco)
            #print(l_sco)
            #
            #   file.write(str(max_sco))
            i+=1
            pygame.display.update()
        
            #l_maxsco.append(max_sco)
            #print(l_maxsco)
        max_sco=max(l_sco)
        
player_name=''

def button(x_button, y_button, x, y, x_pad, y_pad, mess_b, colour, colour_hover):
    
    pygame.draw.rect(screen, white, [x_button, y_button, x, y],20,10)
    pygame.draw.rect(screen, colour, [x_button, y_button, x, y],4,4,4,4)
    
    Message(53, mess_b, x_button + x_pad, y_button + y_pad, black)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button + x and y_button < mouse[1] < y_button + y:
        pygame.draw.rect(screen, colour_hover, [x_button, y_button, x, y],20,4)
        Message(53, mess_b, x_button + x_pad, y_button + y_pad, white)

        if click == (1, 0, 0) and mess_b == "RULES":
            game_rules()
        if click == (1, 0, 0) and mess_b == "QUIT":
            quit_confirmation()

        if click == (1, 0, 0) and mess_b == "SCORES":
            scores()
        if click == (1, 0, 0) and mess_b == "YES":
        
            pygame.quit()
            quit()
        
        if click == (1, 0, 0) and mess_b == "PLAY":
            start()
        if click == (1, 0, 0) and mess_b == "CONTROLS":
            gamecontrols()
        if click==(1,0,0) and mess_b=='COLOR':
            bike_colour()
        if click==(1,0,0) and mess_b=='BACK':
            game_intro()
        if click==(1,0,0) and mess_b=='NO':
            game_intro()
        if click==(1,0,0) and mess_b=='OK':
            name()
        if click==(1,0,0) and mess_b=='LOG IN':
            game_intro()
def game_intro():
    global pointer_x
    global pointer_y
    global log
    if log==1:
        window.destroy()
        log=0
    
    #music()
    intro = False
    i = 0
    width = 800
    while intro == False:
        screen.fill(black)
        
        screen.blit(background, (i, 0))
        screen.blit(background, (width + i, 0))

        if i == -width:
            screen.blit(background, (width + i, 0))
            i = 0

        i = i - 8
        
        screen.blit(bike1, (450, 450))
        screen.blit(bike1, (370, 475))
        screen.blit(title, (43, 15))

        button(55, 200, 219, 40, 63, 5, "PLAY", blue, lightblue)
        button(55, 270, 219, 40, 46, 5, "RULES", blue, lightblue)
        button(55, 340, 219, 40, 3, 5, "CONTROLS", blue, lightblue)
        button(55, 410, 219, 40, 42, 5, "COLOR", blue, lightblue)
        button(55, 480, 219, 40, 35, 5, "SCORES", blue, lightblue)
        button(55, 540, 219, 40, 63, 5, "QUIT", magenta, red)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = True
                pygame.quit()
                quit()
            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        screen.blit(pointer,(pointer_x,pointer_y))
            
        pygame.display.update()


'''
def name():
    global player_name
    global pointer_x
    global pointer_y
    
    
    input_box = pygame.Rect(340, 85, 140, 40)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                done = True
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if input_box.collidepoint(event.pos):
                    
                    active = not active
                else:
                    active = False
                
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        
                        player_name=text
                        print(player_name)
                        if text=='':
                            no_name_entered()
                        
                        else:
                            player_name=text
                            text = ''
                            start()
                        
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        
                    else:
                        text += event.unicode
                        if len(text)>15:
                            limit_exceeded()
                else:
                    text_box_not_selected()

            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        
        screen.blit(pointer,(pointer_x,pointer_y))
        
        screen.fill((100, 200, 30))
        button(5, 550, 119, 40, 8, 5, "BACK", black, black)
        txt_surface = font.render(text, True, color)
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        #Message(100,str(sco_max),0,0,black)
        pygame.draw.rect(screen, color, input_box, 2)
        Message(25,'ENTER NAME OF THE PLAYER',83,90,black)
        Message(20,'(LIMIT : 15 words)',83,110,red)
        Message(20,'PRESS ENTER TO CONTINUE',600,580,black)
        screen.blit(pointer,(pointer_x,pointer_y))

        pygame.display.update()

def no_name_entered():
    global player_name
    global pointer_x
    global pointer_y
    
    
    input_box = pygame.Rect(340, 85, 140, 40)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                done = True
                pygame.quit()
                quit()
            

            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        
        screen.fill((100, 200, 30))
        pygame.draw.rect(screen, white, [205, 200, 425,190])
        pygame.draw.rect(screen, blue, [200, 200, 435,190],15,10)
        button(360,325, 90, 40, 17, 5, "OK",magenta , magenta)
        
        Message(35,'PLEASE ENTER A NAME',265,235,black)
               
        
        txt_surface = font.render(text, True, color)
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        
        pygame.draw.rect(screen, color, input_box, 2)
        Message(25,'ENTER NAME OF THE PLAYER',83,90,black)
        Message(20,'PRESS ENTER TO CONTINUE',600,580,black)
       
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()

        
def limit_exceeded():
    global player_name
    global pointer_x
    global pointer_y
    
    input_box = pygame.Rect(340, 85, 140, 40)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                done = True
                pygame.quit()
                quit()
            

            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        
        screen.fill((100, 200, 30))
        pygame.draw.rect(screen, white, [205, 200, 425,190])
        pygame.draw.rect(screen, blue, [200, 200, 435,190],15,10)
        button(360,325, 90, 40, 17, 5, "OK",magenta , magenta)
        
        Message(35,'LIMIT OF 15 WORDS EXCEEDED',230,235,black)
               
        
        txt_surface = font.render(text, True, color)
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        
        pygame.draw.rect(screen, color, input_box, 2)
        Message(25,'ENTER NAME OF THE PLAYER',83,90,black)
        Message(20,'PRESS ENTER TO CONTINUE',600,580,black)
       
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()


        
def text_box_not_selected():
    global player_name
    global pointer_x
    global pointer_y
    
    input_box = pygame.Rect(340, 85, 140, 40)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                done = True
                pygame.quit()
                quit()
            

            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        
        screen.fill((100, 200, 30))
        pygame.draw.rect(screen, white, [205, 150, 425,250])
        pygame.draw.rect(screen, blue, [200, 150, 435,260],15,10)
        button(355, 340, 90, 40, 17, 5, "OK",magenta , magenta)
        
        Message(50,'TEXT BOX NOT ',279,200,black)
        Message(50,'SELECTED',320,250,black)
        
        
        txt_surface = font.render(text, True, color)
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        
        pygame.draw.rect(screen, color, input_box, 2)
        Message(25,'ENTER NAME OF THE PLAYER',83,90,black)
        
        Message(20,'PRESS ENTER TO CONTINUE',600,580,black)
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()
'''


def game_rules():
    global pointer_x
    global pointer_y
    j = 0
    width = 800
    rule = True
    
    while rule:

        screen.blit(background, (j, 0))
        screen.blit(background, (width + j, 0))
        if j == -width:
            screen.blit(background, (width + j, 0))
            j = 0
        j = j - 1
        screen.blit(rules, (15, 75))
        button(650, 550, 119, 40, 8, 5, "BACK", black, black)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rule = False
            if event.type == pygame.QUIT:
                rule = False
                pygame.quit()
                quit()
            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()

def scores():
    global pointer_x
    global pointer_y
    global max_sco
    global player_name
    j = 0
    width = 800
    rule = True
    file=open('score.txt','r+')
    file2=open('playername.txt','r+')
    score_l=eval(file.read())
    pl_name=eval(file2.read())
    file.close()
    file2.close()
    
    for i in score_l:
        #print(i)
        #print(max_sco)
        if i==max_sco:
            break
        if i<max_sco:
            score_l.remove(score_l[len(score_l)-1])
            pl_name.remove(pl_name[len(score_l)])
            print(pl_name)
            i=max_sco
            score_l.append(i)
            

            score_l.sort(reverse=True)
            
            place=score_l.index(max_sco)
            pl_name.insert(place,player_name)
            break
    
        
    #print(score_l)
    

    while rule:

        screen.blit(background, (j, 0))
        screen.blit(background, (width + j, 0))
        if j == -width:
            screen.blit(background, (width + j, 0))
            j = 0
        j = j - 1
        
        Message(130,'SCORES',200,30,black)
        Message(80,'1. '+str(score_l[0]),30,150,black)
        Message(80,'2. '+str(score_l[1]),30,210,black)
        Message(80,'3. '+str(score_l[2]),30,290,black)
        Message(80,'4. '+str(score_l[3]),30,360,black)
        Message(80,'5. '+str(score_l[4]),30,440,black)
        Message(80,':'+str(pl_name[0]),200,150,black)
        Message(80,':'+str(pl_name[1]),200,210,black)
        Message(80,':'+str(pl_name[2]),200,290,black)
        Message(80,':'+str(pl_name[3]),200,360,black)
        Message(80,':'+str(pl_name[4]),200,440,black)
        file=open('score.txt','w')
        file.write(str(score_l))
        file.close()

        file3=open('playername.txt','w')
        file3.write(str(pl_name))
        file3.close()
        
        button(650, 550, 119, 40, 8, 5, "BACK", black, black)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rule = False
            if event.type == pygame.QUIT:
                rule = False
                pygame.quit()
                quit()
            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()

def gamecontrols():
    global pointer_x
    global pointer_y
    j = 0
    width = 800
    controls = True
    
    while controls:

        screen.blit(background, (j, 0))
        screen.blit(background, (width + j, 0))
        if j == -width:
            screen.blit(background, (width + j, 0))
            j = 0
        j = j - 1
        screen.blit(control, (12, 100))
        button(650, 550, 119, 40, 8, 5, "BACK", black, black)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controls = False
                    
            if event.type == pygame.QUIT:
                controls = False
                pygame.quit()
                quit()
            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()

def pause():
    global sco
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_r:
                    sco = 0
                    count2=0
                    start()
                elif event.key == pygame.K_m:
                    sco = 0
                    count2=0
                    game_intro()
        screen.fill(white)
        Message(100, 'Paused', 250, 100, black)
        Message(45, "Press 'c' to continue", 50, 300, blue)
        Message(45, "Press 'r' to restart the game", 50, 350, blue)
        Message(45, "Press 'm' to go to main menu", 50, 400, blue)
        pygame.display.update()
        clock.tick(5)


#def Message(size, mess, x_pos, y_pos, colour):
        
def quit_confirmation():
    global pointer_x
    global pointer_y
    j = 0
    width = 800
    confirm = True
    
    while confirm:

        screen.blit(background, (j, 0))
        screen.blit(background, (width + j, 0))
        if j == -width:
            screen.blit(background, (width + j, 0))
            j = 0
        j = j - 1
        pygame.draw.rect(screen, white, [205, 130, 425,325])
        pygame.draw.rect(screen, blue, [200, 130, 435,335],15,10)
        button(275, 350, 90, 40, 8, 5, "YES", green, green)
        button(475, 350, 90, 40, 20, 5, "NO", red, red)
        Message(50,'DO YOU REALLY WANT',219,200,black)
        Message(50,'TO QUIT??',320,250,black)
       
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controls = False
                    
            if event.type == pygame.QUIT:
                controls = False
                pygame.quit()
                quit()
            pointer_x,pointer_y=pygame.mouse.get_pos()
            pointer_x-=pointer.get_width()-41
            pointer_y-=pointer.get_height()-35
        screen.blit(pointer,(pointer_x,pointer_y))
        pygame.display.update()


def gameover():
    global sco
    global count2
    over = True
    
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    sco = 0
                    count2=0
                    start()
                    

                elif event.key == pygame.K_m:
                    sco = 0
                    count2=0
                    game_intro()
        screen.fill(white)
        Message(100, 'GAME OVER', 200, 100, black)
        score(300, 200, sco, black)
        #shot_count(270,250,count2,black)
       
        Message(45, "Press 'r' to restart the game", 50, 350, blue)
        Message(45, "Press 'm' to go to main menu", 50, 400, blue)
        pygame.display.update()
        clock.tick(5)


entry1=''
entry2=''
en1=''
en2=''
en3=''
en4=''
in_text=''
dic={}
window=''
def getTextInput1():
    global dic,window
    global player_name
    found=False
    in_text=entry1.get()
    in_text2=entry2.get()
    if in_text!='' and in_text2!='':
        file=open('subscription.dat','rb')
        try:
            while True:
                dic2=pickle.load(file)
                player_name=dic2[in_text][1]
                if in_text in dic2 and dic2[in_text][0]==in_text2:
                    #game_intro()
                    found=True
                    game_intro()

                
        except EOFError:
            file.close()
        if found==False:
            popup3()
    else:
        popup4()

new_window=''

def popup2():
    msg2=Toplevel(window)
    msg2.geometry('250x150')
    lbl1=Label(msg2,text='Password does not match',font=('Helvetica',15))
    lbl1.pack(pady=10)
    btn1=Button(msg2,text='OK',command=lambda: [msg2.destroy()])
    btn1.pack(pady=10)
def popup3():
    msg3=Toplevel(window)
    msg3.geometry('250x150')
    lbl1=Label(msg3,text='Please enter password or',font=('Helvetica',15))
    lbl1.pack()
    lbl2=Label(msg3,text='UserID correctly',font=('Helvetica',15))
    lbl2.pack()
    lbl3=Label(msg3,text='OR make a new account',font=('Helvetica',15))
    lbl3.pack()
    btn1=Button(msg3,text='OK',command=lambda: [msg3.destroy()])
    btn1.pack(pady=10)

def popup4():
    msg4=Toplevel(window)
    msg4.geometry('250x150')
    lbl1=Label(msg4,text='Text Box Is Empty',font=('Helvetica',15))
    lbl1.pack(pady=10)
    btn1=Button(msg4,text='OK',command=lambda: [msg4.destroy()])
    btn1.pack(pady=10)

l_user=[]
def popup1():
    global dic,new_window
    global l_user   
    l_user=[]

    in_text=en1.get()
    in_text2=en2.get()
    in_text3=en3.get()
    in_text4=en4.get()

    if in_text3==in_text4:
        l_user.append(in_text3)
        l_user.append(in_text2)
        msg=Toplevel(window)

        msg.geometry('250x150')
        lbl1=Label(msg,text='New account created',font=('Helvetica',15))
        lbl1.pack(pady=10)
        btn1=Button(msg,text='OK',command=lambda: [new_window.destroy(),msg.destroy()])
        btn1.pack(pady=10)

        #dic[in_text]=l_user
        file=open('subscription.dat','rb')
        
        try:
            while True:
                dic=pickle.load(file)
                #print(dic)
        except EOFError:
            file.close()
        #file.close()

        dic[in_text]=l_user
        file2=open('subscription.dat','wb')
        pickle.dump(dic,file2)
        #file2.write(str(dic))
        #window.destroy()
        file2.close()
    else:
        popup2()



def signup():
    global new_window
    global en1,en2,en3,en4
    new_window=Toplevel(window)
    new_window.geometry('800x600')
    new_window.resizable(0,0)
    new_window.title('SIGN UP')
    
    lbll=Label(new_window,text='USER ID',fg='red',font=('Helvetica',15),justify='left')
    lbll.place(x=200,y=100)
    
    lbl2=Label(new_window,text='USERNAME',fg='red',font=('Helvetica',15))
    lbl2.place(x=200,y=150)
    
    lbl3=Label(new_window,text='PASSWORD',fg='red',font=('Helvetica',15))
    lbl3.place(x=200,y=200)

    lbl4=Label(new_window,text='CONFIRM PASSWORD',fg='red',font=('Helvetica',15))
    lbl4.place(x=200,y=250)
    
    en1=Entry(new_window)
    en1.place(x=300,y=95,height=30)
    
    en2=Entry(new_window)
    en2.place(x=330,y=145,height=30)
    
    en3=Entry(new_window)
    en3.place(x=330,y=195,height=30)
    
    en4=Entry(new_window)
    en4.place(x=430,y=245,height=30)
    
    btn1=Button(new_window,text='close',command=lambda: new_window.destroy())
    btn1.place(x=200,y=400)  
    
    btn2=Button(new_window,text='create',command=popup1)
    btn2.place(x=300,y=400)  
    '''
    btn2=Button(new_window,text='create',command=popup1)
    btn2.place(x=300,y=400)  
    '''

    #print(in_text)

def login():
    global log
    global entry1
    global entry2,window
    global in_text


    window=Tk()
    window.geometry('800x600')
    window.resizable(0,0)
    window.title('LOGIN')
    log=1

    label=Label(window,text='USER ID',fg='red',font=('Helvetica',15),justify='left')
    label.place(x=220,y=180)
    labe2=Label(window,text='PASSWORD',fg='red',font=('Helvetica',15))
    labe2.place(x=220,y=230)
    entry1=Entry(window)
    entry1.place(x=320,y=175,height=30)
    #a=entry1.get('1.0','end')
    
    entry2=Entry(window)
    entry2.place(x=350,y=225,height=30)
    but1=Button(window,text='LOGIN',command=getTextInput1)
    but1.place(x=430,y=300)
    #print(in_text)
  
    but2=Button(window,text='Create an account',command=signup)
    but2.place(x=250,y=300)
        
    
    
    
    window.mainloop()
    
login()  

#start()

pygame.quit()
quit()
