# Python program to translate
# speech to text and text to speech
from pycaw.pycaw import AudioUtilities 
import re
import speech_recognition as sr
import pyttsx3
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech

def intify(Value):
    
    int_str = ''.join(str(num) for num in Value)

    # Convert the string back to an integer
    single_integer = int(int_str)

    return single_integer


def VolumeModify(Value):
    Value=intify(Value)
    Current=44
    int(Current)
    New=Current+Value
    print("currentvolume:",Current,"New Volume:",New)

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
    if(WordCheck("Volume",MyText) and WordCheck("Increase",MyText)):
        Value=extract_numeric_values(MyText)
        VolumeModify(Value)
    elif(WordCheck("Volume",MyText) and WordCheck("Decrease",MyText)):
        Value=extract_numeric_values(MyText)
        Value=intify(Value)
        Value=0-Value
        VolumeModify(Value)
        
        
 
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
 
            Assistant(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")