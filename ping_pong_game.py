# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [PAD_WIDTH / 2, HEIGHT / 2]
paddle2_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [1, 1]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    x = random.randrange(1, 2)
    y = random.randrange(1, 2)
    if direction:
        vel = [x, -y]
    else:
        vel = [-x, -y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, vel
    global paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle2_pos[1] += paddle2_vel
    paddle1_pos[1] += paddle1_vel
    if (paddle1_pos[1] <= HALF_PAD_HEIGHT) or (paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_vel = 0
    if (paddle2_pos[1] <= HALF_PAD_HEIGHT) or (paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_vel = 0
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT / 2], [paddle1_pos[0], paddle1_pos[1] - PAD_HEIGHT / 2], PAD_WIDTH, "Green")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT / 2], [paddle2_pos[0], paddle2_pos[1] - PAD_HEIGHT / 2], PAD_WIDTH, "Blue")
    # determine whether ball hits top or bottom
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS):

        vel[1] = -vel[1]
    # determine whether ball hits gutters:
    if ball_pos[0] >= WIDTH - PAD_WIDTH:
        score1 += 1
        spawn_ball(LEFT)
    elif ball_pos[0] <= PAD_WIDTH:
        score2 += 1
        spawn_ball(RIGHT)
    # determine whether paddle and ball collide  
    if (ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH) and (ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT - BALL_RADIUS) and (ball_pos[1] <=paddle2_pos[1] + HALF_PAD_HEIGHT + BALL_RADIUS):
        vel[0] += 0.1 * vel[0]
        vel[1] += 0.1 * vel[1]
        vel[0] = -vel[0]
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT - BALL_RADIUS) and (ball_pos[1] <=paddle1_pos[1] + HALF_PAD_HEIGHT + BALL_RADIUS):
        vel[0] += 0.1 * vel[0]
        vel[1] += 0.1 * vel[1]
        vel[0] = -vel[0]
    # update score if ball doesn't hit paddle

    # draw scores
    canvas.draw_text(str(score1), [150, 100], 66, "Red")
    canvas.draw_text(str(score2), [400, 100], 66, "Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game)


# start frame
new_game()
frame.start()
