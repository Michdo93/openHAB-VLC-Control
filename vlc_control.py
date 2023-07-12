import keyboard
import os
import sys
import pygetwindow as gw

keyboard.unhook_all()

def focus_vlc():
    try:
        window = gw.getWindowsWithTitle("VLC media player")[0]  # Anpassen des Fenstertitels, falls erforderlich
        if window.isMinimized:
            window.restore()
        window.activate()
        return True
    except IndexError:
        print("Das VLC-Fenster wurde nicht gefunden.")
        return False

def playPause():
    focus_vlc()
    keyboard.press("space")
    keyboard.release("space")

def fiveMinutesForward():
    focus_vlc()
    keyboard.press_and_release("ctrl + alt + right")

def fiveMinutesBackward():
    focus_vlc()
    keyboard.press_and_release("ctrl + alt + left")

def oneMinuteForward():
    focus_vlc()
    keyboard.press_and_release("ctrl + right")

def oneMinuteBackward():
    focus_vlc()
    keyboard.press_and_release("ctrl + left")

def tenSecondsForward():
    focus_vlc()
    keyboard.press_and_release("alt + right")

def tenSecondsBackward():
    focus_vlc()
    keyboard.press_and_release("alt + left")

def threeSecondsForward():
    focus_vlc()
    keyboard.press_and_release("shift + right")

def threeSecondsBackward():
    focus_vlc()
    keyboard.press_and_release("shift + left")

def stop():
    focus_vlc()
    keyboard.press("s")
    keyboard.release("s")

def faster():
    focus_vlc()
    keyboard.press("+")
    keyboard.release("+")

def slower():
    focus_vlc()
    keyboard.press("-")
    keyboard.release("-")

def normalSpeed():
    focus_vlc()
    keyboard.press("=")
    keyboard.release("=")

def nextTrack():
    focus_vlc()
    keyboard.press("n")
    keyboard.release("n")

def previousTrack():
    focus_vlc()
    keyboard.press("p")
    keyboard.release("p")

def showCurrentPostionTime():
    focus_vlc()
    keyboard.press("t")
    keyboard.release("t")

def changeLoopOption():
    focus_vlc()
    keyboard.press("l")
    keyboard.release("l")

def nextFrame():
    focus_vlc()
    keyboard.press("e")
    keyboard.release("e")

def fivePercentLouder():
    focus_vlc()
    keyboard.press_and_release("ctrl + up")

def fivePercentQuieter():
    focus_vlc()
    keyboard.press_and_release("ctrl + down")

def mute():
    focus_vlc()
    keyboard.press("m")
    keyboard.release("m")

def enableDisableFullscreen():
    focus_vlc()
    keyboard.press("f")
    keyboard.release("f")

def deactivateFullscreenMode():
    focus_vlc()
    keyboard.press("esc")
    keyboard.release("esc")

def createSnapshot():
    focus_vlc()
    keyboard.press_and_release("shift + s")

def startStopRecording():
    focus_vlc()
    keyboard.press_and_release("shift + r")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
