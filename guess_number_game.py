# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guesses_left
    print ""
    secret_number = random.randrange(0, 101)
    guesses_left = math.ceil(math.log(100 + 1, 2))

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, guesses_left
    print ""
    print "New game. Random from 0 to 100"
    new_game()
    secret_number = random.randrange(0, 101)
    guesses_left = math.ceil(math.log(100 + 1, 2))

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, guesses_left
    print ""
    print "New game. Random from 0 to 1000"
    new_game()
    guesses_left = 10
    secret_number = random.randrange(0, 1001)
    guesses_left = math.ceil(math.log(1000 + 1, 2))
    
def input_guess(guess):
    # main game logic goes here	
    global guesses_left
    number_guess = int(guess)
    guesses_left =int(guesses_left) - 1
    print "Your guess is", guess
    if (guesses_left > -1):
        if (number_guess > secret_number):
            print "Lower!"
            print "Guesses left", guesses_left
            print ""
        elif (number_guess < secret_number):
            print "Higher!"
            print "Guesses left", guesses_left
            print ""
        else:
            print "Correct!"
            print ""
            print "New game. Range from 0 to 100"
            new_game()
    else:
        print "You have no more attempts to guess"
        new_game()
  
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range 100", range100, 200)
frame.add_button("Range 1000", range1000, 200)
frame.add_input("Your guess", input_guess, 200)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
