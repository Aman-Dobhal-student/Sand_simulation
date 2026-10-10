import pygame
from setting import cell_size
from setting import WIDTH ,HEIGHT



class World:
    def __init__(self,screen):
        self.screen = screen
        self.no_row = HEIGHT//10
        self.no_col = WIDTH//10
        self.grid = []

    def fill_world(self):
        for row in range(self.no_row):
            self.grid.append([])
            for col in range(self.no_col):
                self.grid[row].append(0)  # storing the world dat


    def update(self,row_mouse,col_mouse):
        if row_mouse < self.no_row and row_mouse > -1:
            if col_mouse < self.no_col and col_mouse >-1: 
                self.grid[row_mouse][col_mouse] = 1
                
    def converter(self,row,col):
        screen_x = col * cell_size
        screen_y = row*cell_size
        return screen_x,screen_y

    

    
    def draw_sand(self):
        

         
        for row in range(self.no_row):
             for col in range(self.no_col):

                 if self.grid[row][col] == 1:
                    screen_pos = self.converter(row,col)
                    
                    pygame.draw.rect(self.screen,(255,255,255),(screen_pos[0],screen_pos[1],10,10))
                     
                    pass


 