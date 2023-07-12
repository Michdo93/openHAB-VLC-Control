import pyautogui
import os
import sys

pyautogui.FAILSAFE = False

def focus_vlc():
    pyautogui.click(x=100, y=100, clicks=1, button="left")

def playPause():
    focus_vlc()
    pyautogui.press("space")

def fiveMinutesForward():
    focus_vlc()
    pyautogui.hotkey("ctrl", "alt", "right")

def fiveMinutesBackward():
    focus_vlc()
    pyautogui.hotkey("ctrl", "alt", "left")

def oneMinuteForward():
    focus_vlc()
    pyautogui.hotkey("ctrl", "right")

def oneMinuteBackward():
    focus_vlc()
    pyautogui.hotkey("ctrl", "left")

def tenSecondsForward():
    focus_vlc()
    pyautogui.hotkey("alt", "right")

def tenSecondsBackward():
    focus_vlc()
    pyautogui.hotkey("alt", "left")

def threeSecondsForward():
    focus_vlc()
    pyautogui.hotkey("shift", "right")

def threeSecondsBackward():
    focus_vlc()
    pyautogui.hotkey("shift", "left")

def stop():
    focus_vlc()
    pyautogui.press("s")

def faster():
    focus_vlc()
    pyautogui.press("+")

def slower():
    focus_vlc()
    pyautogui.press("-")

def normalSpeed():
    focus_vlc()
    pyautogui.press("=")

def nextTrack():
    focus_vlc()
    pyautogui.press("n")

def previousTrack():
    focus_vlc()
    pyautogui.press("p")

def showCurrentPostionTime():
    focus_vlc()
    pyautogui.press("t")

def changeLoopOption():
    focus_vlc()
    pyautogui.press("l")

def nextFrame():
    focus_vlc()
    pyautogui.press("e")

def fivePercentLouder():
    focus_vlc()
    pyautogui.hotkey("ctrl", "up")

def fivePercentQuieter():
    focus_vlc()
    pyautogui.hotkey("ctrl", "down")

def mute():
    focus_vlc()
    pyautogui.press("m")

def enableDisableFullscreen():
    focus_vlc()
    pyautogui.press("f")

def deactivateFullscreenMode():
    focus_vlc()
    pyautogui.press("esc")

def createSnapshot():
    focus_vlc()
    pyautogui.hotkey("shift", "s")

def startStopRecording():
    focus_vlc()
    pyautogui.hotkey("shift", "r")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
