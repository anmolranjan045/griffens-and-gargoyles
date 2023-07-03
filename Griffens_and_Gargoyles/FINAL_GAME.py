import pygame, sys, time, random
from pygame.locals import *

pygame.init()

pygame.mixer.init()

width = 800
height = 600

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption('GRIFFENS AND GARGOYALES')

#music = pygame.mixer.music.load('"D:\Laptop Back up\anmol\ANMOL_FINAL GAME_DONE\WONDER WOMAN Theme Music Batman v Superman OST Hans Zimmer & Junkie XL HD.mp3"')
#pygame.mixer.music.play(-1)

sound = pygame.mixer.Sound('glock18-1.wav')

# importing PICS
bg = pygame.image.load('Capture.GIF')
bg = pygame.transform.scale(bg,(width, height))
pause = pygame.image.load('Capture_1.PNG')
pause = pygame.transform.scale(pause,(width, height))
open_imag = pygame.image.load('CROPPED GRIFFIN.png')
open_imag = pygame.transform.scale(open_imag,(width,height))
load_imag = pygame.image.load('menu_1.GIF')
load_imag = pygame.transform.scale(load_imag,(width,height))
menu_play = pygame.image.load('menu_2.GIF')
menu_play = pygame.transform.scale(menu_play,(width,height))
menu_highscore = pygame.image.load('menu_3.GIF')
menu_highscore = pygame.transform.scale(menu_highscore,(width,height))
menu_instrustions = pygame.image.load('menu_4.GIF')
menu_instrustions = pygame.transform.scale(menu_instrustions ,(width,height))
menu_quit = pygame.image.load('menu_5.GIF')
menu_quit = pygame.transform.scale(menu_quit,(width,height))
game_over = pygame.image.load('GAME_OVER.png')
game_over = pygame.transform.scale(game_over,(width,height))
instructions = pygame.image.load('INSTRUCTION.PNG')
instructions = pygame.transform.scale(instructions,(width, height))
how_to_play = pygame.image.load('HOW TO PLAY.PNG')
how_to_play = pygame.transform.scale(how_to_play,(width, height))
high_ = pygame.image.load('chaos-knight-nessaj-dota-2-hd-wallpaper-1366x768.jpg')
high_ = pygame.transform.scale(high_,(width, height))

run = True
game = True
play = False
clock = pygame.time.Clock()
FPS = 27
score = 0
paused = False
add_new_alpha = 8
inst__ = False
high_score = 0

al_a = pygame.image.load('A.png')
al_b = pygame.image.load('B.png')
al_c = pygame.image.load('C.png')
al_d = pygame.image.load('D.png')
al_e = pygame.image.load('E.png')
al_f = pygame.image.load('F.png')
al_g = pygame.image.load('G.png')
al_h = pygame.image.load('H.png')
al_i = pygame.image.load('I.png')
al_j = pygame.image.load('J.png')
al_k = pygame.image.load('K.png')
al_l = pygame.image.load('L.png')
al_m = pygame.image.load('M.png')
al_n = pygame.image.load('N.png')
al_o = pygame.image.load('O.png')
al_p = pygame.image.load('P.png')
al_q = pygame.image.load('Q.png')
al_r = pygame.image.load('R.png')
al_s = pygame.image.load('S.png')
al_t = pygame.image.load('T.png')
al_u = pygame.image.load('U.png')
al_v = pygame.image.load('V.png')
al_w = pygame.image.load('W.png')
al_x = pygame.image.load('X.png')
al_y = pygame.image.load('Y.png')
al_z = pygame.image.load('Z.png')

alpha = []   # y coordinate
alpha_2 = []  # x coordinate
alpha_4 = []  # appends images to blit randomly
check = 0   # to check no alphabets not missed
alpha_3 = [pygame.image.load('B.png'), pygame.image.load('A.png'), pygame.image.load('C.png'), pygame.image.load('D.png'), pygame.image.load('E.png'), pygame.image.load('F.png'), pygame.image.load('G.png'), pygame.image.load('H.png'), pygame.image.load('I.png'), pygame.image.load('J.png'), pygame.image.load('K.png'), pygame.image.load('L.png'), pygame.image.load('M.png'), pygame.image.load('N.png'), pygame.image.load('O.png'), pygame.image.load('P.png'), pygame.image.load('Q.png'), pygame.image.load('R.png'), pygame.image.load('S.png'), pygame.image.load('T.png'), pygame.image.load('U.png'), pygame.image.load('V.png'), pygame.image.load('W.png'), pygame.image.load('X.png'),pygame.image.load('Y.png'), pygame.image.load('Z.png')]
alpha_5 = [al_b, al_a, al_c, al_d, al_e, al_f, al_g, al_h, al_i, al_j, al_k, al_l, al_m, al_n, al_o, al_p, al_q, al_r, al_s, al_t, al_u, al_v, al_w, al_x, al_y, al_z]
alpha_6 = []

Aqua   =    (0, 255, 255) 
Black  =  (0,   0,   0) 
Blue    =   (0,   0, 255) 
Fuchsia =   (255,   0, 255) 
Gray    =   (128, 128, 128) 
Green   =   (0, 128,   0) 
Lime    =   (0, 255,   0) 
Maroon   =  (128,   0,   0) 
NavyBlue  =  (0,   0, 128) 
Olive    =  (128, 128,   0) 
Purple  =   (128,   0, 128) 
Red     =   (255,   0,   0) 
Silver   =  (192, 192, 192) 
Teal  =     (0, 128, 128) 
White  =    (255, 255, 255) 
Yellow  =   (255, 255,   0)

# importing text
first_font = pygame.font.Font("HTOWERTI.TTF",45)

inst_1 = first_font.render("Press Enter to Continue",True, Black)
inst_2 = first_font.render("Press Enter to Continue",True, Yellow)
inst_3 = first_font.render("Press Enter to Know How to Play",True, Yellow)
inst_4 = first_font.render("Press Enter to Go Back",True, Maroon)
inst_5 = first_font.render("Press Enter to Return",True, NavyBlue)


font = pygame.font.SysFont('comicsans', 30, True, True)
font_1 = pygame.font.SysFont('comicsans', 50, True, True)
font_2 = pygame.font.SysFont('comicsans', 80, True, True)
font_3 = pygame.font.SysFont('comicsans', 250,True)


while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_RETURN:
                inst__ = True

    while inst__:
        surface.fill(White)
        surface.blit(instructions, (0,0))
        surface.blit(inst_2, (width//4-40,height//2+250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    inst__ = False
                    run = False
    surface.fill(White)
    surface.blit(open_imag, (0,0))
    surface.blit(inst_1, (width//4,height//2+200))
    pygame.display.update()


def highscore_(high_score):
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    run = False
        surface.fill(White)
        surface.blit(high_, (0,0))

        if score > high_score:
            highscore_file = open('HIGHSCORE.txt',"w")#w for write
            highscore_file.write(str(score))
            highscore_file.close()
            highscore_file = open('HIGHSCORE.txt',"r")#r for reading
            highscore_int = int(highscore_file.read())
            text_2 = font_2.render('The Highest Score is', 1, (Yellow))
            text_3 = font_3.render(str(highscore_int), 1, (Teal ))
            surface.blit(text_2, (50, 150))
            surface.blit(text_3, (203,303))
            
        else:
            highscore_file = open('HIGHSCORE.txt',"r")#r for reading
            highscore_int = int(highscore_file.read())
            text_2 = font_2.render('The Highest Score is', 1, (Yellow))
            text_3 = font_3.render(str(highscore_int), 1, (Teal ))
            surface.blit(text_2, (50, 150))
            surface.blit(text_3, (203,303))
            

        surface.blit(inst_5, (width//4,height//2+200))
        pygame.display.update()


def how_to():
    global inst__
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    inst__ = True

        surface.fill(White)
        surface.blit(instructions, (0,0))
        surface.blit(inst_3, (width//4-80,height//2+250))
        pygame.display.update()

        while inst__:
            surface.fill(White)
            surface.blit(how_to_play, (0,0))
            surface.blit(inst_4, (width//4-40,height//2+250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYUP:
                    if event.key == K_RETURN:
                        inst__ = False
                        run = False
            pygame.display.update()


class moving_man(object):
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    char = pygame.image.load('standing.png')
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 4
        self.rou = 0

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

        if self.walkCount  >= 27:
            self.walkCount = 0

        if self.x > 753:
            self.rou += 1


def game_display(image_1):
    surface.fill(White)
    surface.blit(image_1,(0,0))
    pygame.display.update()


def make_new(alpha, alpha_2):
    alpha.append(0)
    x_quad = random.randint(1, 800-64)
    alpha_2.append(x_quad)
    return alpha, alpha_2


def check_new(alpha):
    a = len(alpha)
    if a == 0:
        alpha = make_new(alpha)
    else:
        b = alpha[a]
        if b >= 50:
            alpha = make_new(alpha)
    return alpha


def move_forward(alpha):
    for i in range(len(alpha)):
        alpha[i] += 1
    return alpha
    

def leave():
    pygame.quit()
    sys.exit()


def make_new(alpha,alpha_2,alpha_3,alpha_4):
    alpha.append(0)
    x_quad = random.randint(1, 800-64)
    alpha_2.append(x_quad)
    a=len(alpha_3)
    b=random.randint(0,a-1)
    c=alpha_3[b]
    alpha_4.append(c)
    c=alpha_5[b]
    alpha_6.append(c)
    return alpha, alpha_2,alpha_4


def check_new(alpha,alpha_2,alpha_4):
    a = len(alpha)
    if a == 0:
        alpha,alpha_2,alpha_4 = make_new(alpha,alpha_2,alpha_3,alpha_4)
    else:
        b = alpha[a-1]
        if b >= 50:
            alpha,alpha_2,alpha_4 = make_new(alpha,alpha_2,alpha_3,alpha_4)
    return alpha,alpha_2,alpha_4


def move_forward(alpha):
    for i in range(len(alpha)):
        alpha[i] += 2       #for increasing speed increase this
    return alpha


def delete(alpha,alpha_2,alpha_4,check):
    j = 0
    check_1 = check
    for i in range(len(alpha)):
        i = i-j
        if alpha[i] >= 508-64:
            alpha.pop(i)
            alpha_2.pop(i)
            alpha_4.pop(i)
            alpha_6.pop(i)
            j += 1
            check_1 += 1
        return alpha,alpha_2,alpha_4,check_1


def redrawGamewindow(alpha,alpha_2,bg,surface,alpha_4):
    surface.blit(bg, (0,0))
    for i in range(len(alpha_4)):
        surface.blit(alpha_4[i],(alpha_2[i],alpha[i]))
    man_run.draw(surface)
    text = font.render('Rounds Complete: ' + str(man_run.rou) , 1, (Red ))
    surface.blit(text, (500,10))
    text_1 = font.render('Score: ' + str(score) , 1, (Red ))
    surface.blit(text_1, (500,50))
    text_2 = font_1.render('Pause', 1, (Yellow))
    surface.blit(text_2, (10,10))
    text_3 = font.render('Fall Count: '+ str(check), 1, (Red))
    surface.blit(text_3, (500,90))
    pygame.display.update()


def for_pause(image_1):
    paused = True

    while paused:
        surface.fill(White)
        surface.blit(image_1,(0,0))
        x,y = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if x>=277 and y>=186 and x<=488 and y<=243:
                if event.type == pygame.MOUSEBUTTONUP:
                    return

            elif x>=211 and y>=299 and x<=554 and y<=357:
                if event.type == pygame.MOUSEBUTTONUP:
                    how_to()

            elif x>=322 and y>=411 and x<=432 and y<=478:
                if event.type == pygame.MOUSEBUTTONUP:
                    check = 0
                    man_run.rou = 0
                    score = 0
                    alpha.clear()
                    alpha_6.clear()
                    alpha_4.clear()
                    alpha_2.clear()
                    main_menu()
        pygame.display.update()


man_run = moving_man(1, 445, 64, 64, 750)


def play_now():
    global alpha,alpha_2,alpha_4,check,score,event
    play = True
    score = 0
    check = 0

    while play:     # main game loop
        clock.tick(FPS)
        if check >= 10:
                surface.blit(game_over, (0,0))
                if score > high_score:
                    highscore_file = open('HIGHSCORE.txt',"w") #w for write
                    highscore_file.write(str(score))
                    highscore_file.close()
                pygame.display.update()
                time.sleep(1)
                check = 0
                man_run.rou = 0
                score = 0
                alpha.clear()
                alpha_6.clear()
                alpha_4.clear()
                alpha_2.clear()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                play = False

            x,y = pygame.mouse.get_pos()

            if x>=14 and y>=14 and x<=124 and y<=38:
                if event.type == pygame.MOUSEBUTTONUP:
                        for_pause(pause)
               
            if event.type == KEYUP:

                if event.key == K_SPACE and man_run.rou >= 5:
                    man_run.rou -= 5
                    alpha.clear()
                    alpha_6.clear()
                    alpha_4.clear()
                    alpha_2.clear()
                    time.sleep(0.50)

                elif event.key == K_a :
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_a:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            score += 3
                            x+=1
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_a and len(alpha_6)-1 == s:
                            score -=1
                            
                elif event.key == K_b:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_b:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            score += 3
                            x+=1
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_b and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_c:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_c:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_c and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_d:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_d:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_d and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_e:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_e:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_e and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_f:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_f:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_f and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_g:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_g:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_g and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_h:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_h:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_h and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_i:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_i:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_i and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_j:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_j:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_j and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_k:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_k:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_k and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_l:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_l:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_l and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_m:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_m:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_m and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_n:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_n:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_n and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_o:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_o:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_o and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_p:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_p:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_p and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_q:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_q:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_q and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_r:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_r:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_r and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_s:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_s:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_s and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_t:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_t:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_t and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_u:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_u:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_u and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_v:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_v:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_v and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_w:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_w:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_w and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_x:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_x:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_x and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_y:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_y:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_y and len(alpha_6)-1 == s:
                            score -=1

                elif event.key == K_z:
                    x=0
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] == al_z:
                            alpha_6.pop(s)
                            alpha_4.pop(s)
                            alpha.pop(s)
                            alpha_2.pop(s)
                            x+=1
                            score +=3
                            #pygame.mixer.Sound.play(sound)
                            break
                    for s in range(0,len(alpha_6)):
                        s=s-x
                        if alpha_6[s] != al_z and len(alpha_6)-1 == s:
                            score -=1

        alpha,alpha_2,alpha_4 = check_new(alpha,alpha_2,alpha_4)
        alpha = move_forward(alpha)
        redrawGamewindow(alpha,alpha_2,bg,surface,alpha_4)
        alpha,alpha_2,alpha_4,check = delete(alpha,alpha_2,alpha_4,check)
        pygame.display.update()
    pygame.quit()
    sys.exit()  


def main_menu():
    surface.fill(Black)
    game_display(load_imag)
    waiting = True
    while waiting:
        x,y = pygame.mouse.get_pos()
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif x>=242 and y>=49 and x<=596 and y<=144:
                game_display(menu_play)
                if event.type == pygame.MOUSEBUTTONUP:
                    play_now()

            elif x>=235 and y>=173 and x<=613 and y<=268:
                game_display(menu_highscore)
                if event.type == pygame.MOUSEBUTTONUP:
                    highscore_(high_score)

            elif x>=192 and y>=305 and x<=657 and y<=400:
                game_display(menu_instrustions)
                if event.type == pygame.MOUSEBUTTONUP:
                    how_to()

            elif x>=260 and y>=436 and x<=582 and y<=532:
                game_display(menu_quit)
                if event.type == pygame.MOUSEBUTTONUP:
                    leave()

            else :
                game_display(load_imag)

main_menu()