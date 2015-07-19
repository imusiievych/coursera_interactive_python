import simplegui
import time

# global state
time = 0
minut = 0
sec = 0
m_sec = 0
tries = 0
success = 0
is_running = False

# helper functions
def update():
    global time
    time += 1
    return time

def format(t):
    global minut, sec, m_sec

    if t == 0:
        f_time = "0:00.0"
    else:
        sec = (t % 600) / 10
        m_sec = (t % 600) - sec * 10
        minut = t / 600
        f_time = str(minut) + ":0" + str(sec) + "." + str(m_sec)

        if sec < 10:
            f_time = str(minut) + ":0" + str(sec) + "." + str(m_sec)
        else:
            f_time = str(minut) + ":" + str(sec) + "." + str(m_sec)
            
    return f_time

def draw_handler(canvas):
    global tries, success
    canvas.draw_text(str(format(time)), [100, 100], 24, "White")
    score = str(success) + "/" + str(tries)
    canvas.draw_text(score, [50,50], 32, "Red")
    
def start_handler():
    global is_running
    is_running = True
    timer.start()
    
def stop_handler():
    global time, tries, success, m_sec, is_running
    timer.stop()

    if is_running:
        if m_sec == 0:
            success += 1
            tries += 1
        else:
            tries += 1
    is_running = False
    
def reset_handler():
    global time, success, tries
    success = 0
    tries = 0
    time = 0

    
# timer callback



# register event handlers
frame = simplegui.create_frame("Timer", 200, 300)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)
timer = simplegui.create_timer(100, update)

# start program
frame.start()
