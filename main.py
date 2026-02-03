import pyautogui
from pynput import keyboard
import threading
import time

spamming = False

def spam_enter():
    global spamming
    while spamming:
        pyautogui.press('enter')
        time.sleep(0.05)

def startingSpam():
    global spamming
    if not spamming:
        spamming = True
        threading.Thread(target=spam_enter, daemon=True).start()
        print("Spamming started")

def stopSpam():
    global spamming
    spamming = False
    print("Spamming stopped")

def scanningPixelPosition():
    print(pyautogui.position())

def on_press(key):
    if key == keyboard.Key.backspace:
        stopSpam()

listenerStop = keyboard.Listener(on_press=on_press)
listenerStop.start()

with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+r': startingSpam,
    'p': scanningPixelPosition,
}) as h:
    h.join()
