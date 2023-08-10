# Python program to translate
# speech to text and text to speech
from pycaw.pycaw import AudioUtilities 
import re
import time
import pynput
from pynput.keyboard import Key,Controller
keyboard = Controller()
import speech_recognition as sr
import pyttsx3
Activationword ="please" 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def getcurrentvolume():
    return

def intify(Value):
    
    int_str = ''.join(str(num) for num in Value)

    # Convert the string back to an integer
    single_integer = int(int_str)

    return single_integer


def VolumeModify(Value,strings):
    if (strings=="Inc"):
        Value=intify(Value)
        Modulo=Value//2
        for i in range(Modulo):
            
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.1)
    elif (strings=="Dec"):
        Value=intify(Value)
        Modulo=Value//2
        for i in range(Modulo):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.1)
    elif (strings=="Mute"):
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
    return


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
            
    

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def WordCheck(Word,Text):
    
    Word = Word.lower()
    Text = Text.lower()

    # Split the text into individual words
    words_in_text = Text.split()

    # Check if the word is present in the list of words from the text
    if Word in words_in_text:
        return True
    else:
        return False

def extract_numeric_values(input_string):
    # Regular expression pattern to find numeric values
    pattern = r'-?\d+(?:\.\d+)?'

    # Find all occurrences of numeric values in the input string
    numeric_values = re.findall(pattern, input_string)

    # Convert the strings to actual numeric values (integers or floats)
    numeric_values = [int(value) if '.' not in value else float(value) for value in numeric_values]
    

    return numeric_values

         

def Assistant(MyText):
    
    strings=""
    if(WordCheck("Volume",MyText)):
        Value=extract_numeric_values(MyText)
        if(WordCheck("Increase",MyText)):
            strings=strings+"Inc"
        elif(WordCheck("Decrease",MyText)):                  
            strings=strings+"Dec"
        elif(WordCheck("Mute",MyText)):            
            strings=strings+"Mute"
    
        VolumeModify(Value,strings)
    elif(WordCheck("Song",MyText) or WordCheck("Music",MyText) or WordCheck("Pause",MyText) or WordCheck("Play",MyText)):
        if(WordCheck("Next",MyText)or WordCheck("Skip",MyText)):
            strings=strings+"Skip"
        elif(WordCheck("Previous",MyText) or WordCheck("Back",MyText)):
            strings=strings+"Prev"
        elif( WordCheck("Pause",MyText) or WordCheck("Play",MyText)):
            strings=strings+"PausePlay"
        Mediacontrol(strings)
        
        
def main(): 
    while(1):   
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                if(WordCheck(Activationword,MyText)):
                    Assistant(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("could you please repeat that")
            
main()
