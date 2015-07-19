# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global WIDTH, cards, card_pos, exposed, state, click_count, n, m, exp_ind 
    WIDTH = 600
    cards = list(range(9)) + list(range(9)) #generates list with numbers
    card_pos = [WIDTH/36.0 - 15, 70] #determine the position of the first card (to be used in draw(canvas)
    exposed = list(18 * [False]) #generates list of exposed elements, with True for exposed 
    state = 0 #determines the state of the game
    click_count = 0.5
    n = -1 #determines the position of the previous clicked card
    m = -1 #determines the position of pre-previous clicked card
    exp_ind = [] #list with indexes of exposed elements
    random.shuffle(cards)
     
# define event handlers
def mouseclick(pos):
    global exposed, state, click_count, n, m, label, exp_ind
    for i in range(0,18): #sections iterator in canvas
        if pos[0] in range(i * WIDTH/18, (i + 1) * WIDTH/18): #to determine the section number in canvas
            if i not in exp_ind: #checks if we click on already exposed index
                exposed[i] = True 
                exp_ind.append(i) #adds i to exposed indexes list 'exp_ind'
                click_count += 0.5
                if state == 0:
                    state = 1
                elif state == 1:
                    if cards[i] == cards[n]:
                        state = 0
                    else:
                        state = 2
                elif state == 2:
                    exp_ind.remove(m) #removes previous element from exp_ind list
                    exp_ind.remove(n) #removes pre-previous element from exp_ind list
                    exposed[n] = False
                    exposed[m] = False
                    state = 1
                m = n
                n = i
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_pos, exposed, click_count, label
    label.set_text("Turns = " + str(int(click_count)))
    n = 0
    n2 = 0
    #looks for exposed and not exposed cards and draws appropriate text or color
    for i in range(len(cards)):
        if not exposed[i]:
            canvas.draw_line((card_pos[0] + 15 + n * WIDTH/18.0, 0), (card_pos[0] + 15 + n * WIDTH/18.0, 100), WIDTH/18.0, 'Green')
        elif exposed[i]: 
            canvas.draw_text(str(cards[i]),[card_pos[0] + (WIDTH/18.0) * n, card_pos[1]], 42, "White")
        n += 1
    #draws a separator between cards
    for i in range(19):
        canvas.draw_line([(WIDTH/18.0) * n2, 0], [(WIDTH/18.0) * n2, 100], 2, "Violet")
        n2 += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turhjns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric