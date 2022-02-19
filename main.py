from concurrent.futures import thread
import pyautogui
import time
import threading
import loops
import random 

def handle_loop1(commands, count):
    count = int(commands[1][1].get())
    # button1 = pyautogui.moveTo(x=int(commands[2][1].get().split(',')[0]), y=int(commands[2][1].get().split(',')[1]))
    # button2 = pyautogui.moveTo(x=int(commands[5][1].get().split(',')[0]), y=int(commands[5][1].get().split(',')[1]))
    # button3 = pyautogui.moveTo(x=int(commands[8][1].get().split(',')[0]), y=int(commands[8][1].get().split(',')[1]))
    # button4 = pyautogui.moveTo(x=int(commands[12][1].get().split(',')[0]), y=int(commands[12][1].get().split(',')[1]))
    # click = pyautogui.click(clicks=int(commands[i][1].get()), button=pyautogui.LEFT)

    time.sleep(int(commands[0][1].get()))
    for m in range(count+1):
        if m != 15 and m != 30 and m != 45:
            #button1
            pyautogui.moveTo(x=int(commands[2][1].get().split(',')[0]), y=int(commands[2][1].get().split(',')[1]))
            pyautogui.click(clicks=1, button=pyautogui.LEFT)
            time.sleep(int(commands[4][1].get()))
            #button2
            pyautogui.moveTo(x=int(commands[5][1].get().split(',')[0]), y=int(commands[5][1].get().split(',')[1]))
            pyautogui.click(clicks=1, button=pyautogui.LEFT)
            time.sleep(int(commands[7][1].get()))
            # button3
            pyautogui.moveTo(x=int(commands[8][1].get().split(',')[0]), y=int(commands[8][1].get().split(',')[1]))
            pyautogui.click(clicks=1, button=pyautogui.LEFT)
            time.sleep(int(commands[10][1].get()))
        else:
            #button2
            pyautogui.moveTo(x=int(commands[5][1].get().split(',')[0]), y=int(commands[5][1].get().split(',')[1]))
            pyautogui.click(clicks=1, button=pyautogui.LEFT)
            time.sleep(int(commands[7][1].get()))
                        # button3
            pyautogui.moveTo(x=int(commands[8][1].get().split(',')[0]), y=int(commands[8][1].get().split(',')[1]))
            pyautogui.click(clicks=1, button=pyautogui.LEFT)
            time.sleep(int(commands[10][1].get()))
            pass

    time.sleep(int(commands[11][1].get()))
    pyautogui.moveTo(x=int(commands[12][1].get().split(',')[0]), y=int(commands[12][1].get().split(',')[1]))
    pyautogui.click(clicks=1, button=pyautogui.LEFT)

    # for m in range(count):
    #     for i in range(len(commands)):
    #         if commands[i][0].get() == 'MOUSE MOVEMENT':
    #             pyautogui.moveTo(x=int(commands[i][1].get().split(',')[0]), y=int(commands[i][1].get().split(',')[1]))
    #         elif commands[i][0].get() == 'WAIT':
    #             time.sleep(int(commands[i][1].get()))
    #         elif commands[i][0].get() == 'SCROLL':
    #             pyautogui.scroll(int(commands[i][1].get()))
    #         elif commands[i][0].get() == 'LEFT CLICK':
    #             if not commands[i][1].get().__contains__(','):
    #                 pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.LEFT)
    #             else:
    #                 pyautogui.click(clicks=int(commands[i][1].get().split(',')[0]), interval=float(commands[i][1].get().split(',')[1]), button=pyautogui.LEFT)
    #         elif commands[i][0].get() == 'RIGHT CLICK':
    #             pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.RIGHT)
    #         elif commands[i][0].get() == 'SCROLL CLICK':
    #             pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.MIDDLE)

def handle_loop(commands, count):
    print(commands)
    print(count)
    for k in range(count):
        for i in range(len(commands)):
            if commands[i][0].get() == 'MOUSE MOVEMENT':
                pyautogui.moveTo(x=int(commands[i][1].get().split(',')[0]), y=int(commands[i][1].get().split(',')[1]))
            elif commands[i][0].get() == 'WAIT':
                time.sleep(int(commands[i][1].get()))
            elif commands[i][0].get() == 'SCROLL':
                pyautogui.scroll(int(commands[i][1].get()))
            elif commands[i][0].get() == 'LEFT CLICK':
                if not commands[i][1].get().__contains__(','):
                    pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.LEFT)
                else:
                    pyautogui.click(clicks=int(commands[i][1].get().split(',')[0]), interval=float(commands[i][1].get().split(',')[1]), button=pyautogui.LEFT)
            elif commands[i][0].get() == 'RIGHT CLICK':
                pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.RIGHT)
            elif commands[i][0].get() == 'SCROLL CLICK':
                pyautogui.click(clicks=int(commands[i][1].get()), interval=0.02, button=pyautogui.MIDDLE)
            elif commands[i][0].get() == 'START LOOP':
                j = 1
                loop_commands = []
                itet = int(commands[i][1].get().split(',')[1])
                while (commands[i + j][0].get() != 'END LOOP') and (commands[i + j][1].get() == commands[i][1].get().split(',')[0]):
                    loop_commands.append(commands[i + j])
                    j += 1
                handle_loop1(loop_commands, itet)

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

    def run(self):
        self.isAlive = False
        for j in range(int(self.commands[0][1].get()) + 1):
            for m in range(int(self.commands[1][1].get()) +1):
                if m != 15 and m != 30 and m != 45:
                    #button1
                    pyautogui.moveTo(x=int(self.commands[2][1].get().split(',')[0]), y=int(self.commands[2][1].get().split(',')[1]))
                    pyautogui.click(clicks=1, button=pyautogui.LEFT)
                    time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
                    #button2
                    pyautogui.moveTo(x=int(self.commands[3][1].get().split(',')[0]), y=int(self.commands[3][1].get().split(',')[1]))
                    pyautogui.click(clicks=1, button=pyautogui.LEFT)
                    time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
                    # button3
                    pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
                    pyautogui.click(clicks=1, button=pyautogui.LEFT)
                    time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
                else:
                    #button2
                    pyautogui.moveTo(x=int(self.commands[3][1].get().split(',')[0]), y=int(self.commands[3][1].get().split(',')[1]))
                    pyautogui.click(clicks=1, button=pyautogui.LEFT)
                    time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
                    # button3
                    pyautogui.moveTo(x=int(self.commands[4][1].get().split(',')[0]), y=int(self.commands[4][1].get().split(',')[1]))
                    pyautogui.click(clicks=1, button=pyautogui.LEFT)
                    time.sleep(float(self.commands[6][1].get()) + (random.random()/10))
                    pass

            time.sleep(float(self.commands[7][1].get()) + (random.random()/10))
            #button4
            pyautogui.moveTo(x=int(self.commands[5][1].get().split(',')[0]), y=int(self.commands[5][1].get().split(',')[1]))
            pyautogui.click(clicks=1, button=pyautogui.LEFT)