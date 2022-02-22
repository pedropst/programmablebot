import pyautogui
import random
import time
import threading

class Script(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.commands = None
        self.isAlive = True
        self.isStopped = False

    def callback(self):
        pass
    
    def call(self, commands):
        self.commands = commands
        if self.isAlive is True:
            self.start()

    def virtual_button(self, pos):
        if self.commands[pos][1].get() != '':
            pyautogui.moveTo(x=int(self.commands[pos][1].get().split(',')[0]), y=int(self.commands[pos][1].get().split(',')[1]))
            pyautogui.click(clicks=int(self.commands[pos+1][1].get()), button=pyautogui.LEFT, interval=float(self.commands[pos+2][1].get()))
            time.sleep(float(self.commands[pos+3][1].get()) + (random.random()/10))

    def run(self):
        self.isAlive = False
        button_count = len(self.commands)-1
        button_count = int(button_count/4)
        for _ in range(int(self.commands[0][1].get())):
            if not self.isStopped:
                for j in range(0, button_count):
                    if not self.isStopped:
                        self.virtual_button(1 + j*4)
                    else:
                        break
            else:
                break

