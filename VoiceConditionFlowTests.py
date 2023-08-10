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




operationmode=0





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
    
def remove_word(MyText, ActivationWord):
    words = MyText.split()
    modified_words = [word for word in words if word != ActivationWord]
    modified_string = ' '.join(modified_words)
    return modified_string


  
def WordTest(MyText):
    print (MyText)
    
    
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
    
        print(strings)
    elif(WordCheck("Song",MyText) or WordCheck("Music",MyText) or WordCheck("Pause",MyText) or WordCheck("Play",MyText)):
        if(WordCheck("Next",MyText)or WordCheck("Skip",MyText)):
            strings=strings+"Skip"
        elif(WordCheck("Previous",MyText) or WordCheck("Back",MyText)):
            strings=strings+"Prev"
        elif( WordCheck("Pause",MyText) or WordCheck("Play",MyText)):
            strings=strings+"PausePlay"
        print(strings)
        
        
def main(): 
    while(1):   
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone(1) as source2:
                
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
                    MyText=remove_word(MyText,Activationword)
                    if(operationmode==1):
                        Assistant(MyText)
                    else:
                        WordTest(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Could You Please Repeat That")
            
main()
