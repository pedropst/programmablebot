import pyautogui
import time

def run(commands):
    for i in range(len(commands)):
        if commands[i][0].get() == 'MOUSE MOVEMENT':
            pyautogui.moveTo(x=int(commands[i][1].get().split(',')[0]), y=int(commands[i][1].get().split(',')[1]))
        elif commands[i][0].get() == 'WAIT':
            time.sleep(int(commands[i][1].get()))
        elif commands[i][0].get() == 'SCROLL':
            pyautogui.scroll(int(commands[i][1].get()))
        elif commands[i][0].get() == 'LEFT CLICK':
            pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.LEFT)
        elif commands[i][0].get() == 'RIGHT CLICK':
            pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.RIGHT)
        elif commands[i][0].get() == 'SCROLL CLICK':
            pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.MIDDLE)