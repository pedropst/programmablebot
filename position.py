import threading
import pyautogui
import keyboard
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
import tkinter as tkinter

class Position(threading.Thread):
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
        while 1:
            if isEnable and keyboard.is_pressed('esc') and type(self.entry) == tkinter.Entry:
                self.entry.delete(0, END)
                self.entry.insert(0, f"{str(pyautogui.position().x)},{str(pyautogui.position().y)}")
                self.root.focus_force()
                break
            if keyboard.is_pressed('esc') and type(self.entry) != tkinter.Entry:
                break
        isEnable = False