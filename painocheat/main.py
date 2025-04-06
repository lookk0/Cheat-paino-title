#X1:  601 X2:  687 X3:  780 X4:  856 Y:  623 RGB:(  0,   0,   0)
import pyautogui as pg
import time as t
import keyboard as k
import win32api,win32con

run = False
def switch():
    global run
    run = not run
    if run:
        print('running')
    else:
        print('stoped')

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

k.add_hotkey('o',switch)
x1,x2,x3,x4,y=601,687,780,856,500
while True:
    if run:
        if pg.pixel(x1,y)[0] == 0:
            click(x1,y)
        if pg.pixel(x2,y)[0] == 0:
            click(x2,y)
        if pg.pixel(x3,y)[0] == 0:
            click(x3,y)
        if pg.pixel(x4,y)[0] == 0:
            click(x4,y)
        t.sleep(0.01)
    else:
        pass