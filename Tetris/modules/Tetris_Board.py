#Imports
import pygame
from random import randint as r
import modules.Tetris_Shapes as TS

#Global variables
global colors_on_board, score, level, lines
colors_on_board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #20 rows in total
score = 0
level = 0
lines = 0

#===========================================================================#
#===========================================================================#
#===========================================================================#

def reset_variables():
    
    #Call the global variable
    global colors_on_board, score, level, lines
    
    #Reset the global variables
    colors_on_board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    score = 0
    level = 0
    lines = 0

#===========================================================================#
#===========================================================================#
#===========================================================================#

def draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height):
    
    #Get the block colors and set the colors accordingly
    bc = TS.get_block_color()
    
    # change the grid color based on the user's choice
    if bc == 0: grid_color = (211,211,211,128) ; boundary_color = (221,221,221) ; change_background = False
    elif bc == 1 or bc == 2 or bc == 3 or bc == 4 or bc == 5 or bc == 6 or bc == 7 or bc == 10: grid_color = (70,70,70,128) ; boundary_color = (221,221,221) ; change_background = True ; background_color = (0,0,0)
    elif bc == 9 or bc == 11: grid_color = (70,70,70,128) ; boundary_color = (111,111,111) ; change_background = True ; background_color = (144,144,144)
    elif bc == 8: grid_color = (70,70,70,128) ; boundary_color = (133,133,133) ; change_background = True ; background_color = (0,0,0)
        
    #Draw the background to cover previous images (blocks)
    canvas.blit(background_image, (0,0))
    
    #Change the background if needed
    if change_background:
        pygame.draw.rect(canvas, background_color, pygame.Rect((round(reso_width/39.19148936) * 10),0,round(reso_width/1.805882353),round(reso_height/1.04964539)))
        
    #Draw the grid
    for y in range(0,(round(reso_height/22.04255319) * 20),round(reso_height/22.04255319)):
        for x in range(round(reso_width/3.562862669),(round(reso_width/39.19148936) * 21),round(reso_width/39.19148936)):
            pygame.draw.rect(canvas, grid_color, pygame.Rect(x,y,(reso_width/38.53556485), (reso_height/21.67364017)), 2)
    
    #Draw the placed shapes
    draw_shapes(shapes_on_board, canvas, reso_width, reso_height)
    
    #Draw the blocks
    for y in range(0,round(reso_height/1.04964539),round(reso_height/22.04255319)):
        pygame.draw.rect(canvas, boundary_color, pygame.Rect((round(reso_width/39.19148936) * 10),y,(reso_width/38.53556485), (reso_height/21.67364017)))
        pygame.draw.rect(canvas, (0,0,0), pygame.Rect((round(reso_width/39.19148936) * 10),y,(reso_width/38.53556485), (reso_height/21.67364017)), 2)
        
        pygame.draw.rect(canvas, boundary_color, pygame.Rect((round(reso_width/39.19148936) * 21),y,(reso_width/38.53556485), (reso_height/21.67364017)))
        pygame.draw.rect(canvas, (0,0,0), pygame.Rect((round(reso_width/39.19148936) * 21),y,(reso_width/38.53556485), (reso_height/21.67364017)), 2)
    
    for x in range((round(reso_width/39.19148936) * 10),round(reso_width/1.805882353),round(reso_width/39.19148936)):
        pygame.draw.rect(canvas, boundary_color, pygame.Rect(x,(round(reso_height/22.04255319) * 20),(reso_width/38.53556485), (reso_height/21.67364017)))
        pygame.draw.rect(canvas, (0,0,0), pygame.Rect(x,(round(reso_height/22.04255319) * 20),(reso_width/38.53556485), (reso_height/21.67364017)), 2)
    
    #Draw the background for the outside of the blocks
    pygame.draw.rect(canvas, (25,25,25), pygame.Rect(round(reso_width/1.781431335), 0, round(reso_width/2.276885043), round(reso_height/1.04964539)))
    pygame.draw.rect(canvas, (25,25,25), pygame.Rect(0, 0, (round(reso_width/39.19148936) * 10), round(reso_height/1.04964539)))
    pygame.draw.rect(canvas, (25,25,25), pygame.Rect(0, round(reso_height/1.04964539), round(reso_width/.999457406), round(reso_height/1.04964539)))
    
    #Draw the boxes where the "lines", "score", "level", and "batter box" will go
    pygame.draw.rect(canvas, (255,255,255), pygame.Rect(round(reso_width/1.710306407), round(reso_height/51.8), round(reso_width/6.351724138), round(reso_height/9.008695652))) # score
    pygame.draw.rect(canvas, (255,255,255), pygame.Rect(round(reso_width/1.710306407), round(reso_height/5.312820513), round(reso_width/6.351724138), round(reso_height/9.008695652))) # level
    pygame.draw.rect(canvas, (255,255,255), pygame.Rect(round(reso_width/1.710306407), round(reso_height/2.8), round(reso_width/6.351724138), round(reso_height/9.008695652))) # lines
    pygame.draw.rect(canvas, (255,255,255), pygame.Rect(round(reso_width/1.686813187), round(reso_height/1.770940171), round(reso_width/7.084615385), round(reso_height/4.408510638))) # batter box
    
    pygame.draw.rect(canvas, (25,140,255), pygame.Rect(round(reso_width/1.710306407), round(reso_height/51.8), round(reso_width/6.351724138), round(reso_height/9.008695652)), 2) # score border
    pygame.draw.rect(canvas, (25,140,255), pygame.Rect(round(reso_width/1.710306407), round(reso_height/5.312820513), round(reso_width/6.351724138), round(reso_height/9.008695652)), 2) # level border
    pygame.draw.rect(canvas, (25,140,255), pygame.Rect(round(reso_width/1.710306407), round(reso_height/2.8), round(reso_width/6.351724138), round(reso_height/9.008695652)), 2) # lines border
    pygame.draw.rect(canvas, (25,140,255), pygame.Rect(round(reso_width/1.686813187), round(reso_height/1.770940171), round(reso_width/7.084615385), round(reso_height/4.408510638)), 2) # batter box border
    
    #Draw the text for the "lines", "score", and "level" boxes
    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/36.84 + reso_height/20.72)/2))).render('S c o r e',True,(0,0,0))),(round(reso_width/1.592048401),round(reso_height/41.44)))
    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/36.84 + reso_height/20.72)/2))).render('L e v e l',True,(0,0,0))),(round(reso_width/1.592048401),round(reso_height/5.18)))
    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/36.84 + reso_height/20.72)/2))).render('L i n e s',True,(0,0,0))),(round(reso_width/1.592048401),round(reso_height/2.762666667)))
    
    #Draw the numbers for each of the boxes that requires numbers
    game_information(canvas, reso_width, reso_height)
    
    #Return
    return

#===========================================================================#
#===========================================================================#
#===========================================================================#

def draw_shapes(shapes_on_board, canvas, reso_width, reso_height):
    
    #Call the global variables
    global colors_on_board
    
    #Create an index variable for simplecity
    index1 = 0
    
    #Draw the shapes
    for row in shapes_on_board:
        if len(row) != 0:
            
            #Create another index variable and loop for every location / block within that row
            index2 = 0
            for location in row:
                
                #Draw every single block
                pygame.draw.rect(canvas, colors_on_board[index1][index2], pygame.Rect(location[0], location[1], (reso_width/38.53556485), (reso_height/21.67364017)))
                pygame.draw.rect(canvas, (0,0,0), pygame.Rect(location[0], location[1], (reso_width/38.53556485), (reso_height/21.67364017)), 2)
                index2 += 1
        
        #Increase index1 for every row
        index1 += 1
    
#===========================================================================#
#===========================================================================#
#===========================================================================#

def add_shapes(color, shape, locations, shapes_on_board, reso_height):
    
    #Call the global variable
    global colors_on_board
    
    #Based on the locations, append the locations to shapes_on_board
    for location in locations:
        shapes_on_board[(location[1]//round(reso_height/22.04255319))].append([location[0],location[1]])
        
        #Also add the color in the corresponding spot to colors_on_board
        colors_on_board[(location[1]//round(reso_height/22.04255319))].append(color)
    
    #Return shapes_on_board
    return shapes_on_board

#===========================================================================#
#===========================================================================#
#===========================================================================#

def remove_lines(shapes_on_board, background_image, canvas, LiS, LeS, ts, reso_width, reso_height):
    
    #Call the global variables
    global colors_on_board
    
    #Set variables
    add_lines = 0
    
    #Loop until there are no more rows that are filled
    while True:
        
        #Check the length of each row
        for row in shapes_on_board:
            if len(row) == 10:
                
                #If the row is full then clear that row on the colors board and the shapes board
                index = shapes_on_board.index(row)
                
                del shapes_on_board[index]
                del colors_on_board[index]
                
                #Add a row at the beginning of each list
                shapes_on_board.insert(0, []) ; colors_on_board.insert(0, [])
                
                #Loop for every row above the deleted row and increase the y value by a scaled number
                for rows in shapes_on_board[:index + 1]: # add 1 because of the insertted list
                    
                    if len(rows) != 0:
                        for block in rows:
                            block[1] += round(reso_height/22.04255319)
                            
                #Draw the board after a line is removed
                draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height)
                
                #Update the screen for the user
                pygame.display.update()
                
                #Since a line was removed, increase add_lines
                add_lines += 1
                
                #Continue to loop again to check for more rows
                continue
        
        #After there are no more rows to remove, update the game information
        dont_play = update_game_information(add_lines, ts)
        
        #Play a sound if there is a tetris, lines, or level increase
        if 0 < add_lines < 4 and not dont_play: pygame.mixer.Sound.play(LiS) # play the sound effect
        elif add_lines == 4 and not dont_play: pygame.mixer.Sound.play(LeS) # play the sound effect
        
        #If there are no more rows with 10 blocks, go back to the main function
        return shapes_on_board

#===========================================================================#
#===========================================================================#
#===========================================================================#
    
def checker(location, shapes_on_board):
    
    #Create an index variable for simplecity
    index1 = 0
    
    #Loop for every row in shapes_on_board
    for row in shapes_on_board:
        if len(row) != 0:
            
            #Create another index variable and loop for every location / block within that row
            index2 = 0
            for block in row:
                
                #Check to see if the location passed is going to run into the location within the row
                if location[1] == block[1] and location[0] == block[0]:
                    
                    #If so, return true
                    return True
                
                index2 += 1
        
        #Increase index1 for every row
        index1 += 1
    
    #If there are no soon to be colliding blocks, return false
    return False

#===========================================================================#
#===========================================================================#
#===========================================================================#

def game_information(canvas, reso_width, reso_height):
    
    #Call the global variables
    global score, level, lines
    
    #Modifications of the text
    text_colors = (0,0,0)
    sizes = round((reso_width/23.025 + reso_height/12.95)/2)
    fonts = "Watermelon"
    
    #Set the font of the text
    font = pygame.font.SysFont(fonts, sizes)
    
    #Render the texts
    score_text = font.render(str(score), True, text_colors)
    level_text = font.render(str(level), True, text_colors)
    lines_text = font.render(str(lines), True, text_colors)
        
    #Render the texts on the canvas based on their length
    if score > 999999:
        canvas.blit(score_text, (round(reso_width/1.674545455),round(reso_height/14.8)))
    elif score > 99999:
        canvas.blit(score_text, (round(reso_width/1.644642857),round(reso_height/14.8)))
    elif score > 9999:
        canvas.blit(score_text, (round(reso_width/1.622907489),round(reso_height/14.8)))
    elif score > 999:
        canvas.blit(score_text, (round(reso_width/1.594805195),round(reso_height/14.8)))
    elif score > 99:
        canvas.blit(score_text, (round(reso_width/1.567659574),round(reso_height/14.8)))
    elif score > 9:
        canvas.blit(score_text, (round(reso_width/1.541422594),round(reso_height/14.8)))
    elif score > -1:
        canvas.blit(score_text, (round(reso_width/1.516049383),round(reso_height/14.8)))
        
    if level > 999999:
        canvas.blit(level_text, (round(reso_width/1.674545455),round(reso_height/4.228571429)))
    elif level > 99999:
        canvas.blit(level_text, (round(reso_width/1.644642857),round(reso_height/4.228571429)))
    elif level > 9999:
        canvas.blit(level_text, (round(reso_width/1.622907489),round(reso_height/4.228571429)))
    elif level > 999:
        canvas.blit(level_text, (round(reso_width/1.594805195),round(reso_height/4.228571429)))
    elif level > 99:
        canvas.blit(level_text, (round(reso_width/1.567659574),round(reso_height/4.228571429)))
    elif level > 9:
        canvas.blit(level_text, (round(reso_width/1.541422594),round(reso_height/4.228571429)))
    elif level > -1:
        canvas.blit(level_text, (round(reso_width/1.516049383),round(reso_height/4.228571429)))
        
    if lines > 999999:
        canvas.blit(lines_text, (round(reso_width/1.674545455),round(reso_height/2.437647059)))
    elif lines > 99999:
        canvas.blit(lines_text, (round(reso_width/1.644642857),round(reso_height/2.437647059)))
    elif lines > 9999:
        canvas.blit(lines_text, (round(reso_width/1.622907489),round(reso_height/2.437647059)))
    elif lines > 999:
        canvas.blit(lines_text, (round(reso_width/1.594805195),round(reso_height/2.437647059)))
    elif lines > 99:
        canvas.blit(lines_text, (round(reso_width/1.567659574),round(reso_height/2.437647059)))
    elif lines > 9:
        canvas.blit(lines_text, (round(reso_width/1.541422594),round(reso_height/2.437647059)))
    elif lines > -1:
        canvas.blit(lines_text, (round(reso_width/1.516049383),round(reso_height/2.437647059)))
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def update_game_information(add_lines, ts):
    
    #Call the global variables
    global score, level, lines
    
    #Create variables for the sound play checker
    old_level = 0 ; old_level += (lines // 10) ; increase = False
    
    #Increase the lines by the variable passed
    lines += add_lines
    
    #Update the level
    level = lines // 10
    
    #If there is an increase in level, play the sound effect
    if level > old_level: increase = True ; pygame.mixer.Sound.play(ts) # play the sound effect
    
    #Based on the amount added increase the score and the level
    if level == 0:
        if add_lines == 1:
            score += 40
        elif add_lines == 2:
            score += 100
        elif add_lines == 3:
            score += 300
        elif add_lines == 4:
            score += 1200
    
    elif level == 1:
        if add_lines == 1:
            score += 80
        elif add_lines == 2:
            score += 200
        elif add_lines == 3:
            score += 600
        elif add_lines == 4:
            score += 2400
            
    elif level >= 2 and level <= 8:
        if add_lines == 1:
            score += 120
        elif add_lines == 2:
            score += 300
        elif add_lines == 3:
            score += 900
        elif add_lines == 4:
            score += 3600
            
    elif level == 9:
        if add_lines == 1:
            score += 400
        elif add_lines == 2:
            score += 1000
        elif add_lines == 3:
            score += 3000
        elif add_lines == 4:
            score += 12000
            
    elif level > 9:
        if add_lines == 1:
            score += 40*(add_lines + 1) 
        elif add_lines == 2:
            score += 100*(add_lines + 1)
        elif add_lines == 3:
            score += 300*(add_lines + 1)
        elif add_lines == 4:
            score += 1200*(add_lines + 1)
            
    #Return the variable that will decide whether the other sound effects will be played
    return increase

#===========================================================================#
#===========================================================================#
#===========================================================================#

def shape_shadow(locations, shapes_on_board, bc, canvas, reso_width, reso_height):
    
    #Decide on a color based on the block_color # CHANGED
    shadow_color = (255,255,255)
    
    #Create a copy of the locations
    shadow_locations = [[],[],[],[]]
    index1 = 0
    
    for location in locations:
        
        index2 = 0
        
        for variable in location:
            
            shadow_locations[index1].append(locations[index1][index2])
            index2 += 1
        
        index1 += 1
    
    #Create a boolean variable to detect when the shape finally hits another block
    collision = False
    
    #Create an accumulator to keep looping
    loop = 0
    
    #Loop for every location in locations and check for when any of the locations collide with a block
    while not collision:
        for location in shadow_locations:
            location[1] += round(reso_height/22.04255319)
            
        #Check to see if the new location is hitting anything
        for row in shapes_on_board:
            if len(row) > 0:
                for block in row:
                    for location in shadow_locations:
                        
                        #Check to see if they match
                        if location[1] == block[1] and location[0] == block[0]:
                            
                            #If so, then change the collision variable to be true
                            collision = True
        
        #Check for if / when any of the new location hits the bottom of the board instead
        for location in shadow_locations:
            if location[1] == (round(reso_height/22.04255319) * 20):
                collision = True
        
        #If there is a collision, increase all of the variables in the locations and break out of the loop
        if collision:
            for location2 in shadow_locations:
                location2[1] -= round(reso_height/22.04255319)
            break
    
    #Finally, draw the shape's shadow on the board
    for location in shadow_locations:
        pygame.draw.rect(canvas, shadow_color, pygame.Rect(location[0],location[1],(reso_width/38.53556485), (reso_height/21.67364017)), 2)

#===========================================================================#
#===========================================================================#
#===========================================================================#

def get_statistics():
    
    #Call the global variables
    global score, level, lines
    
    #Return the variables
    return score, level, lines

#===========================================================================#
#===========================================================================#
#===========================================================================#

def get_time():
    
    #Call the global variable
    global level
    
    #Check to see the length of the level
    if level >= 15:
        return 50
    
    time = 800 - (50*level)
    
    #Return the time
    return time

#===========================================================================#
#===========================================================================#
#===========================================================================#

def get_rgb(value, change, a1, a2, a3):
    
    #Start by increasing the red value
    if a1 != 225 and change:
        a1 += 1
    
    #Then decrease the green value
    elif a2 != 0 and change:
        a2 -= 1
    
    #Then decrease the blue value and red value and increase the green vlaue
    elif a3 != 0 and a2 != 225:
        change = False
        a3 -= 1
        a1 -= 1
        a2 += 1
        
    #Then increase the blue
    elif a3 != 225:
        a3 += 1
    
    #Then change the change value and begin increasing the red value again
    else:
        change = True
        
    #Return the values
    return a1, a2, a3, value, change

#===========================================================================#
#===========================================================================#
#===========================================================================#

def return_global():
    
    #Call the global variables
    global score, level, lines
    
    #Return them
    return score, level, lines