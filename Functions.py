from turtle import width
import playsound
import pygame

def play_mp3(mp3_file):
    playsound(mp3_file)

def list_create(list_contents):
    list = [list_contents]
    print(list)

def pygame_win(window_name):
    import pygame 
    pygame.init()
    var = pygame.display.set_mode((500,600))
    pygame.display.set_caption('{window_name}')
    running = True
    while running:
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
      if running == False:
       pygame.quit()