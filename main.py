import pygame 

pygame.init()
WIDTH= 1050
HEIGHT=1050
screen= pygame.display.seet_mode(WIDTH, HEIGHT)
font= pygame.font.Font('freesansbold.ttf', 20)
big_font= pygame.font.Font('freesansbold.ttf', 50)
timer= pygame.time.Clock()
fps= 60

#game variables 