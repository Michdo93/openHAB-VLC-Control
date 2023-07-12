import keyboard
import os
import sys

keyboard.unhook_all()

def playPause():
    keyboard.press("space")
    keyboard.release("space")

def fiveMinutesForward():
    keyboard.press_and_release("ctrl + alt + right")

def fiveMinutesBackward():
    keyboard.press_and_release("ctrl + alt + left")

def oneMinuteForward():
    keyboard.press_and_release("ctrl + right")

def oneMinuteBackward():
    keyboard.press_and_release("ctrl + left")

def tenSecondsForward():
    keyboard.press_and_release("alt + right")

def tenSecondsBackward():
    keyboard.press_and_release("alt + left")

def threeSecondsForward():
    keyboard.press_and_release("shift + right")

def threeSecondsBackward():
    keyboard.press_and_release("shift + left")

def stop():
    keyboard.press("s")
    keyboard.release("s")

def faster():
    keyboard.press("+")
    keyboard.release("+")

def slower():
    keyboard.press("-")
    keyboard.release("-")

def normalSpeed():
    keyboard.press("=")
    keyboard.release("=")

def nextTrack():
    keyboard.press("n")
    keyboard.release("n")

def previousTrack():
    keyboard.press("p")
    keyboard.release("p")

def showCurrentPostionTime():
    keyboard.press("t")
    keyboard.release("t")

def changeLoopOption():
    keyboard.press("l")
    keyboard.release("l")

def nextFrame():
    keyboard.press("e")
    keyboard.release("e")

def fivePercentLouder():
    keyboard.press_and_release("ctrl + up")

def fivePercentQuieter():
    keyboard.press_and_release("ctrl + down")

def mute():
    keyboard.press("m")
    keyboard.release("m")

def enableDisableFullscreen():
    keyboard.press("f")
    keyboard.release("f")

def deactivateFullscreenMode():
    keyboard.press("esc")
    keyboard.release("esc")

def createSnapshot():
    keyboard.press_and_release("shift + s")

def startStopRecording():
    keyboard.press_and_release("shift + r")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
