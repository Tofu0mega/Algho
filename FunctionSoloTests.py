import pynput
from pynput.keyboard import Key,Controller
keyboard = Controller()
import time
def Mediacontrol(Task):
    Task=Task.lower()
    
    if(Task=="pauseplay"):
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
    elif(Task=="skip"):
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
    elif(Task=="prev"):
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
        
    return   


Mediacontrol("prev")