# openHAB-VLC-Control
Control a [VLC media player](https://www.videolan.org/vlc) with openHAB using the [Exec Action](https://www.openhab.org/docs/configuration/actions.html#exec-actions) and a python script.

**Note: This does not include starting a stream, video or music. The VLC player must already be running before.** As example you are looking [TV with it](https://github.com/Michdo93/openHAB-web-tv).

## Installation

At first you have to install `pyautogui`:

```
pip install pyautogui
```

Maybe on Linux you have to run

```
python3 -m pip install pyautogui
```

On Windows it is definitely

```
python -m pip install pyautogui
```

Then you have to download the `vlc_control.py` file and place it to a path where you can run it inside your VM. On a Linux VM as example:

```
cd /home/<user>
wget https://raw.githubusercontent.com/Michdo93/openHAB-VLC-Control/main/vlc_control.py
sudo chmod +x room
```

On Windows:

```
cd C:\Users\<user>
wget https://raw.githubusercontent.com/Michdo93/openHAB-VLC-Control/main/vlc_control.py
```

The paths `/home/<user>` or `C:\Users\<user>` are the default paths which are open when you start a ssh session to this VM. Please make sure that you replace `<user>` with your actual username.

## Usage

By pressing one of the following keys VLC will do the following action. With this the `vlc_control.py` `pyautogui` will press this keys for you. So the [Exec Action](https://www.openhab.org/docs/configuration/actions.html#exec-actions) can be used that `pyautogui` will press the keys for you while VLC is running.

| Key Combination | Function | Description |
| :-------------: |:-------------:| :-----:|
| <kbd>Space</kbd> | `playPause()` | Play/Pause |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>→</kbd> | `fiveMinutesForward()` | 5 minutes forward |
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>←</kbd> | `fiveMinutesBackward()` | 5 minutes backward |
| <kbd>Ctrl</kbd> + <kbd>→</kbd> | `oneMinuteForward()` | 1 minute forward |
| <kbd>Ctrl</kbd> + <kbd>←</kbd> | `oneMinuteBackward()` | 1 minute backward |
| <kbd>Alt</kbd> + <kbd>→</kbd> | `tenSecondsForward()` | 10 seconds forward |
| <kbd>Alt</kbd> + <kbd>←</kbd> | `tenSecondsBackward()` | 10 seconds backward |
| <kbd>Shift</kbd> + <kbd>→</kbd> | `threeSecondsForward()` | 3 seconds forward |
| <kbd>Shift</kbd> + <kbd>←</kbd> | `threeSecondsBackward()` | 3 seconds backward |
| <kbd>S</kbd> | `stop()` | stop (not the same as pause. It means to stop the whole playback) |
| <kbd>+</kbd> | `faster()` | Faster |
| <kbd>-</kbd> | `slower()` | Slower |
| <kbd>=</kbd> | `normalSpeed()` | normal speed |
| <kbd>N</kbd> | `nextTrack()` | next track |
| <kbd>P</kbd> | `previousTrack()` | previous track |
| <kbd>T</kbd> | `showCurrentPostionTime()` | Fades in Postion/Time |
| <kbd>L</kbd> | `changeLoopOption()` | Change loop option: Loop, Loop one (once), Loop off |
| <kbd>E</kbd> | `nextFrame()` | Next Frame |
| <kbd>Ctrl</kbd> + <kbd>↑</kbd> | `fivePercentLouder()` | 5% louder |
| <kbd>Ctrl</kbd> + <kbd>↓</kbd> | `fivePercentQuieter()` | 5% quieter |
| <kbd>M</kbd> | `mute()` | Mute |
| <kbd>F</kbd> | `enableDisableFullscreen()` | Enable/disable full screen mode |
| <kbd>ESC</kbd> | `deactivateFullscreenMode()` | Deactivate full screen mode |
| <kbd>Shift</kbd> + <kbd>S</kbd> | `createSnapshot()` | Create snapshot |
| <kbd>Shift</kbd> + <kbd>R</kbd> | `startStopRecording()` | Start/stop recording |

You can call as example the `playPause()` function by running `python3 vlc_control.py playPause`. So at least by calling the functions you have to omit `()`.
