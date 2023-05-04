#Imports
import pygame
import modules.Tetris_Board as TBd
import modules.Tetris_Other as TO
import time
import keyboard as k
from random import randint as r

#NOTES---

#ALL SHAPES WILL BE NUMBERD FROM LEFT TO RIGHT, BOTTOM TO TOP BASED ON THE IMAGE IN THE EXTRA FOLDER
#ALL THE SHAPES ROTATE CLOCKWISE

#NOTES---

#Global variable for the color
block_color = 0

#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def draw_shape(dimensions, locations, color, canvas):
    
    #Decide on the border color based on the shapes color
    if color == (0,0,0): border_color = (0,0,255)
    else: border_color = (0,0,0)
    
    #Based on the locations, draw the blocks
    for location in locations:
        pygame.draw.rect(canvas, color, pygame.Rect(location[0],location[1],dimensions[0],dimensions[1]))
        pygame.draw.rect(canvas, border_color, pygame.Rect(location[0],location[1],dimensions[0],dimensions[1]), 2)
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
    
def batter_box(dimensions, shape, block_colors, canvas, reso_width, reso_height):
    
    #Check to see which shape was passed and then get the details about the shape. Then draw the shape
    if shape == 1:
        locations = [[round(reso_width/1.596187175),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.584097859)],[round(reso_width/1.475961538),round(reso_height/1.584097859)]] # S
        if block_colors == 0: color = (85,255,51)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (255,166,77)
        draw_shape(dimensions, locations, color, canvas)
        
    elif shape == 2:
        locations = [[round(reso_width/1.475961538),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.584097859)],[round(reso_width/1.596187175),round(reso_height/1.584097859)]] # Z
        if block_colors == 0: color = (230,0,0)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (230,0,0)
        elif block_colors == 11: color = (0,0,0)
        draw_shape(dimensions, locations, color, canvas)
        
    elif shape == 3:
        locations = [[round(reso_width/1.596187175),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.584097859)],[round(reso_width/1.475961538),round(reso_height/1.47788873)]] # T
        if block_colors == 0: color = (153,0,230)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (230,0,0)
        elif block_colors == 11: color = (255,166,77)
        draw_shape(dimensions, locations, color, canvas)
        
    elif shape == 4:
        locations = [[round(reso_width/1.596187175),round(reso_height/1.47788873)],[round(reso_width/1.596187175),round(reso_height/1.584097859)],[round(reso_width/1.596187175),round(reso_height/1.70675453)],[round(reso_width/1.533721898),round(reso_height/1.47788873)]] # L
        if block_colors == 0: color = (255,166,77)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (0,0,0)
        draw_shape(dimensions, locations, color, canvas)
        
    elif shape == 5:
        locations = [[round(reso_width/1.533721898),round(reso_height/1.385026738)],[round(reso_width/1.533721898),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.584097859)],[round(reso_width/1.533721898),round(reso_height/1.70675453)]] # line
        if block_colors == 0: color = (102,255,255)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (255,166,77)
        draw_shape(dimensions, locations, color, canvas)
        
    elif shape == 6:
        locations = [[round(reso_width/1.596187175),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.584097859)],[round(reso_width/1.533721898),round(reso_height/1.70675453)]] # mirrored L
        if block_colors == 0: color = (0,0,255)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (230,0,0)
        elif block_colors == 11: color = (0,0,0)
        draw_shape(dimensions, locations, color, canvas)
        
    elif shape == 7:
        locations = [[round(reso_width/1.596187175),round(reso_height/1.47788873)],[round(reso_width/1.596187175),round(reso_height/1.584097859)],[round(reso_width/1.533721898),round(reso_height/1.47788873)],[round(reso_width/1.533721898),round(reso_height/1.584097859)]] # square
        if block_colors == 0: color = (255,255,102)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (255,166,77)
        draw_shape(dimensions, locations, color, canvas)
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def initial_information(shape, block_colors, reso_width, reso_height):
    
    #Check to see which shape was passed. Then return the initial location of the shape
    if shape == 1:
        if block_colors == 0: color = (85,255,51)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (255,166,77)
        return [[(round(reso_width/39.19148936) * 14),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),0],[(round(reso_width/39.19148936) * 16),0]], color # S
        
    elif shape == 2:
        if block_colors == 0: color = (230,0,0)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (230,0,0)
        elif block_colors == 11: color = (0,0,0)
        return [[(round(reso_width/39.19148936) * 14),0],[(round(reso_width/39.19148936) * 15),0],[(round(reso_width/39.19148936) * 15),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 16),round(reso_height/22.04255319)]], color # Z
        
    elif shape == 3:
        if block_colors == 0: color = (153,0,230)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (230,0,0)
        elif block_colors == 11: color = (255,166,77)
        return [[(round(reso_width/39.19148936) * 14),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),0],[(round(reso_width/39.19148936) * 16),round(reso_height/22.04255319)]], color # T
        
    elif shape == 4:
        if block_colors == 0: color = (255,166,77)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (0,0,0)
        return [[(round(reso_width/39.19148936) * 14),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 16),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 16),0]], color # L
        
    elif shape == 5:
        if block_colors == 0: color = (102,255,255)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (255,166,77)
        return [[(round(reso_width/39.19148936) * 14),0],[(round(reso_width/39.19148936) * 15),0],[(round(reso_width/39.19148936) * 16),0],[(round(reso_width/39.19148936) * 17),0]], color # line
    
    elif shape == 6:
        if block_colors == 0: color = (0,0,255)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (230,0,0)
        elif block_colors == 11: color = (0,0,0)
        return [[(round(reso_width/39.19148936) * 14),0],[(round(reso_width/39.19148936) * 14),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 16),round(reso_height/22.04255319)]], color # mirrored L
        
    elif shape == 7:
        if block_colors == 0: color = (255,255,102)
        elif block_colors == 1: color = (85,255,51)
        elif block_colors == 2: color = (0,0,255)
        elif block_colors == 3: color = (230,0,0)
        elif block_colors == 4: color = (102,255,255)
        elif block_colors == 5: color = (255,255,102)
        elif block_colors == 6: color = (255,166,77)
        elif block_colors == 7: color = (153,0,230)
        elif block_colors == 8: color = (255,255,255)
        elif block_colors == 9: color = (0,0,0)
        elif block_colors == 10: color = (85,255,51)
        elif block_colors == 11: color = (255,166,77)
        return [[(round(reso_width/39.19148936) * 15),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 15),0],[(round(reso_width/39.19148936) * 16),round(reso_height/22.04255319)],[(round(reso_width/39.19148936) * 16),0]], color # square
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
    
def rotate(shape, locations, color, rotation, shapes_on_board, canvas, reso_width, reso_height):
    
    #Create a new variable for the unchanged shapes and rotation
    unchanged_locations = [[],[],[],[]] ; unchanged_rotation = 0 ; unchanged_rotation += rotation
    index1 = 0
    
    for location in locations:
        
        index2 = 0
        
        for variable in location:
            
            unchanged_locations[index1].append(locations[index1][index2])
            index2 += 1
        
        index1 += 1
    
    #Check to see which shape is being dealt with
    
    if shape == 1: # S /// WORKS
         
        #Determine the rotation and move accordingly
        if rotation == 0:
            rotation = 1
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] - round(reso_height/11.0212766)]
            locations[1][1] -= round(reso_height/22.04255319)
            locations[2][0] += round(reso_width/39.19148936)
            locations[3][1] += round(reso_height/22.04255319)
            
        elif rotation == 1:
            rotation = 0
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] + round(reso_height/11.0212766)]
            locations[1][1] += round(reso_height/22.04255319)
            locations[2][0] -= round(reso_width/39.19148936)
            locations[3][1] -= round(reso_height/22.04255319)
        
    elif shape == 2: # Z /// WORKS
        
        #Determine the rotation and move accordingly
        if rotation == 0:
            rotation = 1
            locations[0] = [locations[0][0] + round(reso_width/19.59574468), locations[0][1] - round(reso_height/22.04255319)]
            locations[1][0] += round(reso_width/39.19148936)
            locations[2][1] -= round(reso_height/22.04255319)
            locations[3][0] -= round(reso_width/39.19148936)
            
        elif rotation == 1:
            rotation = 0
            locations[0] = [locations[0][0] - round(reso_width/19.59574468), locations[0][1] + round(reso_height/22.04255319)]
            locations[1][0] -= round(reso_width/39.19148936)
            locations[2][1] += round(reso_height/22.04255319)
            locations[3][0] += round(reso_width/39.19148936)
        
    elif shape == 3: # T /// WORKS
        
        #Determine the rotation and move accordingly
        if rotation == 0:
            rotation = 1
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] + round(reso_height/22.04255319)]
            
        elif rotation == 1:
            rotation = 2
            locations[2] = [locations[2][0] - round(reso_width/39.19148936), locations[2][1] + round(reso_height/22.04255319)]
            
        elif rotation == 2:
            rotation = 3
            locations[3] = [locations[3][0] - round(reso_width/39.19148936), locations[3][1] - round(reso_height/22.04255319)]
            
        elif rotation == 3:
            rotation = 0
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] - round(reso_height/22.04255319)]
            locations[2] = [locations[2][0] + round(reso_width/39.19148936), locations[0][1] - round(reso_height/22.04255319)]
            locations[3] = [locations[3][0] + round(reso_width/39.19148936), locations[3][1] + round(reso_height/22.04255319)]
        
    elif shape == 4: # L /// WORKS
        
        #Determine the rotation and move accordingly
        if rotation == 0:
            rotation = 1
            locations[2][0] -= round(reso_width/39.19148936)
            locations[1][1] -= round(reso_height/22.04255319)
            locations[3][1] += round(reso_height/22.04255319)
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] - round(reso_height/11.0212766)]
            
        elif rotation == 1:
            rotation = 2
            locations[2][0] -= round(reso_width/39.19148936)
            locations[3] = [locations[3][0] - round(reso_width/19.59574468), locations[3][1] + round(reso_height/22.04255319)]
            locations[1] = [locations[1][0] - 0, locations[1][1] + round(reso_height/22.04255319)]
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] + round(reso_height/11.0212766)]
            
            
        elif rotation == 2:
            rotation = 3
            locations[2][0] += round(reso_width/39.19148936)
            locations[1][1] += round(reso_height/22.04255319)
            locations[3][1] -= round(reso_height/22.04255319)
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] + round(reso_height/11.0212766)]
            
        elif rotation == 3:
            rotation = 0
            locations[2][0] += round(reso_width/39.19148936)
            locations[3] = [locations[3][0] + round(reso_width/19.59574468), locations[3][1] - round(reso_height/22.04255319)]
            locations[1] = [locations[1][0] + 0, locations[1][1] - round(reso_height/22.04255319)]
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] - round(reso_height/11.0212766)]
        
    elif shape == 5: # line /// WORKS
        
        #Determine the rotation and move accordingly
        if rotation == 0:
            rotation = 1
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] - round(reso_height/22.04255319)]
            locations[2] = [locations[2][0] - round(reso_width/39.19148936), locations[2][1] + round(reso_height/22.04255319)]
            locations[3] = [locations[3][0] - round(reso_width/19.59574468), locations[3][1] + round(reso_height/11.0212766)]
            
        elif rotation == 1:
            rotation = 0
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] + round(reso_height/22.04255319)]
            locations[2] = [locations[2][0] + round(reso_width/39.19148936), locations[2][1] - round(reso_height/22.04255319)]
            locations[3] = [locations[3][0] + round(reso_width/19.59574468), locations[3][1] - round(reso_height/11.0212766)]
            
    elif shape == 6: # mirrored L /// WORKS
        
        #Determine the rotation and move accordingly
        if rotation == 0:
            rotation = 1
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] + round(reso_height/22.04255319)]
            locations[2] = [locations[2][0] - round(reso_width/39.19148936), locations[2][1] + round(reso_height/22.04255319)]
            locations[3] = [locations[3][0] - round(reso_width/19.59574468), locations[3][1] + round(reso_height/11.0212766)]
            
        elif rotation == 1:
            rotation = 2
            locations[0] = [locations[0][0] + round(reso_width/39.19148936), locations[0][1] + round(reso_height/22.04255319)]
            locations[1][0] += round(reso_width/19.59574468)
            locations[2] = [locations[2][0] + round(reso_width/39.19148936), locations[2][1] - round(reso_height/22.04255319)]
            locations[3][1] -= round(reso_height/11.0212766)
            
        elif rotation == 2:
            rotation = 3
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] - round(reso_height/22.04255319)]
            locations[2] = [locations[2][0] + round(reso_width/39.19148936), locations[2][1] - round(reso_height/22.04255319)]
            locations[3] = [locations[3][0] + round(reso_width/19.59574468), locations[3][1] - round(reso_height/11.0212766)]
            
        elif rotation == 3:
            rotation = 0
            locations[0] = [locations[0][0] - round(reso_width/39.19148936), locations[0][1] - round(reso_height/22.04255319)]
            locations[1][0] -= round(reso_width/19.59574468)
            locations[2] = [locations[2][0] - round(reso_width/39.19148936), locations[2][1] + round(reso_height/22.04255319)]
            locations[3][1] += round(reso_height/11.0212766)
            
    elif shape == 7: # square /// WORKS
        
        #It's a square. You can't rotate this
        return locations, rotation
    
    #Next, check to see if any of the new locations interset with blocks on the board. Start by looping for every single location in locations
    for location in locations:
        
        #Check to see if the blocks are hitting either of the walls
        if location[0] == (round(reso_width/39.19148936) * 10) or location[0] == (round(reso_width/39.19148936) * 21):
            
            #Check to see which wall is being hit, and change the x variables needed
            if location[0] == (round(reso_width/39.19148936) * 10):
                for location2 in locations:
                    location2[0] += round(reso_width/39.19148936)
            
            elif location[0] == (round(reso_width/39.19148936) * 21):
                for location2 in locations:
                    location2[0] -= round(reso_width/39.19148936)
                
            #Then check to see if the shape is colliding with another shape after being shifted
            for location2 in locations:
                for row in shapes_on_board:
                    if len(row) > 0:
                        
                        #loop for every block in the row
                        for block in row:
                            
                            #Check to see if the y values and x values match
                            if location2[0] == block[0] and location2[1] == block[1]:
                                
                                #If so, return the unchanged locations
                                return unchanged_locations, unchanged_rotation

        #If the shape isn't colliding with a wall, check to see if it's colliding with any shapes
        for row in shapes_on_board:
            if len(row) > 0:
                
                #loop for every block in the row
                for block in row:
                    
                    #Check to see if the y values and x values match
                    if location[0] == block[0] and location[1] == block[1]:
                        
                        #If so shift the shape to the right, check the collisions, and then to the left, and check the collisions
                        collision = False
                        for location2 in locations:
                            location2[0] += round(reso_width/39.19148936)
                        for location2 in locations:
                            for rows in shapes_on_board:
                                if len(rows) > 0:
                                    for blocks in rows:
                                        if location2[0] == blocks[0] and location2[1] == blocks[1]:
                                            collision = True
                        if collision:
                            for location2 in locations:
                                if shape != 5:
                                    location2[0] -= round(reso_width/19.59574468)
                                else: # move two over to the left if the shape is the line
                                    location2[0] -= round(reso_width/13.06382979)
                            for location2 in locations:
                                for rows in shapes_on_board:
                                    if len(rows) > 0:
                                        for blocks in rows:
                                            if location2[0] == blocks[0] and location2[1] == blocks[1]:
                                                
                                                #If the shape can't be shifted and rotated right or left, then don't rotate the shape
                                                return unchanged_locations, unchanged_rotation
                        
        #Then check to see if the block is hitting the block is hitting the floor
        if location[1] == (round(reso_height/22.04255319) * 20):
            
            #If so then move the blocks up and then check to see if it's hitting the wall or floor
            for location2 in locations:
                location2[1] -= round(reso_height/22.04255319)
            
            #After changing the locations, check for collisions with the walls
            for location2 in locations:
                if location2[0] == (round(reso_width/39.19148936) * 10) or location2[0] == (round(reso_width/39.19148936) * 21):
                    
                    #Check to see which wall is being hit, and change the x variables needed
                    if location2[0] == (round(reso_width/39.19148936) * 10):
                        for location3 in locations:
                            location3[0] += round(reso_width/39.19148936)
                    
                    elif location2[0] == (round(reso_width/39.19148936) * 21):
                        for location3 in locations:
                            location3[0] -= round(reso_width/39.19148936)
                        
                    #Then check to see if the shape is colliding with another shape after being shifted
                    for location3 in locations:
                        for row in shapes_on_board:
                            if len(row) > 0:
                                
                                #loop for every block in the row
                                for block in row:
                                    
                                    #Check to see if the y values and x values match
                                    if location3[0] == block[0] and location3[1] == block[1]:
                                        
                                        #If so, return the unchanged locations
                                        return unchanged_locations, unchanged_rotation
                        
                #If the shape isn't colliding with a wall, check to see if it's colliding with any shapes
                for row in shapes_on_board:
                    if len(row) > 0:
                        
                        #loop for every block in the row
                        for block in row:
                            
                            #Check to see if the y values and x values match
                            if location2[0] == block[0] and location2[1] == block[1]:
                                
                                #If so shift the shape to the right, check the collisions, and then to the left, and check the collisions
                                collision = False
                                for location3 in locations:
                                    location3[0] += round(reso_width/39.19148936)
                                for location3 in locations:
                                    for rows in shapes_on_board:
                                        if len(rows) > 0:
                                            for blocks in rows:
                                                if location3[0] == blocks[0] and location3[1] == blocks[1]:
                                                    collision = True
                                if collision:
                                    for location3 in locations:
                                        if shape != 5:
                                            location3[0] -= round(reso_width/19.59574468)
                                        else: # move two over to the left if the shape is the line
                                            location3[0] -= round(reso_width/13.06382979)
                                    for location3 in locations:
                                        for rows in shapes_on_board:
                                            if len(rows) > 0:
                                                for blocks in rows:
                                                    if location3[0] == blocks[0] and location3[1] == blocks[1]:
                                                        
                                                        #If the shape can't be shifted and rotated right or left, then don't rotate the shape
                                                        return unchanged_locations, unchanged_rotation
        
    #If there aren't any problems with the changes, then update the locations in shapes_on_board
    for location in unchanged_locations:
        for row in shapes_on_board:
            if len(row) > 0:
                for block in row:
                    if block == location:
                        block = locations[unchanged_locations.index(location)]
                        break
    
    #If there aren't any problems, then draw the new shape on the board to show the user the changes
    draw_shape([(reso_width/38.53556485), (reso_height/21.67364017)], locations, color, canvas)
    pygame.display.update()
    
    #If there aren't any matches, return the changed locations
    return locations, rotation
        
#===========================================================================#
#===========================================================================#
#===========================================================================#

def horizontal(key, locations, color, shapes_on_board, canvas, reso_width, reso_height):
    
    #Just to be sure, loop until either of the keys are released
    while k.is_pressed('LEFT') or k.is_pressed('RIGHT'): pass
    
    #Create a variable for the unchanged_locations
    unchanged_locations = []
    for location in locations: unchanged_locations.append(location)
    
    #Check to see what the key is and set the symbol
    if key == 'right':
    
        #Loop for every location and add a scaled value to the x value
        for location in locations:
            location[0] += round(reso_width/39.19148936)
            
    elif key == 'left':
        
        #Loop for every location and subtract a scaled value to the x value
        for location in locations:
            location[0] -= round(reso_width/39.19148936)
            
    #Next, check to see if any of the new locations interset with blocks on the board. Start by looping for every single location in locations
    for location in locations:
        
        #Check to see if the x value matches with either the walls
        if location[0] == (round(reso_width/39.19148936) * 10):
            
            #if so, change the values and then return
            locations[0][0] += round(reso_width/39.19148936)
            locations[1][0] += round(reso_width/39.19148936)
            locations[2][0] += round(reso_width/39.19148936)
            locations[3][0] += round(reso_width/39.19148936)
            return locations
        
        if location[0] == (round(reso_width/39.19148936) * 21):
            
            #if so, change the values and then return
            locations[0][0] -= round(reso_width/39.19148936)
            locations[1][0] -= round(reso_width/39.19148936)
            locations[2][0] -= round(reso_width/39.19148936)
            locations[3][0] -= round(reso_width/39.19148936)
            return locations
        
        #Loop for every row
        for row in shapes_on_board:
            if len(row) > 0:
                
                #loop for every block in the row
                for block in row:
                    
                    #Check to see if the y values and x values match
                    if location[0] == block[0] and location[1] == block[1]:
                        
                        #If so, return the unchanged locations
                        if key == 'left':
            
                            #if so, change the values and then return
                            locations[0][0] += round(reso_width/39.19148936)
                            locations[1][0] += round(reso_width/39.19148936)
                            locations[2][0] += round(reso_width/39.19148936)
                            locations[3][0] += round(reso_width/39.19148936)
                            return locations
                        
                        if key == 'right':
                            
                            #if so, change the values and then return
                            locations[0][0] -= round(reso_width/39.19148936)
                            locations[1][0] -= round(reso_width/39.19148936)
                            locations[2][0] -= round(reso_width/39.19148936)
                            locations[3][0] -= round(reso_width/39.19148936)
                            return locations
    
    #If there aren't any problems with the changes, then update the locations in shapes_on_board
    for location in unchanged_locations:
        for row in shapes_on_board:
            if len(row) > 0:
                for block in row:
                    if block == location:
                        block = locations[unchanged_locations.index(location)]
                        break
    
    #If there aren't any problems, then draw the new shape on the board to show the user the changes
    draw_shape([(reso_width/38.53556485), (reso_height/21.67364017)], locations, color, canvas)
    #pygame.display.update()

    #If there aren't any matches, return the changed locations
    return locations 
        
#===========================================================================#
#===========================================================================#
#===========================================================================#

def down(use_shadow, block_colors, clock, color, locations, shapes_on_board, background_image, batter_box_shape, canvas, bs, button1, button2, current_user_rectangle_image, current_user, best_score, score_rectangle_image2, x_best, reso_width, reso_height):
    
    #Set the current time and time ticks
    current_time = pygame.time.get_ticks()
    time_ticks = pygame.time.get_ticks()
    
    #Loop until the user lets go of the down arrow
    while k.is_pressed('DOWN'):
        
        #Update the current time
        current_time = pygame.time.get_ticks()
        
        #Check to see if an action should be made
        if current_time - time_ticks > 50:
            
            #Change time_ticks
            time_ticks = pygame.time.get_ticks()
            
            #Create the previous locations
            previous_locations = [[],[],[],[]]
            index1 = 0
    
            for location in locations:
                
                index2 = 0
                
                for variable in location:
                    
                    previous_locations[index1].append(locations[index1][index2])
                    index2 += 1
                
                index1 += 1
            
            #Increase the y values of all the locations
            for location in locations:
                location[1] += round(reso_height/22.04255319)
                
            #Check to see if the blocks are colling with any blocks
            for location in locations:
                
                #Check to see if the x value matches with the floor
                if location[1] >= (round(reso_height/22.04255319) * 20):
                    
                    #If so, return the previous locations
                    return previous_locations
                
                #Loop for every row
                for row in shapes_on_board:
                    if len(row) > 0:
                        
                        #loop for every block in the row
                        for block in row:
                            
                            #Check to see if the y values and x values match
                            if location[0] == block[0] and location[1] == block[1]:
                                
                                #If so, return the unchanged locations
                                return previous_locations
            
            #Draw the board
            TBd.draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height)
            
            #If the blocks aren't colliding with anything, then draw them so the user can see the changes being made
            draw_shape([(reso_width/38.53556485), (reso_height/21.67364017)], locations, color, canvas)
            if use_shadow: TBd.shape_shadow(locations, shapes_on_board, block_colors, canvas, reso_width, reso_height)
            
            #Draw the shape in the batter's box
            batter_box([(reso_width/38.53556485), (reso_height/21.67364017)], batter_box_shape, block_colors, canvas, reso_width, reso_height)
            
            #Draw buttons for design
            if button1.draw(canvas, bs):pass
            if button2.draw(canvas, bs): pass
            
            #Draw the other things on the board for design
            canvas.blit(current_user_rectangle_image, (round(reso_width/1.292631579),round(reso_height/8.633333333)))
            TO.display_user(canvas, current_user, round(reso_width/1.147663551), round(reso_height/5.312820513), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
            canvas.blit(score_rectangle_image2, (round(reso_width/1.292631579), round(reso_height/-20.72))) # draw the current user's best score rectangle
            canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(best_score),True,(0,0,0))),(x_best,round(reso_height/41.44))) # draw the user's best score
            
            #Update the canvas
            pygame.display.update()
            clock.tick(60) #60 for 60 frames
            
    #Once the user lets go, return the locations
    return locations

#===========================================================================#
#===========================================================================#
#===========================================================================#

def keyboard_action(use_shadow, block_colors, current_time, time_ticks, clock, locations, shapes_on_board, shapes, background_image, color, canvas, bs, button1, button2, CuRi, current_user, best_score, score_rectangle_image2, x_best, reso_width, reso_height):
    
    keys = pygame.key.get_pressed() # check the key being pressed
    next_shape = False #set up the variable
    
    #Check to see which key the user is holding, loop until they let go, and then return a specific value
    if k.is_pressed('r'):
        key = 'rotate'
            
    elif k.is_pressed('LEFT'):
        key = 'left'
    
    #If the key being held down is the down arrow, don't wait
    elif k.is_pressed('DOWN'):
        return 'down', locations, current_time, time_ticks
        
    elif k.is_pressed('RIGHT'):
        key = 'right'
    
    #Loop until the user lets go all of the keys
    while k.is_pressed('r') or k.is_pressed('LEFT') or k.is_pressed('RIGHT'):
        
        #Check to see if the time to move the shape down is here
        if current_time - time_ticks > TBd.get_time():
            
            #If so, then affect the locations y variables
            for location in locations:
               location[1] += round(reso_height/22.04255319)
            
            #Check to see if the shape collided with anything. If so, go to the next shape
            for location in locations:
                if not next_shape:
                    next_shape = TBd.checker(location, shapes_on_board)
            
            #Check to see if the shape is making contact with the bottom of the board, if so, move onto the next shape
            for location in locations:
                if location[1] == (round(reso_height/22.04255319) * 20):
                    next_shape = True
            
            #If the shape did collide with something, move the shape back up one block and go to the next shape
            while next_shape:
                for location in locations:
                    location[1] -= round(reso_height/22.04255319)
                up = TBd.checker(location, shapes_on_board)
                if up: continue
                
                #Make sure no action can be completed when the next_shape is needed
                return '1', locations, current_time, time_ticks
            
            #If so, then update time_ticks
            time_ticks = pygame.time.get_ticks()
            
        #Update the current_time
        current_time = pygame.time.get_ticks()
        
        #Constantly draw the board
        TBd.draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height)
        
        #Constantly draw the shape (shapes[1]) in the batter's box
        batter_box([(reso_width/38.53556485), (reso_height/21.67364017)], shapes[1], block_colors, canvas, reso_width, reso_height)
        
        #draw the current shape on the board
        draw_shape([(reso_width/38.53556485), (reso_height/21.67364017)], locations, color, canvas)
        if use_shadow: TBd.shape_shadow(locations, shapes_on_board, block_colors, canvas, reso_width, reso_height)
        
        #Draw buttons for design
        if button1.draw(canvas, bs):pass
        if button2.draw(canvas, bs): pass
        
        #Draw the other images for design too
        canvas.blit(CuRi, (round(reso_width/1.292631579),round(reso_height/8.633333333)))
        TO.display_user(canvas, current_user, round(reso_width/1.147663551), round(reso_height/5.312820513), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
        canvas.blit(score_rectangle_image2, (round(reso_width/1.292631579), round(reso_height/-20.72))) # draw the current user's best score rectangle
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(best_score),True,(0,0,0))),(x_best,round(reso_height/41.44))) # draw the user's best score
        
        #Constantly update the screen
        pygame.display.update()
        
    #After the user lets go, return the key
    return key, locations, current_time, time_ticks

#===========================================================================#
#===========================================================================#
#===========================================================================#

def shape_selecter(SC):
    
    #Check to see if any of the numbers are >= to 8
    for count in SC:
        if SC[count] >= 8:
            
            #If so, reset it's number and then return it
            SC[count] = 0
            return int(count), SC
    
    #If none of them are >= to 8, select a random number
    num = r(1,7)
    
    #Increase every shapes' count by 1
    for count in SC:
        SC[count] += 1
    
    #Reset the randomly selected shape's_count to 0
    SC[str(num)] = 0
    
    #Then return that selected shape's_count and the list
    return num, SC

#===========================================================================#
#===========================================================================#
#===========================================================================#

def change_block_color(block_colors):
    
    #Call the global variable
    global block_color
    
    #Change the block color
    block_color = block_colors

#===========================================================================#
#===========================================================================#
#===========================================================================#

def get_block_color():
    
    #Call the global variable
    global bock_color
    
    #Return the block color
    return block_color

#===========================================================================#
#===========================================================================#
#===========================================================================#