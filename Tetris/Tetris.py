#Imports
import pygame
import os
import modules.Tetris_Buttons as TBs
import modules.Tetris_Shapes as TS
import modules.Tetris_Board as TBd
import modules.Tetris_Other as TO
import time
import pickle
import keyboard as k
import pyautogui as pg # used to get the screen resolution

def tetris():
    #Simulates the game Tetris
    
    #First things first, get the current working directory
    cwd = os.getcwd()
    
    #Set the window to a certain spot on the screen
    x_specspot = 0 #Variable used for a specific spot
    y_specspot = 30 #Varialbe used for a specific spot
    
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x_specspot,y_specspot) #Used so that environment variables can be set in python
    
    # declare the current highscore
    current_highscore = 0
    
    #From the data file, get the all of the scores
    try:
        infile = open(cwd + r'\data\Tetris_User_Info', 'rb')
        data_dict = pickle.load(infile)
        infile.close()
        
        for player in data_dict:
            if data_dict[player][1] > current_highscore: current_highscore = data_dict[player][1]
    except:
        data_dict = {}
        
        # create the directory if it didn't exist already
        os.mkdir(cwd + '\data')
        
    #Initialize the pygame modules
    pygame.init()
    pygame.mixer.init() # for music
    
    #Get the resolution, and then the width and height of the user's current screen
    resolution = pg.size()
    reso_width = resolution[0]; reso_height = resolution[1]
    
    #Set the canvas for the window
    canvas = pygame.display.set_mode((reso_width,reso_height))
    
    #Set the canvas for the window
    canvas = pygame.display.set_mode((reso_width, reso_height))
    
    #Set the title for the window
    pygame.display.set_caption('Tetris')
    
    #Find the image for the icon and set the icon
    icon = pygame.image.load(cwd + r'\images\icon.png').convert_alpha()
    pygame.display.set_icon(icon)
    
    #Find an image for the background
    background_image = pygame.image.load(cwd + r'\images\background.png').convert_alpha()

    #Scale the background_image and then set the image on the window / canvas
    background_width = background_image.get_width()
    background_height = background_image.get_height()
    background_image = pygame.transform.scale(background_image, (int(background_width * (reso_width/258.7078652)), int(background_height * (reso_height/199.2307692))))
    
    #Find the image for the title background
    title_rectangle_image = pygame.image.load(cwd + r'\images\title_rectangle.png').convert_alpha()
    
    #Scale the title_background_iage and then set the image on the window / canvas
    title_rectangle_width = title_rectangle_image.get_width()
    title_rectangle_height = title_rectangle_image.get_height()
    title_rectangle_image = pygame.transform.scale(title_rectangle_image, (int(title_rectangle_width * (reso_width/736.8)), int(title_rectangle_height * (reso_height/518))))
    
    #Find the image for the top 3 scores background
    top_3_scores_rectangle_image = pygame.image.load(cwd + r'\images\top_3_scores_rectangle.png').convert_alpha()
    
    #Scale the top_3_scores_background_image and then set the image on the window / canvas
    top_3_scores_rectangle_width = top_3_scores_rectangle_image.get_width()
    top_3_scores_rectangle_height = top_3_scores_rectangle_image.get_height()
    top_3_scores_rectangle_image = pygame.transform.scale(top_3_scores_rectangle_image, (int(top_3_scores_rectangle_width * (reso_width/1473.6)), int(top_3_scores_rectangle_height * (reso_height/828.8))))
    
    #Find the image for the highest score background
    high_score_rectangle_image = pygame.image.load(cwd + r'\images\high_score_rectangle.png').convert_alpha()
    
    #Scale the high_score_rectangle_image and then set the image on the window / canvas
    high_score_rectangle_width = high_score_rectangle_image.get_width()
    high_score_rectangle_height = high_score_rectangle_image.get_height()
    high_score_rectangle_image = pygame.transform.scale(high_score_rectangle_image, (int(high_score_rectangle_width * (reso_width/1228)), int(high_score_rectangle_height * (reso_height/690.6666667))))
    
    #Find the image for the blank background
    blank_rectangle_image = pygame.image.load(cwd + r'\images\blank_rectangle.png').convert_alpha()
    
    #Scale the blank_rectangle_image and then set the image on the window / canvas
    blank_rectangle_width = blank_rectangle_image.get_width()
    blank_rectangle_height = blank_rectangle_image.get_height()
    blank_rectangle_image = pygame.transform.scale(blank_rectangle_image, (int(blank_rectangle_width * (reso_width/1473.6)), int(blank_rectangle_height * (reso_height/828.8))))
    blank_rectangle_image2 = pygame.transform.scale(blank_rectangle_image, (int(blank_rectangle_width * (reso_width/334.9090909)), int(blank_rectangle_height * (reso_height/188.3636364)))) #for the add users
    
    #Find the image for the current user background
    current_user_rectangle_image = pygame.image.load(cwd + r'\images\current_user_rectangle.png').convert_alpha()
    
    #Scale the current_user_rectangle_image and then set the image on the window / canvas
    current_user_rectangle_width = current_user_rectangle_image.get_width()
    current_user_rectangle_height = current_user_rectangle_image.get_height()
    current_user_rectangle_image = pygame.transform.scale(current_user_rectangle_image, (int(current_user_rectangle_width * (reso_width/1473.6)), int(current_user_rectangle_height * (reso_height/714.4827586))))
    #Duplicate it for the current_user image in the user stats window
    current_user_rectangle_image2 = pygame.transform.scale(current_user_rectangle_image, (int(current_user_rectangle_width * (reso_width/1228)), int(current_user_rectangle_height * (reso_height/690.6666667))))
    
    #Find the image for the current score, level, and lines background
    score_rectangle_image = pygame.image.load(cwd + r'\images\best_score_rectangle.png').convert_alpha()
    level_rectangle_image = pygame.image.load(cwd + r'\images\best_level_rectangle.png').convert_alpha()
    lines_rectangle_image = pygame.image.load(cwd + r'\images\best_lines_rectangle.png').convert_alpha()
    
    #Scale the current_user_rectangle_image and then set the image on the window / canvas
    score_rectangle_width = score_rectangle_image.get_width() ; level_rectangle_width = level_rectangle_image.get_width() ; lines_rectangle_width = lines_rectangle_image.get_width()
    score_rectangle_height = score_rectangle_image.get_height() ; level_rectangle_height = level_rectangle_image.get_height() ; lines_rectangle_height = lines_rectangle_image.get_height()
    score_rectangle_image = pygame.transform.scale(score_rectangle_image, (int(score_rectangle_width * (reso_width/1228)), int(score_rectangle_height * (reso_height/690.6666667))))
    score_rectangle_image2 = pygame.transform.scale(score_rectangle_image, (int(score_rectangle_width * (reso_width/1473.6)), int(score_rectangle_height * (reso_height/714.4827586)))) #DUPLICATE FOR DESIGN
    level_rectangle_image = pygame.transform.scale(level_rectangle_image, (int(level_rectangle_width * (reso_width/1228)), int(level_rectangle_height * (reso_height/690.6666667))))
    lines_rectangle_image = pygame.transform.scale(lines_rectangle_image, (int(lines_rectangle_width * (reso_width/1228)), int(lines_rectangle_height * (reso_height/690.6666667))))
    
    #Find the image for the current colors background
    current_colors_rectangle_image = pygame.image.load(cwd + r'\images\current_colors_rectangle.png').convert_alpha()
    
    #Scale the blank_rectangle_image and then set the image on the window / canvas
    current_colors_rectangle_width = current_colors_rectangle_image.get_width()
    current_colors_rectangle_height = current_colors_rectangle_image.get_height()
    current_colors_rectangle_image = pygame.transform.scale(current_colors_rectangle_image, (int(current_colors_rectangle_width * (reso_width/1473.6)), int(current_colors_rectangle_height * (reso_height/828.8))))
    
    #Find the images for all of the buttons
    play_button_image = pygame.image.load(cwd + r'\images\play_button.png').convert_alpha()
    quit_button_image = pygame.image.load(cwd + r'\images\quit_button.png').convert_alpha()
    menu_button_image = pygame.image.load(cwd + r'\images\menu_button.png').convert_alpha()
    play_again_button_image = pygame.image.load(cwd + r'\images\play_again_button.png').convert_alpha()
    yes_button_image = pygame.image.load(cwd + r'\images\yes_button.png').convert_alpha()
    no_button_image = pygame.image.load(cwd + r'\images\no_button.png').convert_alpha()
    pause_button_image = pygame.image.load(cwd + r'\images\pause_button.png').convert_alpha()
    resume_button_image = pygame.image.load(cwd + r'\images\resume_button.png').convert_alpha()
    next_song_button_image = pygame.image.load(cwd + r'\images\next_song_button.png').convert_alpha()
    change_user_button_image = pygame.image.load(cwd + r'\images\change_user_button.png').convert_alpha()
    blank_button_image = pygame.image.load(cwd + r'\images\blank_button.png').convert_alpha()
    add_user_button_image = pygame.image.load(cwd + r'\images\add_user_button.png').convert_alpha()
    delete_user_button_image = pygame.image.load(cwd + r'\images\delete_user_button.png').convert_alpha()
    user_stats_button_image = pygame.image.load(cwd + r'\images\user_stats_button.png').convert_alpha()
    edit_name_button_image = pygame.image.load(cwd + r'\images\edit_name_button.png').convert_alpha()
    change_colors_button_image = pygame.image.load(cwd + r'\images\change_colors_button.png').convert_alpha()
    use_shadow_button_image = pygame.image.load(cwd + r'\images\use_shadow_button.png').convert_alpha()
    
    #Instances for the buttons
    play_button = TBs.Button(round(reso_width/2.316981132), round(reso_height/2.59), play_button_image, ((reso_width/1842 + reso_height/1036)/2))
    quit_button = TBs.Button(round(reso_width/2.316981132), round(reso_height/1.883636364), quit_button_image, ((reso_width/1842 + reso_height/1036)/2))
    menu_button = TBs.Button(round(reso_width/2.970967742), round(reso_height/1.328205128), menu_button_image, ((reso_width/1842 + reso_height/1036)/2))
    play_again_button = TBs.Button(round(reso_width/1.805882353), round(reso_height/1.328205128), play_again_button_image, ((reso_width/1842 + reso_height/1036)/2))
    yes_button = TBs.Button(round(reso_width/3.231578947), round(reso_height/2.072), yes_button_image, ((reso_width/1842 + reso_height/1036)/2))
    no_button = TBs.Button(round(reso_width/1.959574468), round(reso_height/2.072), no_button_image, ((reso_width/1842 + reso_height/1036)/2))
    pause_button = TBs.Button(round(reso_width/1.7055555556), round(reso_height/1.263414634), pause_button_image, ((reso_width/1842 + reso_height/1036)/2))
    resume_button = TBs.Button(round(reso_width/2.423684211), round(reso_height/2.302222222), resume_button_image, ((reso_width/1842 + reso_height/1036)/2))
    next_song_button = TBs.Button(round(reso_width/1.279166667), round(reso_height/1.263414634), next_song_button_image, ((reso_width/1842 + reso_height/1036)/2))
    change_user_button = TBs.Button(round(reso_width/1.359409594), round(reso_height/2.496385542), change_user_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb1 = TBs.Button(round(reso_width/18.42), round(reso_height/20.72), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb2 = TBs.Button(round(reso_width/3.508571429), round(reso_height/20.72), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb3 = TBs.Button(round(reso_width/1.938947368), round(reso_height/20.72), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb4 = TBs.Button(round(reso_width/1.339636364), round(reso_height/20.72), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb5 = TBs.Button(round(reso_width/18.42), round(reso_height/2.96), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb6 = TBs.Button(round(reso_width/3.508571429), round(reso_height/2.96), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb7 = TBs.Button(round(reso_width/1.938947368), round(reso_height/2.96), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb8 = TBs.Button(round(reso_width/1.339636364), round(reso_height/2.96), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb9 = TBs.Button(round(reso_width/18.42), round(reso_height/1.593846154), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb10 = TBs.Button(round(reso_width/3.508571429), round(reso_height/1.593846154), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb11 = TBs.Button(round(reso_width/1.938947368), round(reso_height/1.593846154), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    bb12 = TBs.Button(round(reso_width/1.339636364), round(reso_height/1.593846154), blank_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    add_user_button = TBs.Button(round(reso_width/3.542307692), round(reso_height/1.295), add_user_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    menu_button2 = TBs.Button(round(reso_width/21.67058824), round(reso_height/1.295), menu_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    delete_user_button = TBs.Button(round(reso_width/1.928795812), round(reso_height/1.295), delete_user_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    user_stats_button = TBs.Button(round(reso_width/1.359409594), round(reso_height/1.741176471), user_stats_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    menu_button3 = TBs.Button(round(reso_width/2.423684211), round(reso_height/1.279012346), menu_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    edit_name_button = TBs.Button(round(reso_width/1.359409594), round(reso_height/20.72), edit_name_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    change_colors_button = TBs.Button(round(reso_width/1.842), round(reso_height/-51.8), change_colors_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    use_shadow_button = TBs.Button(round(reso_width/1.359409594), round(reso_height/1.336774194), use_shadow_button_image, ((reso_width/1473.6 + reso_height/828.8)/2))
    
    #Set variables for all of the sounds in the game
    shift_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\01shift.ogg')
    buttons_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\02buttons.ogg')
    countdown_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\03countdown.ogg')
    down_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\04down.ogg')
    level_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\05level.ogg')
    lines_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\06lines.ogg')
    rotate_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\07rotate.ogg')
    tetris_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\08tetris.ogg')
    game_over_sound = pygame.mixer.Sound(cwd + r'\sound\sfx\09game_over.ogg')
    game_music = pygame.mixer.music.load(cwd + r'\sound\music\01game_music.mp3')
    
    #Set variables before entering any loops
    finished = False
    dimensions = [(reso_width/38.53556485), (reso_height/21.67364017)]
    clock = pygame.time.Clock()
    reset_variables = False
    again = False
    song = '01'
    current_user = 'Guest'
    block_colors = 0
    use_shadow = False
    
    #Loop until the user chooses to leave the game
    while not finished:
        
        #Constantly set the background for the canvas
        canvas.blit(background_image, (0,0))
        
        #Constantly draw the background image for the title on the canvas
        canvas.blit(title_rectangle_image, (round(reso_width/3.148717949),round(reso_height/11.51111111)))
        
        #Constantly draw the background image for the high_score on the canvas
        canvas.blit(high_score_rectangle_image, (round(reso_width/2.558333333),round(reso_height/1.48)))
        
        #Constantly draw the background image for the top_3_scores on the canvas
        canvas.blit(top_3_scores_rectangle_image, (round(reso_width/18.42),round(reso_height/6.906666667)))
        
        #Constantly draw the background image for the top 3 scores on the canvas
        canvas.blit(blank_rectangle_image, (round(reso_width/18.42),round(reso_height/3.187692308)))
        canvas.blit(blank_rectangle_image, (round(reso_width/18.42),round(reso_height/2.072)))
        canvas.blit(blank_rectangle_image, (round(reso_width/18.42),round(reso_height/1.534814815)))
        
        #Constantly draw the top three players in the game
        TO.top_3_players(canvas, data_dict, reso_width, reso_height)
        
        #Constantly draw the background image for the current_user on the canvas
        canvas.blit(current_user_rectangle_image, (round(reso_width/1.364444444),round(reso_height/4.933333333)))
        
        #Constantly draw the current user's name on the canvas IF they're still in the canvas
        change_to_guest = True
        for player in data_dict:
            if data_dict[player][0] == current_user:
                change_to_guest = False
        if change_to_guest: current_user = 'Guest'
        TO.display_user(canvas, current_user, round(reso_width/1.203921569), round(reso_height/3.635087719), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
        if current_user != 'Guest':
            #If the user clicks the 'edit name' button
            if edit_name_button.draw(canvas, buttons_sound):
                data_dict, current_user = TO.edit_name(current_user, data_dict, canvas, background_image, blank_rectangle_image2, reso_width, reso_height)
        
        #If the user clicks the 'change user' button
        if change_user_button.draw(canvas, buttons_sound):
            current_user = TO.change_user(current_user_rectangle_image, menu_button2, blank_rectangle_image2, add_user_button, delete_user_button, current_user, data_dict, background_image, canvas, buttons_sound, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bb11, bb12, reso_width, reso_height)
            #Save the dictionary every time
            infile = open(cwd + r'\data\Tetris_User_Info', 'wb')
            pickle.dump(data_dict, infile)
            infile.close()
            
            # check to see whether the user with the highest score was deleted
            
            change_highscore = True
            for player in data_dict:
                if data_dict[player][1] == current_highscore: change_highscore = False
            
            # if so, then find out which player has the new highest score
            current_highscore = 0
            for player in data_dict:
                if data_dict[player][1] > current_highscore: current_highscore = data_dict[player][1]
            
        #If the user clicks the 'user stats' button
        if user_stats_button.draw(canvas, buttons_sound):
            TO.display_stats(buttons_sound, menu_button3, current_user_rectangle_image2, score_rectangle_image, level_rectangle_image, lines_rectangle_image, background_image, current_user, data_dict, canvas, reso_width, reso_height)
        
        #If the user clicks the 'change colors' button
        if change_colors_button.draw(canvas, buttons_sound):
            if block_colors == 0: block_colors += 1 # change to all green with black background
            elif block_colors == 1: block_colors += 1 # change to all blue with black background
            elif block_colors == 2: block_colors += 1 # change to all red with black background
            elif block_colors == 3: block_colors += 1 # change to all teel with black background
            elif block_colors == 4: block_colors += 1 # change to all yellow with black background
            elif block_colors == 5: block_colors += 1 # change to all orange with black background
            elif block_colors == 6: block_colors += 1 # change to all purple with black background
            elif block_colors == 7: block_colors += 1 # change to all whie with black background
            elif block_colors == 8: block_colors += 1 # change to all black with white background
            elif block_colors == 9: block_colors += 1 # change to christmas colors with black background
            elif block_colors == 10: block_colors += 1 # change to halloween colors with white background
            elif block_colors == 11: block_colors = 0 # change to normal
            
            #Change the block color in the Tetris_Shapes file as well
            TS.change_block_color(block_colors)
        
        #Find the length of the highscore
        if current_highscore > 999999:
            x = round(reso_width/2.288198758)
        elif current_highscore > 99999:
            x = round(reso_width/2.232727273)
        elif current_highscore > 9999:
            x = round(reso_width/2.192857143)
        elif current_highscore > 999:
            x = round(reso_width/2.141860465)
        elif current_highscore > 99:
            x = round(reso_width/2.093181818)
        elif current_highscore > 9:
            x = round(reso_width/2.046666667)
        elif current_highscore > -1:
            x = round(reso_width/2.002173913)
        
        #Constantly draw the highscore based on its length
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(current_highscore),True,(0,0,0))),(x,round(reso_height/1.336774194)))
        
        #Draw the rectangle background for the current colors rectangle
        canvas.blit(current_colors_rectangle_image, (round(reso_width/3.508571429),round(reso_height/-51.8)))
        
        #Draw the text on the current colors rectangle
        TO.display_current_color(canvas, block_colors, reso_width, reso_height)
        
        #Display the use_shadow button for the user
        if use_shadow_button.draw(canvas, buttons_sound):
            if use_shadow: use_shadow = False
            elif not use_shadow: use_shadow = True
            
        #Based on the boolean variable, use_shadow, display text
        if use_shadow: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('On',True,(0,0,0))),(round(reso_width/1.236241611),round(reso_height/1.23333333)))
        elif not use_shadow: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Off',True,(0,0,0))),(round(reso_width/1.236241611),round(reso_height/1.23333333)))
        
        #Reset / Set variables for the game here
        beginning = True
        won = False
        shapes_on_board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] #20 rows in total
        shape_counter = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        
        #If the user clicks the play button
        if play_button.draw(canvas, buttons_sound) or again:
            
            #Reset the again variable
            again = False
            
            #If beginning is true, then find the first two shapes that will be used
            if beginning:
                shape1, shape_counter = TS.shape_selecter(shape_counter)
                shape2, shape_counter = TS.shape_selecter(shape_counter)
                shapes = [shape1,shape2]
                beginning = False
                
            #If the user entered the game before, then reset colors_on_board
            if reset_variables:
                reset_variables = False
                TBd.reset_variables()
                
            #Constantly draw the entire board
            TBd.draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height)
                
            #ADD A GRAY TRANSPARENT BACKGROUND HERE
            # ///
            transparent = pygame.Surface((reso_width,reso_height))  # the size of your rect
            transparent.set_alpha(128)                # alpha level
            transparent.fill((56,56,56))           # this fills the entire surface
            # ///
                
            #Update the screen
            pygame.display.update()
            
            #Find the user's best score
            best_score = 0
            for player in data_dict:
                if data_dict[player][0] == current_user:
                    best_score = data_dict[player][1]
                    
            if best_score != 0:
            #Find the length of the highscore
                if best_score > 999999:
                    x_best = round(reso_width/1.16214511) - round(reso_width/15.35)
                elif best_score > 99999:
                    x_best = round(reso_width/1.16214511) - round(reso_width/18.42)
                elif best_score > 9999:
                    x_best = round(reso_width/1.16214511) - round(reso_width/23.025)
                elif best_score > 999:
                    x_best = round(reso_width/1.16214511) - round(reso_width/30.7)
                elif best_score > 99:
                    x_best = round(reso_width/1.16214511) - round(reso_width/46.05)
                elif best_score > 9:
                    x_best = round(reso_width/1.16214511) - round(reso_width/92.1)
                elif best_score > -1:
                    x_best = round(reso_width/1.16214511) - 0
            else: x_best = round(reso_width/1.16214511)
            
            #Create a countdown
            for seconds in reversed(range(1, 4)):
                if next_song_button.draw(canvas, buttons_sound): pass # for designs
                if pause_button.draw(canvas, buttons_sound): pass # for designs
                canvas.blit(current_user_rectangle_image, (round(reso_width/1.292631579),round(reso_height/8.633333333))) # draw the current user rectangle
                TO.display_user(canvas, current_user, round(reso_width/1.147663551), round(reso_height/5.312820513), round((reso_width/23.025 + reso_height/12.95)/2), reso_width) #draw the user's name
                canvas.blit(score_rectangle_image2, (round(reso_width/1.292631579), round(reso_height/-20.72))) # draw the current user's best score rectangle
                canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(best_score),True,(0,0,0))),(x_best,round(reso_height/41.44))) # draw the user's best score
                canvas.blit(transparent, (0,0)) # draw transparency
                canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/7.675 + reso_height/4.316666667)/2))).render(str(seconds),True,(0,0,0))),(round(reso_width/2.002173913),round(reso_height/2.59)))
                pygame.display.update() # update screen before waiting
                pygame.mixer.Sound.play(countdown_sound) # play the sound effect
                time.sleep(1) # wait
                canvas.blit(background_image, (0,0)) # draw background
                TBd.draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height) # draw the board
            
            #After the countown, begin playing the music until the game is over
            pygame.mixer.music.play(-1)
            
            #Reset / Create the variable for the next loop
            done = False
            
            #Loop until the game is over /// THIS IS WHERE THE GAME WILL BE RUNNING
            while not done:
                
                #Get the starting position of the shape and it's color
                locations, color = TS.initial_information(shapes[0], block_colors, reso_width, reso_height)
                
                #Set the variables for the current time and the time ticks
                current_time = pygame.time.get_ticks()
                time_ticks = pygame.time.get_ticks()
                
                #If the user hasn't won yet enter the next loop (won == shape hits the top)
                if not won:
                    
                    #Reset / the boolean variable and rotation
                    next_shape = False
                    rotation = 0
                    
                    #Loop until the user moves onto the next shape
                    while not next_shape:
                        
                        #Check for keys being pressed. Store them in keys
                        keys = pygame.key.get_pressed()
                        
                        #Constantly draw the board and other contents on the board
                        TBd.draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height)
                        canvas.blit(current_user_rectangle_image, (round(reso_width/1.292631579),round(reso_height/8.63333333)))
                        TO.display_user(canvas, current_user, round(reso_width/1.147663551), round(reso_height/5.312820513), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
                        canvas.blit(score_rectangle_image2, (round(reso_width/1.292631579), round(reso_height/-20.72))) # draw the current user's best score rectangle
                        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(best_score),True,(0,0,0))),(x_best,round(reso_height/41.44))) # draw the user's best score
                        
                        #Constantly draw the shape (shapes[1]) in the batter's box
                        TS.batter_box(dimensions, shapes[1], block_colors, canvas, reso_width, reso_height)
                            
                        #the current shape on the board, check to see if it needs to be moved down
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
                                if location[1] == (round(reso_height/22.04255319) * 20): # UNCHANGED
                                    next_shape = True
                            
                            #If the shape did collide with something, move the shape back up one block and go to the next shape
                            if next_shape:
                                for location in locations:
                                    location[1] -= round(reso_height/22.04255319)
                            
                            #If so, then update time_ticks
                            time_ticks = pygame.time.get_ticks()
                            
                        #Update the current_time
                        current_time = pygame.time.get_ticks()
                        
                        #reset the down variable when they let go of the down key
                        if not k.is_pressed('DOWN'): down_playsound = True
                        
                        #Check to see if the user presses either of the arrow keys to rotate the shape AND while there isn't a next_shape needed
                        if k.is_pressed('r') or k.is_pressed('LEFT') or k.is_pressed('DOWN') or k.is_pressed('RIGHT') and not next_shape:
                            
                            #Find out which key is being held. Pass the current_time and time_ticks to keep the blocks moving
                            key, locations, current_time, time_ticks = TS.keyboard_action(use_shadow, block_colors, current_time, time_ticks, clock, locations, shapes_on_board, shapes, background_image, color, canvas, buttons_sound, pause_button, next_song_button, current_user_rectangle_image, current_user, best_score, score_rectangle_image2, x_best, reso_width, reso_height)
                            
                            #Play the down sound effect
                            if key == 'down' and down_playsound:
                                pygame.mixer.Sound.play(down_sound) # play the sound effect
                                down_playsound = False # change the boolean variable
                            
                            #Call a certain function based on the key that was being pressed
                            if key == 'rotate' and not next_shape:
                                locations, rotation = TS.rotate(shapes[0], locations, color, rotation, shapes_on_board, canvas, reso_width, reso_height)
                                pygame.mixer.Sound.play(rotate_sound) # play the sound effect
                                
                            elif key == 'right' or key == 'left' and not next_shape:
                                locations = TS.horizontal(key, locations, color, shapes_on_board, canvas, reso_width, reso_height)
                                pygame.mixer.Sound.play(shift_sound) # play the sound effect
                                
                            elif key == 'down' and not next_shape:
                                locations = TS.down(use_shadow, block_colors, clock, color, locations, shapes_on_board, background_image, shapes[1], canvas, buttons_sound, pause_button, next_song_button, current_user_rectangle_image, current_user, best_score, score_rectangle_image2, x_best, reso_width, reso_height)
                                    
                        #draw the current shape on the board AND it's shadow if user wanted to
                        TS.draw_shape(dimensions, locations, color, canvas)
                        if use_shadow: TBd.shape_shadow(locations, shapes_on_board, block_colors, canvas, reso_width, reso_height)
                                
                        #Check to see if any shape in shapes_on_board is making contact with the top of the board
                        if len(shapes_on_board[0]) > 0:
                            next_shape = True
                            won = True
                            reset_variables = True
                        
                        #If the user presses the pause button
                        if pause_button.draw(canvas, buttons_sound):
                            pygame.mixer.Sound.play(buttons_sound) # play the sound effect
                            more_loops = True
                            
                            #Draw the other buttons that are on the screen for show
                            if next_song_button.draw(canvas, buttons_sound): pass
                            
                            canvas.blit(transparent, (0,0)) # draw transparency
                            #Draw the leaving rectangle
                            pygame.draw.rect(canvas, (0,0,0), pygame.Rect(round(reso_width/3.349090909), round(reso_height/4.144), round(reso_width/2.631428571), round(reso_height/2.59)))
                            pygame.draw.rect(canvas, (25,140,255), pygame.Rect(round(reso_width/3.349090909), round(reso_height/4.144), round(reso_width/2.631428571), round(reso_height/2.59)), 2)
                            canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/15.35 + reso_height/8.6333333333)/2))).render('Paused',True,(255,255,255))),(round(reso_width/2.456),round(reso_height/3.139393939)))
                            
                            while more_loops:
                                
                                #If they press the no button
                                if resume_button.draw(canvas, buttons_sound):
                                    pygame.mixer.Sound.play(buttons_sound) # play the sound effect
                                    more_loops = False
                                
                                #Create a loop to check for events
                                for event in pygame.event.get():
                                    
                                    #Check to see if the user clicks the 'X' button
                                    if event.type == pygame.QUIT:
                                        more_loops = False
                                
                                #Update the screen
                                pygame.display.update()
                                
                        #Create a loop to check for events
                        for event in pygame.event.get():
                            
                            #Check to see if the user clicks the 'X' button
                            if event.type == pygame.QUIT:
                                pygame.mixer.Sound.play(buttons_sound) # play the sound effect
                                
                                #Draw the other buttons for show
                                if next_song_button.draw(canvas, buttons_sound): pass
                                
                                canvas.blit(transparent, (0,0)) # draw transparency
                                #Draw the leaving rectangle
                                pygame.draw.rect(canvas, (0,0,0), pygame.Rect(round(reso_width/3.349090909), round(reso_height/4.144), round(reso_width/2.631428571), round(reso_height/2.59)))
                                pygame.draw.rect(canvas, (25,140,255), pygame.Rect(round(reso_width/3.349090909), round(reso_height/4.144), round(reso_width/2.631428571), round(reso_height/2.59)), 2)
                                canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/15.35 + reso_height/8.6333333333)/2))).render('Are you sure?',True,(255,255,255))),(round(reso_width/2.9472),round(reso_height/3.139393939)))
                                
                                #Enter another loop, asking the user if they really want to leave
                                more_loops = True
                                while more_loops:
                                    
                                    #If they press the no button
                                    if no_button.draw(canvas, buttons_sound):
                                        pygame.mixer.Sound.play(buttons_sound) # play the sound effect
                                        more_loops = False
                                    
                                    #If they press the yes button
                                    if yes_button.draw(canvas, buttons_sound):
                                        pygame.mixer.Sound.play(buttons_sound) # play the sound effect
                                        won = True
                                        next_shape = True
                                        reset_variables = True
                                        more_loops = False
                                        
                                    #Create a loop to check for events
                                    for event1 in pygame.event.get():
                                        
                                        #Check to see if the user clicks the 'X' button
                                        if event1.type == pygame.QUIT:
                                            won = True
                                            next_shape = True
                                            reset_variables = True
                                            pygame.mixer.Sound.play(buttons_sound) # play the sound effect
                                            more_loops = False
                                        
                                    #Update the screen
                                    pygame.display.update()
                        
                        #If the user pressed the "next song" button
                        if next_song_button.draw(canvas, buttons_sound):
                            pygame.mixer.music.stop()
                            song = TO.next_song(song)
                            game_music = pygame.mixer.music.load(cwd + r'\sound\music\\' + song + 'game_music.mp3')
                            pygame.mixer.music.play(-1)
                        
                        #Update the screen
                        pygame.display.update()
                        clock.tick(60) #60 for 60 frames
                        
                        #Check for completed rows and update the board
                        shapes_on_board = TBd.remove_lines(shapes_on_board, background_image, canvas, lines_sound, level_sound, tetris_sound, reso_width, reso_height)
                        
                        #If new_shape is true, then add the shape to the board / Update shapes_on_board IF the game isn't over
                        if next_shape:
                            shapes_on_board = TBd.add_shapes(color, shapes[0], locations, shapes_on_board, reso_height)
                        
                    #Select the next current shape a random shape to go into the batter's box IF the game isn't over
                    if not won:
                        upcoming_shape, shape_counter = TS.shape_selecter(shape_counter)
                        shapes[0] = shapes[1] ; shapes[1] = upcoming_shape
                    
                else:
                    
                    #Once the game is over, stop the music and play the game over sound
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(game_over_sound)
                    
                    #Get all of the numbers from the game
                    score, level, lines = TBd.get_statistics()
                    
                    #Check to see if the score was a personal highscore
                    personal_highscore = False
                    for player in data_dict:
                        if data_dict[player][0] == current_user:
                            if score > data_dict[player][1]: personal_highscore = True
                    
                    #Then, update the user's data
                    data_dict = TO.update_data(current_user, data_dict)
                    
                    #Update the file
                    infile = open(cwd + r'\data\Tetris_User_Info', 'wb')
                    pickle.dump(data_dict, infile)
                    infile.close()
                    
                    # draw the board again and other contents on the board
                    TBd.draw_board(shapes_on_board, background_image, canvas, reso_width, reso_height)
                    canvas.blit(current_user_rectangle_image, (round(reso_width/1.292631579),round(reso_height/8.63333333)))
                    TO.display_user(canvas, current_user, round(reso_width/1.147663551), round(reso_height/5.312820513), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
                    canvas.blit(score_rectangle_image2, (round(reso_width/1.292631579), round(reso_height/-20.72))) # draw the current user's best score rectangle
                    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(best_score),True,(0,0,0))),(x_best,round(reso_height/41.44))) # draw the user's best score
                    
                    #draw the shape (shapes[1]) in the batter's box
                    TS.batter_box(dimensions, shapes[1], block_colors, canvas, reso_width, reso_height)
                    
                    #Draw the other buttons for show
                    if next_song_button.draw(canvas, buttons_sound): pass
                    if pause_button.draw(canvas, buttons_sound): pass
                    
                    #Cover the screen with a transparent dark gray color
                    transparent.fill((0,0,0))
                    canvas.blit(transparent, (0,0)) # draw transparency
                    canvas.blit(transparent, (0,0)) # draw transparency
                    canvas.blit(transparent, (0,0)) # draw transparency
                    
                    #If the user's score that game was higher than the previous high score, then change it
                    new_highscore = False
                    if score > current_highscore: current_highscore = score ; new_highscore = True
                    
                    #Show all of the texts that will apear on the screen
                    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/8.008695652 + reso_height/4.504347826)/2))).render('Game Over!',True,(255,255,255))),(round(reso_width/3.8375),round(reso_height/34.533333333)))
                    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/16.74545455 + reso_height/9.418181818)/2))).render(f'Score : {score}',True,(255,255,255))),(round(reso_width/3.019672131),round(reso_height/3.4533333333)))
                    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/16.74545455 + reso_height/9.418181818)/2))).render(f'Level : {level}',True,(255,255,255))),(round(reso_width/3.019672131),round(reso_height/2.072)))
                    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/16.74545455 + reso_height/9.418181818)/2))).render(f'Lines : {lines}',True,(255,255,255))),(round(reso_width/3.019672131),round(reso_height/1.48)))
                    
                    #Create variables for the breezing effect
                    change = True ; value = 1 ; a1 = 0 ; a2 = 225 ; a3 = 225
                    
                    #After the game is over, show the data to the user
                    while not done:
                        
                        #If there is a new highscore, then show extra text
                        if new_highscore:
                            
                            #Get RGB values
                            a1, a2, a3, value, change = TBd.get_rgb(value, change, a1, a2, a3)
                            canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/14.736 + reso_height/8.288)/2))).render('New High Score!',True,(a1,a2,a3))),(round(reso_width/3.019672131),round(reso_height/5.452631579)))
                            
                        #If there was a personal highscore instead
                        elif personal_highscore:
                            
                            #Get RGB values
                            a1, a2, a3, value, change = TBd.get_rgb(value, change, a1, a2, a3)
                            canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/14.736 + reso_height/8.288)/2))).render('New Personal High Score!',True,(a1,a2,a3))),(round(reso_width/4.385714286),round(reso_height/5.452631579)))
                        
                        #Prove the user with two buttons
                        if menu_button.draw(canvas, buttons_sound):
                            done = True
                            
                        if play_again_button.draw(canvas, buttons_sound):
                            done = True
                            again = True
                        
                        #Check for if the user presses the 'X' button
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                done = True
                        
                        pygame.display.update()
                        
                
        #If the user clicks the quit button
        if quit_button.draw(canvas, buttons_sound):
            finished = True
            
        #Create a loop to check for events
        for event in pygame.event.get():
            
            #Check to see if the user clicks the 'X' button
            if event.type == pygame.QUIT:
                finished = True
                
        #Update the screen
        pygame.display.update()
                
    #Update the screen
    pygame.display.update()
    
    #Close pygame
    pygame.quit()
    
tetris()