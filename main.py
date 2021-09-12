import keyboard
import time
import mouse
import os

print('AutoMine v1.0')
print('Press E to off/on')
print('\nConsole:')

def wait(int):
    time.sleep(int)

false = False
true = True

Enabled = false
Debounce = false
HoldDebounce = false

while True:
    if keyboard.is_pressed('e'):
        if Enabled == false and Debounce == false:
            Debounce = true
            Enabled = true
            print('Enabled AutoMine, please wait 2 seconds')
            wait(2)
            Debounce = false
        elif Enabled == true and Debounce == false:
            Debounce = true
            Enabled = false
            print('Disabled AutoMine, please wait 2 seconds')
            wait(2)
            Debounce = false
    if Enabled == true:
        if HoldDebounce == false:
            HoldDebounce = true
            mouse.hold('left')
            print('Activated AutoMine')
        # END
    elif Enabled == false:
        if HoldDebounce == true:
            HoldDebounce = false
            mouse.release('left')
            print('Deactivated AutoMine')
input()
