#Imports
import pygame
from keyboard import is_pressed as k
import keyboard
import modules.Tetris_Board as TBd

#===========================================================================#
#===========================================================================#
#===========================================================================#

def next_song(current_song):
    
    #Check the current_song that is playing
    if current_song == '01':
        return '02'
    if current_song == '02':
        return '03'
    if current_song == '03':
        return '04'
    if current_song == '04':
        return '05'
    if current_song == '05':
        return '01'

#===========================================================================#
#===========================================================================#
#===========================================================================#
    
def top_3_players(canvas, data_dict, reso_width, reso_height):
    
    #Check to see if there are more than 2 top players
    if len(data_dict) > 0:
        
        #Check for the top three players
        all_scores = []
        for player in data_dict:
            all_scores.append(data_dict[player][1])
        all_scores.sort() ; all_scores.reverse()
        
    #Check to see if there are no players in the dictionary at all
    elif len(data_dict) == 0:
        for y in range(round(reso_height/2.59), round(reso_height/1.381333333) + 1, round(reso_height/5.92)):
            canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('None',True,(0,0,0))),(round(reso_width/8.771428571),y))
        return
    
    #Loop for all of the names present
    present = 0
    for score in all_scores:
        for player in data_dict:
            if score == data_dict[player][1]:
                
                #Find out the x position of the text
                if len(data_dict[player][0]) > 6:
                    x = round(reso_width/12.28) - round(reso_width/92.1)
                elif len(data_dict[player][0]) > 5:
                    x = round(reso_width/10.83529412) - round(reso_width/92.1)
                elif len(data_dict[player][0]) > 4:
                    x = round(reso_width/9.694736842) - round(reso_width/92.1)
                elif len(data_dict[player][0]) > 3:
                    x = round(reso_width/8.771428571) - round(reso_width/92.1)
                elif len(data_dict[player][0]) > 2:
                    x = round(reso_width/8.008695652) - round(reso_width/92.1)
                elif len(data_dict[player][0]) > 1:
                    x = round(reso_width/7.368) - round(reso_width/92.1)
                elif len(data_dict[player][0]) > 0:
                    x = round(reso_width/6.822222222) - round(reso_width/92.1)
                
                canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render(data_dict[player][0],True,(0,0,0))),(x,(round(reso_height/2.59) + round(reso_height/5.92)*present)))
                present += 1
            if present == 3: return
    
    #Based on the length of present, draw the 'None' text(s)
    for y in reversed(range(round(reso_height/2.59), round(reso_height/1.381333333) + 1, round(reso_height/5.92))):
        if y - (400+175*(present-1)) ==  0: return
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('None',True,(0,0,0))),(round(reso_width/8.771428571),y))
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def display_user(canvas, current_user, x_base, y, size, reso_width):
    
    #Find out the x position of the text
    if len(current_user) > 6:
        x = x_base - round(reso_width/15.35)
    elif len(current_user) > 5:
        x = x_base - round(reso_width/18.42)
    elif len(current_user) > 4:
        x = x_base - round(reso_width/23.025)
    elif len(current_user) > 3:
        x = x_base - round(reso_width/30.7)
    elif len(current_user) > 2:
        x = x_base - round(reso_width/46.05)
    elif len(current_user) > 1:
        x = x_base - round(reso_width/92.1)
    elif len(current_user) > 0:
        x = x_base
        
    #Display the text on the screen
    canvas.blit(((pygame.font.SysFont('Watermelon',size)).render(current_user,True,(55,55,55))),(x,y))
    
#===========================================================================#
#===========================================================================#
#===========================================================================#
    
def update_data(current_user, data_dict):
    
    #Check to see if the user isn't a guest
    if current_user.lower() == 'guest' : return data_dict
    
    #Get the global variables
    score, level, lines = TBd.return_global()
    
    #Find the user in the data dictionary and update their information IF the information is better
    for player in data_dict:
        if data_dict[player][0] == current_user:
            if data_dict[player][1] < score: data_dict[player][1] = score
            if data_dict[player][2] < level: data_dict[player][2] = level
            if data_dict[player][3] < lines: data_dict[player][3] = lines
            break
    
    #Return the dictionary
    return data_dict
    
#===========================================================================#
#===========================================================================#
#===========================================================================#

def change_user(current_user_rectangle_image, menu_button2, blank_rectangle_image2, add_user_button, delete_user_button, current_user, data_dict, background_image, canvas, bs, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bb11, bb12, reso_width, reso_height):
    
    #Display the background image
    canvas.blit(background_image, (0,0)) # draw background
    
    #Loop until the user chooses a user or decides to leave with buttons
    finished = False
    while not finished:
        
        #Set the buttons up
        if bb1.draw(canvas, bs):
            try: current_user = data_dict[1][0]
            except: pass
        elif bb2.draw(canvas, bs):
            try: current_user = data_dict[2][0]
            except: pass
        elif bb3.draw(canvas, bs):
            try: current_user = data_dict[3][0]
            except: pass
        elif bb4.draw(canvas, bs):
            try: current_user = data_dict[4][0]
            except: pass
        elif bb5.draw(canvas, bs):
            try: current_user = data_dict[5][0]
            except: pass
        elif bb6.draw(canvas, bs):
            try: current_user = data_dict[6][0]
            except: pass
        elif bb7.draw(canvas, bs):
            try: current_user = data_dict[7][0]
            except: pass
        elif bb8.draw(canvas, bs):
            try: current_user = data_dict[8][0]
            except: pass
        elif bb9.draw(canvas, bs):
            try: current_user = data_dict[9][0]
            except: pass
        elif bb10.draw(canvas, bs):
            try: current_user = data_dict[10][0]
            except: pass
        elif bb11.draw(canvas, bs):
            try: current_user = data_dict[11][0]
            except: pass
        elif bb12.draw(canvas, bs):
            try: current_user = data_dict[12][0]
            except: pass
        
        #Draw the names inside of each square
        x_base = round(reso_width/7.518367347) ; y = round(reso_height/7.969230769)
        for player in range(1, len(data_dict) + 1):
            
            #Call the previously made function to disapy all of the names
            display_user(canvas, data_dict[player][0], x_base, y, round((reso_width/20.46666667 + reso_height/11.51111111)/2), reso_width)
            
            #Increase the x variable
            x_base += round(reso_width/4.385714286)
            
            #Change the variables at certain points
            if player == 4 or player == 8:
                x_base = round(reso_width/7.518367347)
                y += round(reso_height/3.453333333)
        
        #Check for when the user presses the 'x' button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        
        #If the user presses the menu button
        if menu_button2.draw(canvas, bs):
            finished = True
        
        #Check for when / if the user presses the 'add user' button
        if add_user_button.draw(canvas, bs):
            data_dict = add_user(data_dict, canvas, background_image, blank_rectangle_image2, reso_width, reso_height)
            #Draw the background image
            canvas.blit(background_image, (0,0))
            
        #Check for when / if the user presses the 'delete user' button
        if delete_user_button.draw(canvas, bs):
            add = False ; menu = False
            data_dict, add, menu = delete_user(menu_button2, add_user_button, delete_user_button, data_dict, canvas, bs, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bb11, bb12, reso_width, reso_height)
            #Draw the background image
            canvas.blit(background_image, (0,0))
            
            #Check to see if the user pressed other buttons
            if add:
                data_dict = add_user(data_dict, canvas, background_image, blank_rectangle_image2, reso_width, reso_height)
                #Draw the background image
                canvas.blit(background_image, (0,0))
                
            elif menu:
                finished = True
        
        #Display the current user / selected user
        canvas.blit(current_user_rectangle_image, (round(reso_width/1.334782609),round(reso_height/1.328205128)))
        change_to_guest = True
        for player in data_dict:
            if data_dict[player][0] == current_user:
                change_to_guest = False
        if change_to_guest: current_user = 'Guest'
        display_user(canvas, current_user, round(reso_width/1.180769231), round(reso_height/1.211695906), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
        
        #Update the screen
        pygame.display.update()
        
    return current_user

#===========================================================================#
#===========================================================================#
#===========================================================================#

def add_user(data_dict, canvas, background_image, blank_rectangle_image2, reso_width, reso_height):
    
    #Create variables
    name = ''
    key = ''
    
    #Loop until the user is satisfied with their new name
    finished = False
    while not finished:
        
        #Draw the background image
        canvas.blit(background_image, (0,0))
        
        #Draw the massive rectanle
        canvas.blit(blank_rectangle_image2, (round(reso_width/14.16923077),round(reso_height/34.53333333)))
        
        #Display directions for the user
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Press the enter key to keep the name',True,(0,0,0))),(round(reso_width/4.912),round(reso_height/1.4)))
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Press the backspace key to remove letters',True,(0,0,0))),(round(reso_width/5.667692308),round(reso_height/1.233333333)))
        
        #Get a key from the user
        key = key_checker()
        
        #Make an action happen when the user presses a key
        if key != 'nothing' and key != 'backspace' and key != 'enter':
            if len(name) < 7:
                name += key.upper()
        
        #Delete a letter
        if key == 'backspace':
            if len(name) != 0:
                name = name[:len(name)-1]
        
        #Enter the name
        if key == 'enter' and len(name) > 0:
            
            #Check to see if the name exists in the data_dict already
            for player in data_dict:
                if data_dict[player][0].lower() == name.lower():
                    return data_dict
            if len(data_dict) < 12:
                data_dict[len(data_dict) + 1] = [name, 0, 0, 0]
            return data_dict
        
        #Check the length of the name and create the x variable based on it
        if len(name) == 1:
            x = round(reso_width/2.3052)
        elif len(name) == 2:
            x = round(reso_width/2.3052) - round(reso_width/23.052)
        elif len(name) == 3:
            x = round(reso_width/2.3052) - round(reso_width/23.052)*2
        elif len(name) == 4:
            x = round(reso_width/2.3052) - round(reso_width/23.052)*3
        elif len(name) == 5:
            x = round(reso_width/2.3052) - round(reso_width/23.052)*4
        elif len(name) == 6:
            x = round(reso_width/2.3052) - round(reso_width/23.052)*5
        elif len(name) == 7:
            x = round(reso_width/2.3052) - round(reso_width/23.052)*6
        
        #Constantly draw the name for the user to see
        if len(name) > 0: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/7.084615385 + reso_height/3.984615385)/2))).render(name,True,(0,0,0))),(x,round(reso_height/2.59)))
        
        #Check for when the user presses the 'x' button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return data_dict
            
        #Update the screen
        pygame.display.update()

#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def key_checker():
    
    #Check for keys
    if k('a'): key = 'a'
    elif k('b'): key = 'b'
    elif k('c'): key = 'c'
    elif k('d'): key = 'd'
    elif k('e'): key = 'e'
    elif k('f'): key = 'f'
    elif k('g'): key = 'g'
    elif k('h'): key = 'h'
    elif k('i'): key = 'i'
    elif k('j'): key = 'j'
    elif k('k'): key = 'k'
    elif k('l'): key = 'l'
    elif k('m'): key = 'm'
    elif k('n'): key = 'n'
    elif k('o'): key = 'o'
    elif k('p'): key = 'p'
    elif k('q'): key = 'q'
    elif k('r'): key = 'r'
    elif k('s'): key = 's'
    elif k('t'): key = 't'
    elif k('u'): key = 'u'
    elif k('v'): key = 'v'
    elif k('w'): key = 'w'
    elif k('x'): key = 'x'
    elif k('y'): key = 'y'
    elif k('z'): key = 'z'
    elif k('backspace'): key = 'backspace'
    elif k('enter'): key = 'enter'
    else: return 'nothing'
    
    #Loop until the user lets go of the key
    while k(key): continue
    
    #After they let go of a key, return the key found
    return key
#===========================================================================#
#===========================================================================#
#===========================================================================#

def delete_user(menu_button2, add_user_button, delete_user_button, data_dict, canvas, bs, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bb11, bb12, reso_width, reso_height):
    
    #Once the button was clicked, display text on the screen to direct the user
    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Click on a user to delete',True,(0,0,0))),(round(reso_width/3.203478261),round(reso_height/3.767272727)))
    canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Click the delete button again to cancel',True,(0,0,0))),(round(reso_width/4.605),round(reso_height/1.80173913)))
    
    #Variables before entering the loop
    selected_user = ''
    
    #Enter the loop
    finished = False
    while not finished:
    
    #Set the buttons up
        if bb1.draw(canvas, bs):
            try: selected_user = data_dict[1][0]
            except: pass
        elif bb2.draw(canvas, bs):
            try: selected_user = data_dict[2][0]
            except: pass
        elif bb3.draw(canvas, bs):
            try: selected_user = data_dict[3][0]
            except: pass
        elif bb4.draw(canvas, bs):
            try: selected_user = data_dict[4][0]
            except: pass
        elif bb5.draw(canvas, bs):
            try: selected_user = data_dict[5][0]
            except: pass
        elif bb6.draw(canvas, bs):
            try: selected_user = data_dict[6][0]
            except: pass
        elif bb7.draw(canvas, bs):
            try: selected_user = data_dict[7][0]
            except: pass
        elif bb8.draw(canvas, bs):
            try: selected_user = data_dict[8][0]
            except: pass
        elif bb9.draw(canvas, bs):
            try: selected_user = data_dict[9][0]
            except: pass
        elif bb10.draw(canvas, bs):
            try: selected_user = data_dict[10][0]
            except: pass
        elif bb11.draw(canvas, bs):
            try: selected_user = data_dict[11][0]
            except: pass
        elif bb12.draw(canvas, bs):
            try: selected_user = data_dict[12][0]
            except: pass
        
        #Draw the names inside of each square
        x_base = round(reso_width/7.518367347) ; y = round(reso_height/7.969230769)
        for player in range(1, len(data_dict) + 1):
            
            #Call the previously made function to disapy all of the names
            display_user(canvas, data_dict[player][0], x_base, y, round((reso_width/20.46666667 + reso_height/11.51111111)/2), reso_width)
            
            #Increase the x variable
            x_base += round(reso_width/4.385714286)
            
            #Change the variables at certain points
            if player == 4 or player == 8:
                x_base = round(reso_width/7.518367347)
                y += round(reso_height/3.453333333)
        
        #After the user presses a button, make an action
        if selected_user != '':
            
            #Find the selected user and remove them
            for player in data_dict:
                if data_dict[player][0] == selected_user:
                    
                    #Check to see if the selected player is at the end of the list
                    if player == len(data_dict):
                        del data_dict[player]
                        return data_dict, False, False
                    
                    data_dict['a'] = data_dict[player]
                    for number in range(player + 1, len(data_dict)):
                       data_dict[number-1] = data_dict[number]
                       del data_dict[number]
                    del data_dict['a']
                    return data_dict, False, False
        
        #Check to see if the user presses the 'x' button
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return data_dict, False, False
            
        #Check to see if the user presses the delete user button again
        if delete_user_button.draw(canvas, bs):
            return data_dict, False, False
        
        #If the user presses the menu button
        if menu_button2.draw(canvas, bs):
            return data_dict, False, True
        
        #If the user presses the add button
        if add_user_button.draw(canvas, bs):
            return data_dict, True, False
        
        #Update the screen
        pygame.display.update()

#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def display_stats(bs, menu_button3, current_user_rectangle_image2, sRi, LeRi, LiRi, background_image, current_user, data_dict, canvas, reso_width, reso_height):
    
    #Get the information about the user
    score = ''
    for player in data_dict:
        if data_dict[player][0] == current_user:
            score = data_dict[player][1]
            level = data_dict[player][2]
            lines = data_dict[player][3]
    
    #Draw the background
    canvas.blit(background_image, (0,0))
    
    #Display the images for each of the boxes
    canvas.blit(current_user_rectangle_image2, (round(reso_width/2.558333333),round(reso_height/103.6)))
    canvas.blit(sRi, (round(reso_width/2.558333333),round(reso_height/4.933333333)))
    canvas.blit(LeRi, (round(reso_width/2.558333333),round(reso_height/2.526829268)))
    canvas.blit(LiRi, (round(reso_width/2.558333333),round(reso_height/1.698360656)))
    
    #If the user wasn't found, do something else
    if score == '':
        display_user(canvas, 'Guest', round(reso_width/2.002173913), round(reso_height/11.51111111), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('0',True,(0,0,0))),(round(reso_width/2.002173913),round(reso_height/3.572413793)))
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('0',True,(0,0,0))),(round(reso_width/2.002173913),round(reso_height/2.114285714)))
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('0',True,(0,0,0))),(round(reso_width/2.002173913),round(reso_height/1.501449275)))
    
    else:
        #Find the x variable for the score
        x = round(reso_width/2.002173913)
        if score > 999999:
            x_score = x - round(reso_width/15.35)
        elif score > 99999:
            x_score = x - round(reso_width/18.42)
        elif score > 9999:
            x_score = x - round(reso_width/23.025)
        elif score > 999:
            x_score = x - round(reso_width/30.7)
        elif score > 99:
            x_score = x - round(reso_width/46.05)
        elif score > 9:
            x_score = x - round(reso_width/92.1)
        elif score > -1:
            x_score = x - 0
            
        if level > 999999:
            x_level = x - round(reso_width/15.35)
        elif level > 99999:
            x_level = x - round(reso_width/18.42)
        elif level > 9999:
            x_level = x - round(reso_width/23.025)
        elif level > 999:
            x_level = x - round(reso_width/30.7)
        elif level > 99:
            x_level = x - round(reso_width/46.05)
        elif level > 9:
            x_level = x - round(reso_width/92.1)
        elif level > -1:
            x_level = x - 0
            
        if lines > 999999:
            x_lines = x - round(reso_width/15.35)
        elif lines > 99999:
            x_lines = x - round(reso_width/18.42)
        elif lines > 9999:
            x_lines = x - round(reso_width/23.025)
        elif lines > 999:
            x_lines = x - round(reso_width/30.7)
        elif lines > 99:
            x_lines = x - round(reso_width/46.05)
        elif lines > 9:
            x_lines = x - round(reso_width/92.1)
        elif lines > -1:
            x_lines = x - 0
        
        #Display the text for all of the boxes
        display_user(canvas, current_user, round(reso_width/2.002173913), round(reso_height/11.51111111), round((reso_width/23.025 + reso_height/12.95)/2), reso_width)
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(score),True,(0,0,0))),(x_score,round(reso_height/3.572413793)))
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(level),True,(0,0,0))),(x_level,round(reso_height/2.114285714)))
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render(str(lines),True,(0,0,0))),(x_lines,round(reso_height/1.501449275)))
    
    #Enter the loop
    finished = False
    while not finished:
        
        #Check for when the user presses the menu button:
        if menu_button3.draw(canvas, bs):
            return
        
        #Check for when the user presses the 'x' button
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            
        #Update the screen
        pygame.display.update()
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def edit_name(current_user, data_dict, canvas, background_image, blank_rectangle_image2, reso_width, reso_height):
    
    #Create variables
    old_name = ''
    name = ''
    key = ''
    for letter in current_user:
        name += letter ; old_name += letter
    
    #Loop until the user is satisfied with their new name
    finished = False
    while not finished:
        
        #Draw the background image
        canvas.blit(background_image, (0,0))
        
        #Draw the massive rectanle
        canvas.blit(blank_rectangle_image2, (round(reso_width/14.16923077),round(reso_height/34.53333333)))
        
        #Display directions for the user
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Press the enter key to keep the name',True,(0,0,0))),(round(reso_width/4.912),round(reso_height/1.4)))
        canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/20.46666667 + reso_height/11.51111111)/2))).render('Press the backspace key to remove letters',True,(0,0,0))),(round(reso_width/5.667692308),round(reso_height/1.233333333)))
        
        #Get a key from the user
        key = key_checker()
        
        #Make an action happen when the user presses a key
        if key != 'nothing' and key != 'backspace' and key != 'enter':
            if len(name) < 7:
                name += key.upper()
        
        #Delete a letter
        if key == 'backspace':
            if len(name) != 0:
                name = name[:len(name)-1]
        
        #Enter the name
        if key == 'enter' and len(name) > 0:
            
            #Check to see if the user made no changes to the name
            if old_name == name:
                return data_dict, old_name
            
            #Check to see if the name exists in the data_dict already
            for player in data_dict:
                if data_dict[player][0] == old_name:
                    
                    #Change the user's name
                    data_dict[player][0] = name
                    break
                
            return data_dict, name
        
        #Check the length of the name and create the x variable based on it
        if len(name) == 1:
            x = round(reso_width/2.3025)
        elif len(name) == 2:
            x = round(reso_width/2.3025) - round(reso_width/23.025)
        elif len(name) == 3:
            x = round(reso_width/2.3025) - round(reso_width/23.025)*2
        elif len(name) == 4:
            x = round(reso_width/2.3025) - round(reso_width/23.025)*3
        elif len(name) == 5:
            x = round(reso_width/2.3025) - round(reso_width/23.025)*4
        elif len(name) == 6:
            x = round(reso_width/2.3025) - round(reso_width/23.025)*5
        elif len(name) == 7:
            x = round(reso_width/2.3025) - round(reso_width/23.025)*6
        
        #Constantly draw the name for the user to see
        if len(name) > 0: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/7.084615385 + reso_height/3.984615385)/2))).render(name,True,(0,0,0))),(x,round(reso_height/2.59)))
        
        #Check for when the user presses the 'x' button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return data_dict, old_name
            
        #Update the screen
        pygame.display.update()
        
#===========================================================================#
#===========================================================================#
#===========================================================================#
        
def display_current_color(canvas, block_colors, reso_width, reso_height):
    
    #Based on the block_colors, display the text
    if block_colors == 0: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Normal',True,(0,0,0))),(round(reso_width/3.07),round(reso_height/20.72)))
    elif block_colors == 1: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Green',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 2: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Blue',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 3: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Red',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 4: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Teal',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 5: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Yellow',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 6: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Orange',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 7: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Purple',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 8: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('White',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 9: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Black',True,(0,0,0))),(round(reso_width/3.019672131),round(reso_height/20.72)))
    elif block_colors == 10: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Christmas',True,(0,0,0))),(round(reso_width/3.349090909),round(reso_height/20.72)))
    elif block_colors == 11: canvas.blit(((pygame.font.SysFont('Watermelon',round((reso_width/23.025 + reso_height/12.95)/2))).render('Halloween',True,(0,0,0))),(round(reso_width/3.349090909),round(reso_height/20.72)))