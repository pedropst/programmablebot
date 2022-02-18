from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
from turtle import width

import keyboard
import os
import tkinter as tkinter
import pyautogui
import main
import pickle

class Scenario():
    def __init__(self, list, name) -> None:
        self.name = name
        self.actions = []
        self.parameters = []
        for i in range(len(list)):
            self.actions.append(list[i][0].get())
            self.parameters.append(list[i][1].get())
    
    def toPickle(self, file):
        return pickle.dump(self, file)

HEADER_LEN = 4
actions = ['MOUSE MOVEMENT', 'WAIT', 'SCROLL', 'RIGHT CLICK', 'LEFT CLICK', 'SCROLL CLICK']
variables = {}
lines = []
is_get_pos_enable = False

def save_scenario(scenario_name, lines):
    s = Scenario(lines, scenario_name)
    path = fd.askdirectory()
    file = open(os.path.join(path, scenario_name + '.scen'), 'wb')
    s.toPickle(file)
    file.close()

def load_scenario(parent, row, vars1, acts, acts_lines):
    path = fd.askopenfilename()
    file = open(path, 'rb')
    s = pickle.load(file)
    d = {
         'MOUSE MOVEMENT': 0, 
         'WAIT' : 1, 
         'SCROLL' : 2, 
         'RIGHT CLICK' : 3, 
         'LEFT CLICK' :4, 
         'SCROLL CLICK':5
         }
    # acts_lines = []
    for i in range(0, len(s.parameters)):
        acts_lines[-1][0].current(d[s.actions[i]])
        acts_lines[-1][1].insert(0, s.parameters[i])
        if i < len(s.parameters) - 1:
            add_new_line(parent, row + i, vars1, acts, acts_lines)


    print(len(lines))

def remove_line(row, lines):
    if row > 0:
        t = lines[row]
        for i in range(len(t)):
            t[i].destroy()
        lines.pop(row)

def add_new_line(parent, row, vars, acts, acts_lines):
    vars['action' + str(row)] = tkinter.StringVar()

    action_list = ttk.Combobox(parent, textvariable=vars['action' + str(row)])
    action_list['values'] = acts
    action_list.current(0)
    action_list.grid(row=row, column=0, padx=10, pady=10)

    parameter1 = Entry(parent, width=20)
    parameter1.grid(row=row, column=1, padx=10, pady=10)

    # parameter2 = Entry(parent, width=20)
    # parameter2.grid(row=row, column=2, padx=10, pady=10)

    # lines.append((action_list, parameter1, parameter2))
    lines.append((action_list, parameter1))

def get_pos(entry, root, isEnable):
    isEnable = True
    while 1:
        if isEnable and keyboard.is_pressed('esc') and type(entry) == tkinter.Entry:
            entry.delete(0, END)
            entry.insert(0, f"{str(pyautogui.position().x)},{str(pyautogui.position().y)}")
            root.focus_force()
            break
        if keyboard.is_pressed('esc') and type(entry) != tkinter.Entry:
            break
    isEnable = False

def call(root, commands):
    main.run(commands)

root = tkinter.Tk()
root.title('Programmable Bot -')
root.geometry('490x600')



scenario_selection = ttk.Entry(root, width=22)
scenario_name = scenario_selection.get()
scenario_selection.grid(row=0, column=0, padx=10, pady=10)
save_scenario_button = Button(root, text='Save Scenario', command=lambda: save_scenario(scenario_selection.get(), lines), width=19)
save_scenario_button.grid(row = 0, column=1, sticky='W', padx=10, pady=10)
load_scenario_button = Button(root, text='Load Scenario', command=lambda: load_scenario(root, len(lines) + HEADER_LEN, variables, actions, lines), width=19)
load_scenario_button.grid(row = 0, column=2, sticky='W', padx=10, pady=10)

add_line_button = Button(root, text='+', command=lambda: add_new_line(root, len(lines) + HEADER_LEN, variables, actions, lines), width=19)
add_line_button.grid(row=1, column=0, padx=10, pady=10)
remove_line_button = Button(root, text='-', command=lambda: remove_line(len(lines) - 1, lines), width=19)
remove_line_button.grid(row=1, column=1, padx=10, pady=10)
get_pos_button = Button(root, text='Get Position', command=lambda: get_pos(root.focus_get(), root, is_get_pos_enable), width=19)
get_pos_button.grid(row = 1, column=2, sticky='W', padx=10, pady=10)

run_button = Button(root, text='Run', command=lambda: call(root, lines), width=19)
run_button.grid(row = 2, column=2, sticky='W', padx=10, pady=10)

header_action_label = Label(root, text='ACTION TYPE')
header_action_label.grid(row=2, column=0)
header_parameter1_label = Label(root, text='PARAMETER')
header_parameter1_label.grid(row=2, column=1)
# header_action_label = Label(root, text='SECOND PARAMETER')
# header_action_label.grid(row=2, column=2)

add_new_line(root, HEADER_LEN, variables, actions, lines)








root.mainloop()
