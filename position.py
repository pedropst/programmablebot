from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

import pyautogui
import time
import threading
import tkinter as tkinter


class Postion(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.root = None
        self.entry = None
        self.isEnable = None

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
            time.sleep(3)
            self.entry.delete(0, END)
            self.entry.insert(0, f"{str(pyautogui.position().x)},{str(pyautogui.position().y)}")
            self.root.focus_force()

