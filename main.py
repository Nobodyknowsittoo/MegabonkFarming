import pyautogui
from pynput import keyboard
import threading
import time

# home start button Point(x=3850, y=620)
# confirm button for character and map Point(x=4650, y=1130)

characters = {
    "Fox" : (2780, 360),
    "Sir Oofie" : (2980, 360),
    "Calcium" : (3180, 360),
    "Megachad" : (3380, 360),
    "Ogre" : (2780, 560),
    "CL4NK" : (2980, 560),
    "Athena" : (3180, 560),
    "Robinette" : (3380, 560),
    "Monke" : (2780, 760),
    "Tony McZoom" : (2980, 760),
    "Bush" : (3180, 760),
    "Birdo" : (3380, 760),
    "Noelle" : (2780, 960),
    "Amog" : (2980, 960),
    "Spaceman" : (3180, 960),
    "Bandit" : (3380, 960),
    "Ninja" : (2780, 1160),
    "Vlad" : (2980, 1160),
    "Sir Chadwell" : (3180, 1160),
    "Dicehead" : (3380, 1160),
    "Roberto" : (2780, 1260)
}

maps = {
    "Forest" : (3050, 400),
    "Desert" : (3050, 600),
    "Boss" : (3050, 850)
}

tiers = {
    "Tier 1" : (4525, 625),
    "Tier 2" : (4560, 700),
    "Tier 3" : (4575, 770),
}

def moveToAllCharacter():
    global running

    running = True

    for name, (x, y) in characters.items():
        
        if not running:
            return
        
        pyautogui.moveTo(x, y, duration=0.3)
        
        time.sleep(0.5)

def clickMap(whatMap):
    global running

    for name, (x, y) in maps.items():

        if not running:
            return
        
        if name == whatMap:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            pyautogui.moveTo(4650, 1130)
            pyautogui.click()

def clickCharacter(whatCharacter):

    global running

    for name, (x, y) in characters.items():

        if not running:
            return
        
        if name == whatCharacter:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            pyautogui.moveTo(4650, 1130)
            pyautogui.click()


def startProgram():
    
    global running
    running = True

    whatCharacter = input("What Character do you want to use for the sesssion? : ")
    time.sleep(0.5)

    whatMap = input("What map would you like to farm on? (Forest|Desert|Boss) : ")
    
    print("Open now the start window of Megabonk. The program will start in 5 seconds")
    time.sleep(5)

    pyautogui.moveTo(3850, 620)
    pyautogui.click()

    clickCharacter(whatCharacter)
    clickMap(whatMap)

def stopProgram():
    
    global running
    running = False
    
    print("Stopped the program")

def scanningPixelPosition():
    
    print(pyautogui.position())

def scanningPixel():
    
    xScan, yScan = pyautogui.position()
    print(pyautogui.pixel(xScan, yScan))

def on_press(key):
    
    if key == keyboard.Key.f4:
        stopProgram()

listenerStop = keyboard.Listener(on_press=on_press)
listenerStop.start()

with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+r': startProgram,
    'p': scanningPixelPosition,
    'v': moveToAllCharacter,
    'o': scanningPixel
}) as h:
    h.join()
