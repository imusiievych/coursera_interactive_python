#Rock-paper-scissors-lizard-Spock 
#0 — rock, 1 — Spock, 2 — paper, 3 — lizard, 4 — scissors
import random

def name_to_number(name):
    number = 0;
    if (name == 'rock'):
        number = 0;
    elif (name == 'Spock'):
        number = 1;
    elif (name == 'paper'):
        number = 2;
    elif (name == 'lizard'):
        number = 3;
    elif (name == 'scissors'):
        number = 4;
    else:
        number = "Please enter valid choice"
    return number
    
def number_to_name(number):
    if (number == 0 ):
        name = 'rock';
    elif (number == 1 ):
        name = 'Spock';
    elif (number == 2):
        name = 'paper';
    elif (number == 3):
        name = 'lizard';
    elif (number == 4):
        name = 'scissors';
    else:
        name = "Please enter valid choice"
    return name
  
def rpsls(player_choice):
    print ""
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    while (isinstance (player_number, (int))):
        if (comp_number > player_number):
            if (comp_number - player_number <= 2):
                result = "Computer wins!"
            else:
                result = "Player wins!"
        elif (comp_number < player_number):
            if (player_number - comp_number <= 2):
                result = "Player wins!"
            else: 
                result = "Computer wins!"
        else:
            result = "Player and computer tie!"
        
        return result

print rpsls("rock")
print rpsls("Spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")
print rpsls("lala")


    
    
    
    
    
    
    
    
    
    
    
    
