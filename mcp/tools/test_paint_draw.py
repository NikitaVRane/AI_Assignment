import pyautogui
import time
import subprocess
import pygetwindow as gw

# Step 1: Open Paint
subprocess.Popen("mspaint")
time.sleep(10)

# Step 2: Bring Paint to front
try:
    win = gw.getWindowsWithTitle("Paint")[0]
    win.activate()
    win.maximize()
    time.sleep(1)
except:
    print("Fallback to Alt-Tab")
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(1)

# Step 3: Draw a rectangle directly (no tool selection yet)
print("Drawing rectangle now...")
pyautogui.moveTo(300, 300)
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.moveTo(600, 500)
pyautogui.mouseUp()
print("Done.")
