import pygame
pygame.init()
import random
import os
pygame.mixer.init()



# 1) colors
white = (255, 255, 255)
red = (255, 0, 0)
darkred =(139, 0, 0)
black = (0, 0, 0)
green = ( 0, 128, 0)
gray = (128,128,128)
yellow = (128, 128, 0)
pink = (255, 153, 204)
darkblue = (0,0,128)
purple =(128,0,128)
indigo =(75,0,130)
violet = (148,0, 211)
orange = (255, 127, 0)
silver = (192, 192, 192)


# 2) creating window
screen_width = 900
screen_height = 600 
gamewindow = pygame.display.set_mode((screen_width, screen_height))

# 3) background img
bgimg = pygame.image.load("snake7.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()


# 4) game title
pygame.display.set_caption(" Snake City ")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)


# 5) screen 

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

    with open("heighscore", "r") as f:
        heighscore = f.read()



# 6) welcome function 

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(darkblue)
        text_screen("{Snake City-Game}", red, 330, 220)
        text_screen(" Press Enter to Start ", white, 210, 190)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   pygame.mixer.music.load('on&on.mp3')
                   pygame.mixer.music.play() 
                   gamelopp()

        pygame.display.update()
        clock.tick(60)        



# 7) game loop 
def gamelopp():
    
    # 7.a) Game spcification variables

    exit_game = False
    game_over = False
    snake_x = 20
    snake_y = 20
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    heighscore = 500
    food_x = random.randint(15,screen_width/2)
    food_y = random.randint(15, screen_height/2)
    score = 0
    init_velocity = 3
    snake_size = 15
    fps = 15


    if (not os.path.exists("hieighscore.txt")):
        with open("heighscore.txt","w") as f:
            f.write("0")

# 8) function 

    while not exit_game:

        if game_over :

            with open("heighscore", "w") as f:
                f.write(str(heighscore))
            gamewindow.fill(indigo)
            text_screen("Game Over", white, 350, 250)  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0         

                    if event.key == pygame.K_LEFT:
                        velocity_x = - 10
                        velocity_y = 0             

                    if event.key == pygame.K_UP:
                        velocity_y = - 10
                        velocity_x = 0 
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y =  10
                        velocity_x = 0 

                    if event.key == pygame.K_q:
                        score +=10

                    if event.key == pygame.K_q:
                        score +=5


            snake_x = snake_x + velocity_x          
            snake_y = snake_y + velocity_y          

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 15
                food_x = random.randint(4, screen_width / 2)
                food_y = random.randint(4, screen_height / 2)
                snk_length  +=1
                if score > int(heighscore):
                    heighscore = score


            gamewindow.fill(indigo)
            gamewindow.blit(bgimg, (0,0))
            text_screen("Score: "+ str(score) +" Heighscore: "+str(heighscore) , white, 3, 3)
            pygame.draw.rect(gamewindow, orange, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
  
            if head in snk_list[: -1]:
                game_over = True
                pygame.mixer.music.load('Roman.mp3')
                pygame.mixer.music.play()
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('Roman.mp3')
                pygame.mixer.music.play()

            plot_snake (gamewindow, silver, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit ()
    quit()
welcome()



