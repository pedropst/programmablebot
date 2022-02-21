from concurrent.futures import thread
import pyautogui
import time
import threading
import loops
import random 

class Script(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.commands = None
        self.isAlive = True

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
        for m in range(int(self.commands[0][1].get()) +1):
            self.virtual_button(1)
            self.virtual_button(5)
            self.virtual_button(9)
            self.virtual_button(13)
            self.virtual_button(17)
            self.virtual_button(21)
            self.virtual_button(25)
            self.virtual_button(29)
                # if m%15 != 0 or m == 0:
                #     self.virtual_button(1)
                #     self.virtual_button(5)
                #     self.virtual_button(9)
                #     self.virtual_button(17)
                #     self.virtual_button(21)
                #     self.virtual_button(25)
                #     self.virtual_button(29)
                # else:
                #     self.virtual_button(5)
                #     self.virtual_button(9)
            # self.virtual_button(13)




            # if m != 15 and m != 30 and m != 45:
            #     #button1
            #     pyautogui.moveTo(x=int(self.commands[2][1].get().split(',')[0]), y=int(self.commands[2][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     #button2
            #     pyautogui.moveTo(x=int(self.commands[3][1].get().split(',')[0]), y=int(self.commands[3][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button3
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button4
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button5
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button6
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button7
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button8
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            # else:
            #     #button2
            #     pyautogui.moveTo(x=int(self.commands[3][1].get().split(',')[0]), y=int(self.commands[3][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button3
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button9
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     # button10
            #     pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
            #     pyautogui.click(clicks=1, button=pyautogui.LEFT)
            #     time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
            #     pass

            # time.sleep(float(self.commands[7][1].get()) + (random.random()/10))
            # #button4
            # pyautogui.moveTo(x=int(self.commands[5][1].get().split(',')[0]), y=int(self.commands[5][1].get().split(',')[1]))
            # pyautogui.click(clicks=1, button=pyautogui.LEFT)