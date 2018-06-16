import pygame, random, time

pygame.init() #initializes the game

#---Color Settings---
white = (255,255,255) #theese are RGB color things
green = (0,255,0)
blue = (0,0,255)
black= (0,0,0)
red=(255,0,0)
pink=(255,102,255)
orange= (255,153,51)

#---Basic Settings---
screen = pygame.display.set_mode((800,600)) #game window dimensions
screen_rect=screen.get_rect()
pygame.display.set_caption('Shape Friends')#game name
clock=pygame.time.Clock() #chooses the FPS
gameExit=False #when to end game

#---Font Settings---
myfont=pygame.font.SysFont(None, 35) 
smallfont=pygame.font.SysFont(None, 24)
agency=pygame.font.SysFont("agencyfb", 35)
#---Block and Gravity Settings---
block_x, block_y = 390, 200 
block_x_change, block_y_change=0,0
block_gravity =-8
double=True
speed=0.4

#---Platform Settings---
plat_x=0
plat_y=random.randint(175, 375)
plat1_x=155
plat1_y=random.randint(175, 375)
plat2_x=310
plat2_y=random.randint(175, 375)
plat3_x=465
plat3_y=random.randint(175, 375)
plat4_x=620
plat4_y=random.randint(175, 375)
plat5_x=775
plat5_y=random.randint(175, 375)

#---Loves Health Settings---
loves_hp=100
if loves_hp>=67:
    life_color=green
if 67>loves_hp>=33:
    life_color=orange
if 33>loves_hp:
    life_color=red

#---Drawing Rectangles---
plat=pygame.draw.rect(screen, black, (plat_x, plat_y, 150, 10))
plat1=pygame.draw.rect(screen, black, (plat1_x, plat1_y, 150, 10))
plat2=pygame.draw.rect(screen, black, (plat2_x, plat2_y, 150, 10))
plat3=pygame.draw.rect(screen, black, (plat3_x, plat3_y, 150, 10))
plat4=pygame.draw.rect(screen, black, (plat4_x, plat4_y, 150, 10))
plat5=pygame.draw.rect(screen, black, (plat5_x, plat5_y, 150, 10))
block=pygame.draw.rect(screen, black, (block_x, block_y, 10,10))
ground=pygame.draw.rect(screen, red, (0,450, 800,150))
loves_block_back=pygame.draw.rect(screen, black, (27, 7, 206, 26))
loves_block=pygame.draw.rect(screen, life_color, (30,10, loves_hp*2, 20))

#---Loading Images---
button_up=pygame.image.load("Button_up.png").convert_alpha()
button_down=pygame.image.load("Button_down.png").convert_alpha()

rock_pic=pygame.image.load("rock.png").convert_alpha()
lips=pygame.image.load("lips.png").convert_alpha()
tree_pic=pygame.image.load("tree.png").convert_alpha()
seed_pic=pygame.image.load("seed.png").convert_alpha()

background=pygame.image.load("background.png").convert()
lava=pygame.image.load("lava.png").convert()
loves_pic=pygame.image.load("Loves.png").convert_alpha()

arrows=pygame.image.load("arrows.png").convert_alpha()
title=pygame.image.load("Title.png").convert_alpha()
platform=pygame.image.load("platform.png").convert_alpha()

player_happy_right=pygame.image.load("player_happy_right.png").convert_alpha()
player_happy_left=pygame.image.load("player_happy_left.png").convert_alpha()
player_sad_right=pygame.image.load("player_sad_right.png").convert_alpha()
player_sad_left=pygame.image.load("player_sad_left.png").convert_alpha()

guy_open=pygame.image.load("Guy_open.png").convert_alpha()
guy_close=pygame.image.load("Guy_close.png").convert_alpha()

eye=pygame.image.load("Eye_pic.png").convert_alpha()
hat=pygame.image.load("Hat.png").convert_alpha()
spikes=pygame.image.load("Spikes.png").convert_alpha()

win=pygame.image.load("win.png").convert_alpha()
retry_up=pygame.image.load("Restart_up.png").convert_alpha()
retry_down=pygame.image.load("Restart_down.png").convert_alpha()
gameover=pygame.image.load("gameover.png").convert_alpha()
quit_up=pygame.image.load("Quit_up.png").convert_alpha()
quit_down=pygame.image.load("Quit_down.png").convert_alpha()

story=pygame.image.load("Story.png").convert_alpha()
lava=pygame.image.load("lava.png").convert_alpha()
#---Assigning Rects to Images---
rock=rock_pic.get_rect()
rock_x=710
rock_y=-100
rock.top=rock_y
rock.left=rock_x
tree=tree_pic.get_rect()
tree_x=0
tree_y=-100
tree.top=tree_y
tree.left=tree_x
seed=seed_pic.get_rect()
seed_x=random.randint(200,600)
seed_y=-100
seed.top=seed_y
seed.left=seed_x
eye_x=720
eye_y=60

#---Assigning Variables
keys = pygame.key.get_pressed() #checks if key was pressed
level=1                     #what level the player is currently on
num=2                       #changes the speed of the platforms
next_level=False            #checks if the player has made it to the next level
click=False                 #if click, normal jump
on=False                    #this is to check if it is on platform
lose=False                  #checks if the player has lost
spawn=True                  #spawns the player in the proper location (in the middle of the second platform)
loop=True                   #ensures that a varibale is only reset once
first=True                  #ensures the rock does not deal more damage than it is supposed to
near=False                  #stops the firing of the rocks if player is near mouth
play_pressed=False          #activates when the player clicks on a button
cursor_over=False           #checks if the cursor if over the play button
mouse_click=False           #checks if the player has clicked the mouse
right=True                  #checks the direction the player is moving 
hit=False                   #checks if the player has been hit 
sad_counter=0               #timer of sad player after being hit
life_counter=0              #delay between life drops
life_drop=False             #activates the life drop
tree_down=False             #checks if seed has been planted in the platform
first_drop=True             #makes sure the seed drops only once
second_jump=False           #activates the double jump
jump_count=False            #ensures that you can only double jump once
once=True                   #activates the jump only once
rock_cycle=0                #delay between rock firings
restart_pressed=False       #checks if the restart button has been pressed
cursor_over_retry=False     #checks if the cursor is over the retry button
cursor_over_quit=False      #checks if the cursor is over the quit button
first_rock=True             #ensures the rock only changes y value once
opening=True                #loops in the opening scene
title_x=-700                #title c coordinate
timer=0                     #timer to track your score
#---Blitting Starting Images---
screen.blit(background, (0,0))
screen.blit(lava, (0,450))
#---Open Scene Loop---
while opening:
    screen.blit(background, (0,0))
    screen.blit(lava, (-9,441))
    screen.blit(title, (title_x,200))
    if title_x<80:
        title_x+=3
    else:
        time.sleep(3)
        opening=False
    clock.tick(60)
    pygame.display.update()
    
    
#---Starting Menu Loop---
while not play_pressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True
                play_pressed=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click=True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click=False
    if keys[pygame.K_SPACE]:
        mouse_click=True
    screen.blit(background, (0,0))
    screen.blit(lava, (-9,441))
    mouse_pos=pygame.mouse.get_pos()
    screen.blit(story, (35,40))
    screen.blit(arrows, (375, 40))

    if 318<mouse_pos[0]<500 and 412<mouse_pos[1]<545:
        cursor_over=True
    else:
        cursor_over=False
    if cursor_over:
        screen.blit(button_down, (310, 400))
    else:
        screen.blit(button_up, (319, 410))

    if cursor_over and mouse_click:
        play_pressed=True
        game_Exit=False
        
    pygame.display.update()
    
#---Main Game Loop---
while not gameExit: #unless gameExit is true
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True

    #---Player Movement Controls---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        block_x_change=-4
        right=False
    if keys[pygame.K_RIGHT]:
        if on:
            block_x_change=4+num
        else:
            block_x_change=4
        right=True

    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_SPACE or event.key==pygame.K_UP:
            click=True
            if jump_count:
                second_jump=True
                jump_count=False
    if event.type == pygame.KEYUP:
        if event.key==pygame.K_SPACE and click and once:
            jump_count=True
            once=False
        if event.key==pygame.K_UP and click and once:
            jump_count=True
            once=False

    #---Initiating Jump---
    if click:
        if not on and firstloop:
            block_gravity=-8
            firstloop=False
        block_gravity+=speed
        block_y_change+=block_gravity

    if second_jump:
        block_gravity=-8
        second_jump=False
        
    if not on and not click:
        if loop:
            block_gravity=0
            loop=False
        block_gravity+=speed
        block_y_change+=block_gravity    
    
    #---Landing on Platforms---
    if block.colliderect(plat) or block.colliderect(plat1) or block.colliderect(plat2) or block.colliderect(plat3) or block.colliderect(plat4) or block.colliderect(plat5):
        click=False
        second_jump=False
        jump_count=False
        once=True
        if block.colliderect(plat):
            block_y=plat_y-24
        elif block.colliderect(plat1):
            block_y=plat1_y-24
        elif block.colliderect(plat2):
            block_y=plat2_y-24
        elif block.colliderect(plat3):
            block_y=plat3_y-24
        elif block.colliderect(plat4):
            block_y=plat4_y-24
        elif block.colliderect(plat5):
            block_y=plat5_y-24
        block_gravity=-8
        on=True
        loop=True
        firstloop=True
    else:
        on=False

    if on:
        block_x-=num

    #---Platform Cycle---
    if plat_x<=-150:
        plat_x=800
        plat_y=random.randint(250, 350)
        
    elif plat1_x<=-150:
        plat1_x=800
        plat1_y=random.randint(250, 350)
    
    elif plat2_x<=-150:
        plat2_x=800
        plat2_y=random.randint(250, 350)
        
    elif plat3_x<=-150:
        plat3_x=800
        plat3_y=random.randint(250, 350)

    elif plat4_x<=-150:
        plat4_x=800
        plat4_y=random.randint(250, 350)

    elif plat5_x<=-150:
        plat5_x=800
        plat5_y=random.randint(250, 350)

    #---Seed Falling Delay---
    life_counter+=1
    if life_counter>=600:
        life_drop=True
        life_counter=0
        
    #---Dropping Seed---
    if life_drop:
        if first_drop:
            seed_x=random.randint(300, 400)
            seed_y=0
        seed_y+=4

    #---Growing Tree---
    if seed.colliderect(plat) or seed.colliderect(plat1) or seed.colliderect(plat2) or seed.colliderect(plat3) or seed.colliderect(plat4) or seed.colliderect(plat5):
        tree_down=True
        if seed.colliderect(plat):
            tree_y=plat_y-40
        elif seed.colliderect(plat1):
            tree_y=plat1_y-40
        elif seed.colliderect(plat2):
            tree_y=plat2_y-40
        elif seed.colliderect(plat3):
            tree_y=plat3_y-40
        elif seed.colliderect(plat4):
            tree_y=plat4_y-40
        elif seed.colliderect(plat5):
            tree_y=plat5_y-40
        seed_y=-100
        life_drop=False
        tree_x=seed_x-45
        first_drop=False

    if block.colliderect(tree) or tree_x<-100:
        first_drop=True
        tree_y=-100
        tree_x=50
        tree_down=False
    else:
        first_drop=False

    if tree_down:
        tree_x-=num
        
    #---Rock Cycle---
    if rock.colliderect(block) or rock_x<-80:
        rock_x=720
        rock_y=-100
        rock_cycle=0
        first_rock=True
    if rock_cycle>=60:
        if first_rock:
            rock_y=block_y-10
            first_rock=False
        rock_x-=10
    rock_cycle+=1.4
        
    
    #---Getting Lives---
    if block.colliderect(tree):
        loves_hp+=20
        if loves_hp>80:
            loves_hp=100
        tree_y=-100
        tree_down=False
        life_drop=False

    #---Losing Lives---
    if block.colliderect(rock):
        hit=True
        if first:
            loves_hp-=20
            first=False
            if not near:
                rock_x=710
            else:
                rock_x=-100
    if loves_hp<=0 or block.colliderect(ground) or block_x<=20:
        lose=True
        if block_x<=20:
            lose=True
            block_x=20
    else:	
        first=True

    loves_hp-=0.1
                                                
    block_x+=block_x_change
    block_y+=block_y_change

    block_x_change=0
    block_y_change=0

    #---Moving Along With Platforms---
    plat_x-=num
    plat1_x-=num
    plat2_x-=num
    plat3_x-=num
    plat4_x-=num
    plat5_x-=num

    rock.top=rock_y
    rock.left=rock_x
    tree.top=tree_y
    tree.left=tree_x
    seed.top=seed_y
    seed.left=seed_x
    
    #---Sad Duration---
    if hit:
        sad_counter+=1
    if sad_counter>=75:
        sad_counter=0
        hit=False

    
    #---Advancing to the Next Level---
    if block_x>=700 and 150<block_y<350:
        rock_x=720
        rock_y=-100
        level+=1
        num+=0.75
        block_x_change, block_y_change=0,0
        block_gravity =-8
        speed=0.4
        tree_y=-100
        plat_x=0
        plat_y=random.randint(175, 375)
        plat1_x=155
        plat1_y=random.randint(175, 375)
        plat2_x=310
        plat2_y=random.randint(175, 375)
        plat3_x=465
        plat3_y=random.randint(175, 375)
        plat4_x=620
        plat4_y=random.randint(175, 375)
        plat5_x=775
        plat5_y=random.randint(175, 375)
        spawn=True      #spawns on first platform
        click=False     #if click, normal jump
        on=True   #this is to check if it is on platform
        next_level=True
        first_rock=True
        rock_cycle=0
        right=True
        if loves_hp>70:
            loves_hp=100
        else:
            loves_hp+=30

    #---Losing Settings---
    while lose:
        cursor_over_retry=False
        cursor_over_quit=False
        mouse_click=False
        while not restart_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                        pygame.quit
                        quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click=True
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click=False
            screen.blit(background, (0,0))
            mouse_pos=pygame.mouse.get_pos()
            screen.blit(gameover, (50, 50))
            if 118<mouse_pos[0]<300 and 372<mouse_pos[1]<505:
                cursor_over_retry=True
                cursor_over_quit=False
            else:
                cursor_over_retry=False
            if cursor_over_retry:
                screen.blit(retry_down, (110, 360))
            else:
                screen.blit(retry_up, (119, 370))

            if cursor_over_retry and mouse_click:
                restart_pressed=True
                game_Exit=False

            if 518<mouse_pos[0]<700 and 372<mouse_pos[1]<505:
                cursor_over_quit=True
                cursor_over_retry=False
            else:
                cursor_over_quit=False
            if cursor_over_quit:
                screen.blit(quit_down, (510, 360))
            else:
                screen.blit(quit_up, (519, 370))

            if cursor_over_quit and mouse_click:
                pygame.quit()
                quit()
	
            pygame.display.update()

        if restart_pressed:
            block_x_change, block_y_change=0,0
            block_gravity =0
            speed=0.4
            rock_x=710
            tree_y=-100
            plat_x=0
            plat_y=random.randint(175, 375)
            plat1_x=155
            plat1_y=random.randint(175, 375)
            plat2_x=310
            plat2_y=random.randint(175, 375)
            plat3_x=465
            plat3_y=random.randint(175, 375)
            plat4_x=620
            plat4_y=random.randint(175, 375)
            plat5_x=775
            plat5_y=random.randint(175, 375)
            lose=False
            spawn=True      #spawns on first platform
            click=False     #if click, normal jump
            on=False        #this is to check if it is on platform
            level=1
            num=2
            loves_hp=100
            first=True
            rock_cycle=0
            first_rock=True
            right=True
            timer=0
            restart_pressed=False

    #---Winning Settings---
    timer+=1
    while level>=10:
        cursor_over_retry=False
        cursor_over_quit=False
        mouse_click=False
        while not restart_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                        pygame.quit
                        quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click=True
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click=False
            screen.blit(background, (0,0))
            screen.blit(lava, (-9,441))
            mouse_pos=pygame.mouse.get_pos()
            screen.blit(win, (100, 20))
            end_time=agency.render("It took you %r seconds to save your shape friends!"%(int(timer/60)),1,black)
            screen.blit(end_time, (135, 300))
            if 118<mouse_pos[0]<300 and 372<mouse_pos[1]<505:
                cursor_over_retry=True
                cursor_over_quit=False
            else:
                cursor_over_retry=False
            if cursor_over_retry:
                screen.blit(retry_down, (110, 360))
            else:
                screen.blit(retry_up, (119, 370))

            if cursor_over_retry and mouse_click:
                restart_pressed=True
                game_Exit=False

            if 518<mouse_pos[0]<700 and 372<mouse_pos[1]<505:
                cursor_over_quit=True
                cursor_over_retry=False
            else:
                cursor_over_quit=False
            if cursor_over_quit:
                screen.blit(quit_down, (510, 360))
            else:
                screen.blit(quit_up, (519, 370))

            if cursor_over_quit and mouse_click:
                pygame.quit()
                quit()
	
            pygame.display.update()

        if restart_pressed:
            block_x_change, block_y_change=0,0
            block_gravity =0
            speed=0.4
            rock_x=710
            tree_y=-100
            plat_x=0
            plat_y=random.randint(175, 375)
            plat1_x=155
            plat1_y=random.randint(175, 375)
            plat2_x=310
            plat2_y=random.randint(175, 375)
            plat3_x=465
            plat3_y=random.randint(175, 375)
            plat4_x=620
            plat4_y=random.randint(175, 375)
            plat5_x=775
            plat5_y=random.randint(175, 375)
            lose=False
            spawn=True      #spawns on first platform
            click=False     #if click, normal jump
            on=False        #this is to check if it is on platform
            level=1
            num=2
            loves_hp=100
            first=True
            timer=0
            right=True
            restart_pressed=False
        
    #---Spawning---
    if spawn:
        block_x, block_y=plat1_x+60, plat1_y-24
        spawn=False
        
    #---Blitting Everything---    
    screen.fill(white)
    screen.blit(background, (0,0))
    screen.blit(lava, (-9,441))
    
    plat=pygame.draw.rect(screen, black, (plat_x, plat_y, 150, 10))
    plat1=pygame.draw.rect(screen, black, (plat1_x, plat1_y, 150, 10))
    plat2=pygame.draw.rect(screen, black, (plat2_x, plat2_y, 150, 10))
    plat3=pygame.draw.rect(screen, black, (plat3_x, plat3_y, 150, 10))
    plat4=pygame.draw.rect(screen, black, (plat4_x, plat4_y, 150, 10))
    plat5=pygame.draw.rect(screen, black, (plat5_x, plat5_y, 150, 10))
    
    screen.blit(platform, (plat_x-1, plat_y-2))
    screen.blit(platform, (plat1_x-1, plat1_y-2))
    screen.blit(platform, (plat2_x-1, plat2_y-2))
    screen.blit(platform, (plat3_x-1, plat3_y-2))
    screen.blit(platform, (plat4_x-1, plat4_y-2))
    screen.blit(platform, (plat5_x-1, plat5_y-2))
    
    #---Loves Health Settings---
    if loves_hp>=67:
        life_color=green
    if 67>loves_hp>=33:
        life_color=orange
    if 33>loves_hp:
        life_color=red
    loves_block_back=pygame.draw.rect(screen, black, (27, 57, 206, 26))
    loves_block=pygame.draw.rect(screen, life_color, (30,60, loves_hp*2, 20))
    meter=agency.render("Health", 1, black)
    screen.blit(meter, (95, 15))
    screen.blit(rock_pic, (rock_x, rock_y))
    if block_x>=550:
        screen.blit(guy_open, (700,0))
        near=True
    else:
        screen.blit(guy_close, (700,0))
        near=False

    screen.blit(eye, (eye_x, eye_y))

    block=pygame.draw.rect(screen, red, (block_x,block_y, 25,25))
    if right:
        if 1<sad_counter<75:
            screen.blit(player_sad_right, (block_x-1,block_y-2))
        else:
            screen.blit(player_happy_right,(block_x-1,block_y-2))
    if not right:
        if 1<sad_counter<75:
            screen.blit(player_sad_left,(block_x-1,block_y-2))
        else:
            screen.blit(player_happy_left,(block_x,block_y-2))
    screen.blit(hat, (block_x-15, block_y-22))
    
    screen.blit(lava, (0,450))
    score_text=myfont.render("LEVEL %r"%(level), 1, black)
    screen.blit(score_text, (350, 10))
    screen.blit(tree_pic, (tree_x, tree_y))
    screen.blit(seed_pic, (seed_x, seed_y))
    loves_num=smallfont.render("%r/100"%(int(loves_hp)),1,white)
    screen.blit(loves_num, (100,63))
    screen.blit(spikes, (0,0))
    play_time=agency.render("Time: %r"%(int(timer/60)),1,black)
    screen.blit(play_time, (700, 5))
    pygame.display.update() #updates the display
    #---Next Level Pause---
    if next_level:
        time.sleep(1)
        next_level=False
    clock.tick(60) #frames per second
pygame.quit()
quit()
