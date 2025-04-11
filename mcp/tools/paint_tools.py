import pyautogui
import time
import pygetwindow as gw
import subprocess

def open_paint():
    subprocess.Popen("mspaint")
    time.sleep(2)

    paint_window = None
    for window in gw.getWindowsWithTitle("Paint"):
        if "Paint" in window.title:
            paint_window = window
            break

    if paint_window:
        paint_window.activate()
        paint_window.maximize()
        print("Paint window activated.")
    else:
        print("Paint window not found.")

def draw_rectangle():
    print("Drawing rectangle...")
    win = gw.getWindowsWithTitle("Untitled - Paint")[0]
    win.activate()
    win.maximize()
    time.sleep(10)

    pyautogui.moveTo(549, 893)  # Move to rectangle tool
    pyautogui.click()
    time.sleep(10)  #

    pyautogui.click(1000, 380)  # Focus canvas
    time.sleep(10)

    pyautogui.moveTo(800, 700, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(1000, 620, duration=1)
    pyautogui.mouseUp()
    print("Rectangle tool clicked. Pausing for visual confirmation...")
    time.sleep(2)

def add_text_in_paint(text):
    print(f"Adding text in Paint...")

    # Step 1: Click on Text Tool
    pyautogui.moveTo(600, 893)
    pyautogui.click()
    time.sleep(10)

    # Step 2: Click and drag to create a visible text box inside the rectangle
    pyautogui.moveTo(800, 660)  # Start point inside rectangle
    pyautogui.mouseDown()
    pyautogui.moveTo(1000, 700, duration=0.5)  # Drag to make the text box
    pyautogui.mouseUp()
    time.sleep(1)

    # Step 3: Type text after textbox is confirmed
    pyautogui.write(text, interval=0.1)
    print(f"Text added: {text}")