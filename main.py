import pygame 
import sys
from setting import WIDTH, HEIGHT,cell_size
from setting import BLACK ,FPS,GREY
from world import World


update_count = 0
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

TITLE = "SAND"
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
last_time = pygame.time.get_ticks()
update_interval = 1000/150 # update _below will run 33.33ms per frame
accumulator = 0


running = True

wld = World(SCREEN)

# fill world function will out of game loop
wld.fill_world()

row_mouse = 0 # temporary value to make them used out if condition
col_mouse = 0# same as row_mouse
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get mouse  psoition 
    mouse_x,mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:

        col_mouse = mouse_x // cell_size
        row_mouse = mouse_y//cell_size

    # from here put update functions
        wld.update(row_mouse,col_mouse) 
    
    current_time = pygame.time.get_ticks()
    delta_time = current_time - last_time
    last_time = current_time

    accumulator += delta_time

    while accumulator >= update_interval: 
        wld.update_sandbelow()
        accumulator -= update_interval

    if current_time - start_time >= 1000:
        start_time = current_time
    



    SCREEN.fill(GREY) # from here after screen put function for drwaing
    #start here 
    wld.draw_sand()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()