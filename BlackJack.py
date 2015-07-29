# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
lap = 0
message = "Hit or Stand?"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, up = True):
        # up parameter indicates card's face side or back side
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        card_loc_back = (CARD_BACK_CENTER[0], CARD_CENTER[1])
        if up:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_back, card_loc_back, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self, is_dealer = False):
        self.hand = []
        self.is_dealer = is_dealer # helper parameter to be used when drawing hand's cards

    def __str__(self):
        string = "Hand contains "
        for i in range(0, len(self.hand)):
            string += str(self.hand[i]) + " " 
        return string
        
    def add_card(self, card, up = True):
        self.hand.append(card)
        
    def get_value(self):
        # compute the value of the hand
        hand_value = 0
        aces = 0
        for i in self.hand:
            if i.get_rank() in RANKS[0:9]: # count aces as 1, if the hand has an ace,
                hand_value += VALUES[i.get_rank()]
            if i.get_rank() in RANKS[9:len(RANKS)]:
                hand_value += 10
        for i in self.hand: # aces need to be avaluated after all other cards are counted
            if i.get_rank() == 'A':
                aces += 1  
            if aces > 0: # add to hand value 10 for ace if it doesn't bust
                if hand_value + 10 <= 21:
                    hand_value += 10
        return hand_value

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in self.hand:
            if self.is_dealer: # for dealer the back of first card is displayed
                if self.hand.index(i) == 0:
                    # "False" for up parameter in Card.draw(canvas, pos, up = True) means card to be displayed face down
                    i.draw(canvas, (pos[0], pos[1]), False)
                else:
                    i.draw(canvas, (pos[0] + 72 * self.hand.index(i), pos[1]))
            else:
                i.draw(canvas, (pos[0] + 72 * self.hand.index(i), pos[1]))
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                card = Card(i, j)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.deck)

    def deal_card(self):
        dealt = random.choice(self.deck)
        self.deck.remove(dealt) # removes dealt card from deck
        return dealt
    
    def __str__(self):
        string = "Deck contains "
        for i in self.deck:
            string += str(i) + " "
        return string

#define event handlers for buttons
def deal():
    global outcome, score, in_play, lap, message, deck, player_hand, dealer_hand
    if in_play:
        outcome = "You dealt in middle of round. You lose."
        score -= 1
    else:
        in_play = True
        player_hand = Hand()
        dealer_hand = Hand(True)
        deck = Deck()
        deck.shuffle()
        outcome = ""
        lap += 1
        message = "Hit or Stand?"
        cards = []
        for i in range(0,4):
            cards.append(deck.deal_card()) # creates list of 4 random card
            if i == 0 or i == 1:
                player_hand.add_card(cards[i]) # adds 1st and 2nd card of the list to the player hand
            else:
                dealer_hand.add_card(cards[i]) # adds 3rd and 4th card of the list to dealer hand

def hit():
    global outcome, in_play, score, message 
    card = deck.deal_card()
    if in_play: # if the hand is in play, hit the player
        player_hand.add_card(card)
        if player_hand.get_value() > 21:
            outcome = "You have busted"
            in_play = False
            score -= 1
            dealer_hand.is_dealer = False
            message = "New Deal?"

def stand():
    global outcome, in_play, score, message, lap
    if in_play:
        while dealer_hand.get_value() < 17: # hit dealer's hand if value < 17
            card = deck.deal_card()
            dealer_hand.add_card(card)
            if dealer_hand.get_value() > 21:
                outcome = "Dealer has busted"
                in_play = False
                score += 1
                dealer_hand.is_dealer = False
                message = "New Deal?"
        if in_play:
            if player_hand.get_value() > dealer_hand.get_value(): # compare player's and dealer's values
                outcome = "You win!))"
                score += 1
                in_play = False
                dealer_hand.is_dealer = False
            else:
                outcome = "You lose! It's sad("
                score -= 1
                in_play = False
                dealer_hand.is_dealer = False
            message = "New Deal?"    
    else:
        outcome = "You have already busted" 
        message = "New Deal?"

# draw handler    
def draw(canvas):
    global player_hand, dealer_hand, score, outcome, message
    player_hand.draw(canvas, (100, 400))
    dealer_hand.draw(canvas, (100, 200))

    canvas.draw_text("BlackJack", [20, 50], 44, "Violet")
    canvas.draw_text("Score: " + str(score), [400, 50], 34, "Red")
    canvas.draw_text("Dealer", [100, 150], 30, "Black")
    canvas.draw_text("Player", [100, 350], 30, "Black")
    canvas.draw_text(message, [300, 350], 30, "Black")
    canvas.draw_text(outcome, [100, 550], 25, "Red")
    canvas.draw_text("Lap: " + str(lap), [400, 150], 40, "Blue")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()



