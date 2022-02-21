from pathlib import PosixPath
import threading
import pyautogui
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
import tkinter as tkinter
from pynput import keyboard
import time

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

class Postion(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.root = None
        self.entry = None
        self.isEnable = None

    def on_press(self, key):
        try:
            self.entry.delete(0, END)
            self.entry.insert(0, f"{str(pyautogui.position().x)},{str(pyautogui.position().y)}")
            self.root.focus_force()
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def callback(self):
        pass

    def call(self, entry, isEnable, root):
        self.root = root
        self.isEnable = isEnable
        self.entry = entry
        self.start()

    def run(self):
        isEnable = True
        if isEnable and type(self.entry) == tkinter.Entry:
            time.sleep(5)
            self.entry.delete(0, END)
            self.entry.insert(0, f"{str(pyautogui.position().x)},{str(pyautogui.position().y)}")
            self.root.focus_force()
            # with keyboard.Listener(
            #     on_press=self.on_press,
            #     on_release=on_release) as listener:
            #     listener.join()
        # isEnable = True
        # while 1:
        #     if isEnable and keyboard.is_pressed('esc') and type(self.entry) == tkinter.Entry:
        #         self.entry.delete(0, END)
        #         self.entry.insert(0, f"{str(pyautogui.position().x)},{str(pyautogui.position().y)}")
        #         self.root.focus_force()
        #         break
        #     if keyboard.is_pressed('esc') and type(self.entry) != tkinter.Entry:
        #         break
        # isEnable = False


# p = Postion().start()

