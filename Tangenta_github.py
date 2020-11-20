from time import process_time
import pygame
from pygame.locals import *
import time

alphabet = "abcdefghijklmnopqrstuvwxyz"
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((800, 200))
print(pygame.font.get_fonts())


font = pygame.font.SysFont(None, 28)
font1 = pygame.font.Font("Tangenta\\UbuntuMono-R.ttf",22)

text = ''
img = font1.render(text, True, RED)

intro_text = 'To start press Enter - Make sure text is empty - Then press Enter to end.'
intro_img = font.render(intro_text, True, RED)
intro_rect = Rect(5,10,600,48)

time_text = ''
time_rect = Rect(600,150,200,48)


rect = img.get_rect()
rect.topleft = (20, 80)

cursor = Rect(rect.topright, (3, rect.height))

start_time = False
game_start = False
win = False
running = True

end_time = ""

background = BLACK

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
           
            if event.key == K_RETURN:
                if start_time == False:
                    if win == True and text != '':                        
                        f = open("stats.txt","a")
                        f.write(text + " : " + end_time + "s\n")
                        f.close()
                        intro_text = "Stats saved! Press Enter with empty text to go again!"
                        intro_img = font.render(intro_text, True, RED)
                        win = False
                    
                    t1 = time.process_time()        #If Enter is pressed, get the starting time
                    
                    if text == '':
                        intro_text = 'Game has started, write alphabet as fast as possible and press enter to end!'
                        intro_img = font.render(intro_text, True, RED)
                        start_time = True
                    
                elif start_time == True:
                    print(text)
                    print(alphabet)
                    
                    if text == alphabet:
                        print("MATCH!")
                        intro_text = "Congrats! Type your name and press enter to save stats - or press enter to go again"
                        intro_img = font.render(intro_text, True, RED)
                        win = True    
                    else:
                        intro_text = "YOU FAILED! PRESS ENTER WITH EMPTY TEXT TO TRY AGAIN!"
                        intro_img = font.render(intro_text, True, RED)
                        
                    text = ''
                    end_time = str(t2-t1)
                    print("Endtime:",end_time)
                    start_time = False
                
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += event.unicode
                
            if event.key == K_ESCAPE:
                running = False
            
            img = font1.render(text, True, GREEN)
            rect.size=img.get_size()
            cursor.topleft = rect.topright
    
    if start_time == True:
        t2 = process_time()
        time_text = str(t2 - t1)
        time_img = font.render(time_text, True, RED)
    
    
    screen.fill(background)
    screen.blit(img, rect)
    screen.blit(intro_img,intro_rect)
    
    if start_time == True:
        screen.blit(time_img,time_rect)
    
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, GRAY, cursor)
    
    pygame.display.update()

pygame.quit()