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

def moveTo():
    global running
    running = True
    for name, (x, y) in character.items():
        if not running:
            return
        pyautogui.moveTo(x, y, duration=0.3)
        time.sleep(0.5)

def startProgram():
    
    global running
    running = True

    whatCharacter = input("What Character do you want to use for the sesssion? : ")
    
    time.sleep(0.5)
    print("Automatically using for now the standard map")
    time.sleep(0.5)
    print("Open now the start window of Megabonk. The program will start in 5 seconds")
    time.sleep(5)


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
    if key == keyboard.Key.backspace:
        stopProgram()

listenerStop = keyboard.Listener(on_press=on_press)
listenerStop.start()

with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+r': startProgram,
    'p': scanningPixelPosition,
    'r': moveTo,
    'o': scanningPixel
}) as h:
    h.join()
