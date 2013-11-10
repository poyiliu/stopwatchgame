# "Stopwatch: The Game"
# Created by Po-Yi Liu (November, 2013)

import simplegui
import time

# define global variables
integer = 0
stops = 0
D = 0
wins = 0
time = 0
time_is_running = True
storedD = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global integer, D, time, storedD
    t = integer
    
    
    D = t%10
    C = (t//10)%10
    #tens of seconds
    B = (t//10)%60//10
    #minutes
    A = t//600
    storedD = D
    #Format A:BC.D
    
    return str(A) + ":" +str(B) + str(C) + "." + str(D)
    
    
# define helper function to help keep count
def counter(x,y):
    global wins, stops
        
    return str(x) + "/" + str(y)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_game():
    timer.start()
    time_is_running = timer.is_running()

    
def stop():
    global wins, stops, time_is_running, storedD
    
    timer.stop()
    stops += 1
    time_is_running = timer.is_running()
    
    if storedD == 0:
        wins += 1
    
                 

def reset():
    global timer, wins, stops, integer
        
    wins = 0
    stops = 0
    integer = 0
    timer.stop()
    time_is_running = timer.is_running()
    

# define event handler for timer with 0.1 sec interval
def tick():
    global integer
    integer += 1

    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text("Stop Watch Game", [100, 30], 20, "White")
    canvas.draw_text(format(integer), [70, 170], 80, "Yellow")
    canvas.draw_text(str(counter(wins, stops)), [190, 80], 50, "Crimson")
 
    
# create frame
f = simplegui.create_frame("Stop Watch Game", 300, 300)

# register event handlers
f.add_button("Start", start_game, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)
f.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)

# start frame

f.start()



