import pyautogui
import os
import sys

pyautogui.FAILSAFE = False

def playPause():
    pyautogui.press("space")

def fiveMinutesForward():
    pyautogui.hotkey("ctrl", "alt", "right")

def fiveMinutesBackward():
    pyautogui.hotkey("ctrl", "alt", "left")

def oneMinuteForward():
    pyautogui.hotkey("ctrl", "right")

def oneMinuteBackward():
    pyautogui.hotkey("ctrl", "left")

def tenSecondsForward():
    pyautogui.hotkey("alt", "right")

def tenSecondsBackward():
    pyautogui.hotkey("alt", "left")

def threeSecondsForward():
    pyautogui.hotkey("shift", "right")

def threeSecondsBackward():
    pyautogui.hotkey("shift", "left")

def stop():
    pyautogui.press("s")

def faster():
    pyautogui.press("+")

def slower():
    pyautogui.press("-")

def normalSpeed():
    pyautogui.press("=")

def nextTrack():
    pyautogui.press("n")

def previousTrack():
    pyautogui.press("p")

def showCurrentPostionTime():
    pyautogui.press("t")

def changeLoopOption():
    pyautogui.press("l")

def nextFrame():
    pyautogui.press("e")

def fivePercentLouder():
    pyautogui.hotkey("ctrl", "up")

def fivePercentQuieter():
    pyautogui.hotkey("ctrl", "down")

def mute():
    pyautogui.press("m")

def enableDisableFullscreen():
    pyautogui.press("f")

def deactivateFullscreenMode():
    pyautogui.press("esc")

def createSnapshot():
    pyautogui.hotkey("shift", "s")

def startStopRecording():
    pyautogui.hotkey("shift", "r")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
