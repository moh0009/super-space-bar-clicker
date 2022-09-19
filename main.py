import pyautogui as p
import time as t
  
def countdown(r): 
    while r:
        mins, secs = divmod(r, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        t.sleep(1)
        for i in range(1000):
            p.PAUSE = 0
            p.press("space")    
        r -= 1

    print("check your space bar !!")

t.sleep(3)
countdown(5)
