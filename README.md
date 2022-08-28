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
sudo chmod +x vlc_control.py
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

## Items

You have to create following items:

```
Group VLC_Control "VLC Control" <screen>

Switch VLC_Control_PlayPause "Play/Pause" (VLC_Control)
Switch VLC_Control_5MinutesForward "5 Minutes Forward" (VLC_Control)
Switch VLC_Control_5MinutesBackward "5 Minutes Backward" (VLC_Control)
Switch VLC_Control_1MinuteForward "1 Minute Forward" (VLC_Control)
Switch VLC_Control_1MinutesBackward "1 Minutes Backward" (VLC_Control)
Switch VLC_Control_10SecondsForward "10 Seconds Forward" (VLC_Control)
Switch VLC_Control_10SecondsBackward "10 Seconds Backward" (VLC_Control)
Switch VLC_Control_3SecondsForward "3 Seconds Forward" (VLC_Control)
Switch VLC_Control_3SecondsBackward "3 Seconds Backward" (VLC_Control)
Switch VLC_Control_Stop "Stop" (VLC_Control)
Switch VLC_Control_Faster "Faster" (VLC_Control)
Switch VLC_Control_Slower "Slower" (VLC_Control)
Switch VLC_Control_NormalSpeed "Normal speed" (VLC_Control)
Switch VLC_Control_NextTrack "Next track" (VLC_Control)
Switch VLC_Control_PreviousTrack "Previous track" (VLC_Control)
Switch VLC_Control_ShowCurrentPostionTime "Fade in Postion/Time" (VLC_Control)
Switch VLC_Control_ChangeLoopOption "Change loop option" (VLC_Control)
Switch VLC_Control_NextFrame "Next frame" (VLC_Control)
Switch VLC_Control_Louder "Louder" (VLC_Control)
Switch VLC_Control_Quieter "Quieter" (VLC_Control)
Switch VLC_Control_Mute "Mute" (VLC_Control)
Switch VLC_Control_ToggleFullscreen "Toggle fullscreen" (VLC_Control)
Switch VLC_Control_DeactivateFullscreen "Deactivate fullscreen" (VLC_Control)
Switch VLC_Control_CreateSnapshot "Create snapshot" (VLC_Control)
Switch VLC_Control_StartStopRecording "Start/stop recording" (VLC_Control)
```

## Rules

In the next step you have to add following rules. One important thing is that the `Switch` items will receive an post update to `OFF`. This is needed so that one of the buttons created later for the sitemap, can be clicked again and again. One would like to switch louder or fast forward several times in succession or increase the speed, etc. In addition, you toggle the play/pause or other input options back and forth.

```
rule "VLC_Control_PlayPause changed to ON"
when
    Item VLC_Control_PlayPause changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py playPause"')
    }
    VLC_Control_PlayPause.postUpdate(OFF)
end

rule "VLC_Control_5MinutesForward changed to ON"
when
    Item VLC_Control_5MinutesForward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fiveMinutesForward"')
    }
    VLC_Control_5MinutesForward.postUpdate(OFF)
end

rule "VLC_Control_5MinutesBackward changed to ON"
when
    Item VLC_Control_5MinutesBackward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fiveMinutesBackward"')
    }
    VLC_Control_5MinutesBackward.postUpdate(OFF)
end

rule "VLC_Control_1MinuteForward changed to ON"
when
    Item VLC_Control_1MinuteForward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py oneMinuteForward"')
    }
    VLC_Control_1MinuteForward.postUpdate(OFF)
end

rule "VLC_Control_1MinutesBackward changed to ON"
when
    Item VLC_Control_1MinutesBackward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py oneMinuteBackward"')
    }
    VLC_Control_1MinutesBackward.postUpdate(OFF)
end

rule "VLC_Control_10SecondsForward changed to ON"
when
    Item VLC_Control_10SecondsForward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py tenSecondsForward"')
    }
    VLC_Control_10SecondsForward.postUpdate(OFF)
end

rule "VLC_Control_10SecondsBackward changed to ON"
when
    Item VLC_Control_10SecondsBackward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py tenSecondsBackward"')
    }
    VLC_Control_10SecondsBackward.postUpdate(OFF)
end

rule "VLC_Control_3SecondsForward changed to ON"
when
    Item VLC_Control_3SecondsForward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py threeSecondsForward"')
    }
    VLC_Control_3SecondsForward.postUpdate(OFF)
end

rule "VLC_Control_3SecondsBackward changed to ON"
when
    Item VLC_Control_3SecondsBackward changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py threeSecondsBackward"')
    }
    VLC_Control_3SecondsBackward.postUpdate(OFF)
end

rule "VLC_Control_Stop changed to ON"
when
    Item VLC_Control_Stop changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py stop"')
    }
    VLC_Control_Stop.postUpdate(OFF)
end

rule "VLC_Control_Faster changed to ON"
when
    Item VLC_Control_Faster changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py faster"')
    }
    VLC_Control_Faster.postUpdate(OFF)
end

rule "VLC_Control_Slower changed to ON"
when
    Item VLC_Control_Slower changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py slower"')
    }
    VLC_Control_Slower.postUpdate(OFF)
end

rule "VLC_Control_NormalSpeed changed to ON"
when
    Item VLC_Control_NormalSpeed changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py normalSpeed"')
    }
    VLC_Control_NormalSpeed.postUpdate(OFF)
end

rule "VLC_Control_NextTrack changed to ON"
when
    Item VLC_Control_NextTrack changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py nextTrack"')
    }
    VLC_Control_NextTrack.postUpdate(OFF)
end

rule "VLC_Control_PreviousTrack changed to ON"
when
    Item VLC_Control_PreviousTrack changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py previousTrack"')
    }
    VLC_Control_PreviousTrack.postUpdate(OFF)
end

rule "VLC_Control_ShowCurrentPostionTime changed to ON"
when
    Item VLC_Control_ShowCurrentPostionTime changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py showCurrentPositionTime"')
    }
    VLC_Control_ShowCurrentPostionTime.postUpdate(OFF)
end

rule "VLC_Control_ChangeLoopOption changed to ON"
when
    Item VLC_Control_ChangeLoopOption changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py changeLoopOption"')
    }
    VLC_Control_ChangeLoopOption.postUpdate(OFF)
end

rule "VLC_Control_NextFrame changed to ON"
when
    Item VLC_Control_NextFrame changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py nextFrame"')
    }
    VLC_Control_NextFrame.postUpdate(OFF)
end

rule "VLC_Control_Louder changed to ON"
when
    Item VLC_Control_Louder changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fivePercentLouder"')
    }
    VLC_Control_Louder.postUpdate(OFF)
end

rule "VLC_Control_Quieter changed to ON"
when
    Item VLC_Control_Quieter changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fivePercentQuieter"')
    }
    VLC_Control_Quieter.postUpdate(OFF)
end

rule "VLC_Control_Mute changed to ON"
when
    Item VLC_Control_Mute changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py mute"')
    }
    VLC_Control_Mute.postUpdate(OFF)
end

rule "VLC_Control_ToggleFullscreen changed to ON"
when
    Item VLC_Control_ToggleFullscreen changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py enableDisableFullscreen"')
    }
    VLC_Control_ToggleFullscreen.postUpdate(OFF)
end

rule "VLC_Control_DeactivateFullscreen changed to ON"
when
    Item VLC_Control_DeactivateFullscreen changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py deactivateFullscreenMode"')
    }
    VLC_Control_DeactivateFullscreen.postUpdate(OFF)
end

rule "VLC_Control_CreateSnapshot changed to ON"
when
    Item VLC_Control_CreateSnapshot changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py createSnapshot"')
    }
    VLC_Control_CreateSnapshot.postUpdate(OFF)
end

rule "VLC_Control_StartStopRecording changed to ON"
when
    Item VLC_Control_StartStopRecording changed to ON
then
    response = executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"')

    if (response > 0) {
        executeCommandLine('/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py startStopRecording"')
    }
    VLC_Control_StartStopRecording.postUpdate(OFF)
end
```

Also you have to add following to `/etc/openhab/misc/exec.whitelist`:

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/bin/ps aux | /bin/grep [v]lc | /usr/bin/wc -l"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py %2$s"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py playPause"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fiveMinutesForward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fiveMinutesBackward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py oneMinuteForward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py oneMinuteBackward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py tenSecondsForward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py tenSecondsBackward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py threeSecondsForward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py threeSecondsBackward"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py stop"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py faster"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py slower"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py normalSpeed"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py nextTrack"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py previousTrack"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py showCurrentPositionTime"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py changeLoopOption"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py nextFrame"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fivePercentLouder"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py fivePercentQuieter"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py mute"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py enableDisableFullscreen"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py deactivateFullscreenMode"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py createSnapshot"
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no <user>@<ip> "/usr/bin/python3 vlc_control.py startStopRecording"

You have to replace `<user>` and `<password>` with the username and password of your remote computer. Also you have to replace `<ip>` with the ip address of your remote computer.
```

## Sitemaps

At least you have to add following to your sitemap:

```
Text label="VLC Control" icon="screen" {
    Switch item=VLC_Control_PlayPause label="Play/Pause" icon="exec_restart" mappings=[ON="Play/Pause"]
    Switch item=VLC_Control_5MinutesForward label="5 Minutes Forward" icon="exec_restart" mappings=[ON=">> 5 min"]
    Switch item=VLC_Control_5MinutesBackward label="5 Minutes Backward" icon="exec_restart" mappings=[ON="<< 5 min"]
    Switch item=VLC_Control_1MinuteForward label="1 Minute Forward" icon="exec_restart" mappings=[ON=">> 1 min"]
    Switch item=VLC_Control_1MinutesBackward label="1 Minutes Backward" icon="exec_restart" mappings=[ON="<< 1 min"]
    Switch item=VLC_Control_10SecondsForward label="10 Seconds Forward" icon="exec_restart" mappings=[ON=">> 10 sec"]
    Switch item=VLC_Control_10SecondsBackward label="10 Seconds Backward" icon="exec_restart" mappings=[ON="<< 10 sec"]
    Switch item=VLC_Control_3SecondsForward label="3 Seconds Forward" icon="exec_restart" mappings=[ON=">> 3 sec"]
    Switch item=VLC_Control_3SecondsBackward label="3 Seconds Backward" icon="exec_restart" mappings=[ON="<< 3 sec"]
    Switch item=VLC_Control_Stop label="Stop" icon="exec_restart" mappings=[ON="Stop"]
    Switch item=VLC_Control_Faster label="Faster" icon="exec_restart" mappings=[ON="faster"]
    Switch item=VLC_Control_Slower label="Slower" icon="exec_restart" mappings=[ON="slower"]
    Switch item=VLC_Control_NormalSpeed label="Normal speed" icon="exec_restart" mappings=[ON="normal speed"]
    Switch item=VLC_Control_NextTrack label="Next track" icon="exec_restart" mappings=[ON=">>|"]
    Switch item=VLC_Control_PreviousTrack label="Previous track" icon="exec_restart" mappings=[ON="|<<"]
    Switch item=VLC_Control_ShowCurrentPostionTime label="Fade in Postion/Time" icon="exec_restart" mappings=[ON="Fade in postion/time"]
    Switch item=VLC_Control_ChangeLoopOption label="Change loop option" icon="exec_restart" mappings=[ON="Change loop option"]
    Switch item=VLC_Control_NextFrame label="Next frame" icon="exec_restart" mappings=[ON="Next Frame"]
    Switch item=VLC_Control_Louder label="Louder" icon="exec_restart" mappings=[ON="Vol +"]
    Switch item=VLC_Control_Quieter label="Quieter" icon="exec_restart" mappings=[ON="Vol -"]
    Switch item=VLC_Control_Mute label="Mute" icon="exec_restart" mappings=[ON="Mute"]
    Switch item=VLC_Control_ToggleFullscreen label="Toggle fullscreen" icon="exec_restart" mappings=[ON="Toggle Fullscreen"]
    Switch item=VLC_Control_DeactivateFullscreen label="Deactivate fullscreen" icon="exec_restart" mappings=[ON="Escape Fullscreen"]
    Switch item=VLC_Control_CreateSnapshot label="Create snapshot" icon="exec_restart" mappings=[ON="Snapshot"]
    Switch item=VLC_Control_StartStopRecording label="Start/stop recording" icon="exec_restart" mappings=[ON="Start/stop recording"]
}
```
