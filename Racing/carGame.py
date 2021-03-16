import pygame
import time
import random



pygame.init()

# Sound
# crash_sound
pygame.mixer.music.load("Deep_State_Vans_in_Japan.wav")



display_width = 800
display_height = 800
border_width = 40

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
gred = (0,100,100)
blue = (0,0,255)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 103
car_height = 200

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Hamza Racing')
clock = pygame.time.Clock()

carImgage = pygame.image.load('racecar.png')

pygame.display.set_icon(carImgage)

pause = False

thingsColor = (0,0,0)







def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged  "+str(count), True,black)
    gameDisplay.blit(text,(border_width,0))



#######
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#######


def car(x,y):
    gameDisplay.blit(carImgage,(x,y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont("comicsansms", 100)             #Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText, red)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    #pygame.display.update()

    #time.sleep(2)

    #game_loop()
    
    

def crash():
    pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(crash_sound)
    message_display('Crashed')

    while True:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()

          button("Continue",200,400,100,50,green,bright_green,game_loop)
          button("Quit",500,400,100,50,red,bright_red, game_quit)

          pygame.display.update()
          clock.tick(15)          



def button(msg,x,y,w,h,icolor,acolor,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolor,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, icolor,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)



def game_quit():
    pygame.quit()
    quit()


def unpaused():
    global pause

    pygame.mixer.music.unpause()
    pause = False
	

def paused(): 

    pygame.mixer.music.pause()  

    largeText = pygame.font.SysFont("comicsansms", 80) #Font("freesansbold.ttf",80)
    TextSurf, TextRect = text_objects("Paused", largeText, black)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    #pause = True
    while pause:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

         #gameDisplay.fill(white)

         #mouse = pygame.mouse.get_pos()

         button("Continue",200,400,100,50,green,bright_green,unpaused)
         button("Quit",500,400,100,50,red,bright_red, game_quit)

         pygame.display.update()
         clock.tick(15)


def game_intro():
    intro = True
    while intro:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

         gameDisplay.fill(white)
         largeText = pygame.font.Font("freesansbold.ttf",80)
         TextSurf, TextRect = text_objects("Hamza Racing", largeText, black)
         TextRect.center = ((display_width/2),(display_height/3))
         gameDisplay.blit(TextSurf, TextRect)

         mouse = pygame.mouse.get_pos()

         button("Start",200,400,100,50,green,bright_green,game_loop)
         button("Quit",500,400,100,50,red,bright_red, game_quit)

         pygame.display.update()
         clock.tick(15)


    
def game_loop():

    global pause
    global thingsColor

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.65)

    x_change = 0
######
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(border_width, display_width-thing_width-border_width)
    thing_starty = -600
    thing_speed = 5

    dodged = 0

######
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_SPACE:
                    #print('space pressed')
                    pause = True
                    paused()

                if event.key == pygame.K_DOWN:
                    if dodged > 0:
                       dodged += -1
                       thing_speed += -1 

                if event.key == pygame.K_UP:
                    dodged += 1
                    thing_speed += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

     ##########
     ####
        things(0, 0, border_width, display_height, red)                           # Left red border
        things(display_width-border_width, 0, border_width, display_height, red)  # right red border
        
        #Road paint  3 pieces
        things(display_width/2, thing_starty, 20, display_width/3, gred)                                   
        things(display_width/2, thing_starty+display_height/3+display_height/3, 20, display_width/3, gred) 
        things(display_width/2, thing_starty-display_height/3-display_height/3, 20, display_width/3, gred)

     ####
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, thingsColor)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
     ##########
        if x > display_width - car_width - border_width or x < border_width:
            crash()

        if thing_starty > display_height:
            # Change obstacle color randomly
            R = random.randrange(10,200)
            G = random.randrange(10,200)
            B = random.randrange(10,200)
            thingsColor = (R,G,B)

            thing_starty = 0 - thing_height
            thing_startx = random.randrange(border_width,display_width-border_width-car_width)
            dodged += 1
            thing_speed += 1
            thing_width += 2
        
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx+thing_width or x < thing_startx and x+car_width > thing_startx:
                crash()   
        
        pygame.display.update()
        clock.tick(60)




game_intro()
game_loop()
pygame.quit()
quit()
