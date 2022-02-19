from concurrent.futures import thread
import pyautogui
import time
import threading

def handle_loop1(commands, count):
    for m in range(count):
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

    def run(self, commands):
        self.isAlive = False
        runcommand = []
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
                while (commands[i + j][0].get() != 'END LOOP') and (commands[i + j][1].get() == commands[i][1].get().split(',')[0]) and commands[i + j][0].get() != 'START LOOP':
                    loop_commands.append(commands[i + j])
                    j += 1
                for _ in range(itet):
                    runcommand.append(loop_commands)
                # print(loop_commands)
                # handle_loop(loop_commands, itet)
        self = None