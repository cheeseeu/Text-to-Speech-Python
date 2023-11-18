import pyttsx3
engine = pyttsx3.init()
from colorama import Fore, Back, Style

#config
speakingRate = 125 #speaking rate
volume = 1 #volume 0-1

engine.setProperty('rate', speakingRate) #set speaking rate to the one in config
rate = engine.getProperty('rate') #get the current speaking rate
print ("Speaking rate set to " + str(speakingRate))

engine.setProperty('volume', volume) #set speaking rate to the one in config
volume = engine.getProperty('volume') #get the current speaking rate
print ("Volume set to: " + str(volume))

def log(message): # print a message with [System] at the start
    print(f"[System] {message}") 

#check if there is a input.txt file. If not, ask user for input. If there is, set the "text" property to the files contents
try:
    with open('input.txt', 'r') as file:
        text = file.read()
except FileNotFoundError:
    text = input('No input.txt file not found. What do you want to convert to audio? ')

save = input('Would you like to save this as an mp3? (y/n)')

if save == "y":
    path = input("Where should the file be saved to? ")
    log("Saving...")
    engine.save_to_file(text, f'{path}output.mp3') # save the file with the text to the path the user requested
    log(f"Saved! Path: {path}output.mp3!")

engine.say(text) # say the text outloud
engine.runAndWait()
