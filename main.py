from concurrent.futures import thread
import pyautogui
import time
import threading

class Script(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.commands = None
        self.isAlive = True

    def callback(self):
        self.join()

    def call(self, commands):
        self.commands = commands
        if self.isAlive is True:
            self.start()

    def run(self):
        self.isAlive = False
        for i in range(len(self.commands)):
            if self.commands[i][0].get() == 'MOUSE MOVEMENT':
                pyautogui.moveTo(x=int(self.commands[i][1].get().split(',')[0]), y=int(self.commands[i][1].get().split(',')[1]))
            elif self.commands[i][0].get() == 'WAIT':
                time.sleep(int(self.commands[i][1].get()))
            elif self.commands[i][0].get() == 'SCROLL':
                pyautogui.scroll(int(self.commands[i][1].get()))
            elif self.commands[i][0].get() == 'LEFT CLICK':
                pyautogui.click(clicks=int(self.commands[i][1].get()), interval=0.02, button=pyautogui.LEFT)
            elif self.commands[i][0].get() == 'RIGHT CLICK':
                pyautogui.click(clicks=int(self.commands[i][1].get()), interval=0.02, button=pyautogui.RIGHT)
            elif self.commands[i][0].get() == 'SCROLL CLICK':
                pyautogui.click(clicks=int(self.commands[i][1].get()), interval=0.02, button=pyautogui.MIDDLE)