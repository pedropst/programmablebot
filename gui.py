from cgitb import text
from email import header
from operator import le
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk

import os
import tkinter as tkinter
import pyautogui

HEADER_LEN = 3
actions = ['MOUSE MOVEMENT', 'WAIT', 'SCROLL', 'RIGHT CLICK', 'LEFT CLICK', 'SCROLL CLICK']
variables = {}
lines = []

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
    action_list.current = acts[0]
    action_list.grid(row=row, column=0, padx=10, pady=10)

    parameter1 = Entry(parent, width=20)
    parameter1.grid(row=row, column=1, padx=10, pady=10)

    # parameter2 = Entry(parent, width=20)
    # parameter2.grid(row=row, column=2, padx=10, pady=10)

    # lines.append((action_list, parameter1, parameter2))
    lines.append((action_list, parameter1))


root = tkinter.Tk()
root.title('Programmable Bot -')
root.geometry('600x600')

scenario_name = tkinter.StringVar()
scenario_selection = ttk.Combobox(root, textvariable=scenario_name)
scenario_selection['values'] = ['Main']
scenario_selection.grid(row=0, column=0, sticky='W', padx=10, pady=10)
save_scenario_button = Button(root, text='Save Scenario', width=19)
save_scenario_button.grid(row = 0, column=1, sticky='W', padx=10, pady=10)
run_button = Button(root, text='Run', width=19)
run_button.grid(row = 0, column=2, sticky='W', padx=10, pady=10)

add_line_button = Button(root, text='+', command=lambda: add_new_line(root, len(lines) + HEADER_LEN, variables, actions, lines), width=19)
add_line_button.grid(row=1, column=0, padx=10, pady=10)
remove_line_button = Button(root, text='-', command=lambda: remove_line(len(lines) - 1, lines), width=19)
remove_line_button.grid(row=1, column=1, padx=10, pady=10)
get_pos_button = Button(root, text='Get Position', width=19)
get_pos_button.grid(row = 1, column=2, sticky='W', padx=10, pady=10)


header_action_label = Label(root, text='ACTION TYPE')
header_action_label.grid(row=2, column=0)
header_parameter1_label = Label(root, text='FIRST PARAMETER')
header_parameter1_label.grid(row=2, column=1)
# header_action_label = Label(root, text='SECOND PARAMETER')
# header_action_label.grid(row=2, column=2)

print(scenario_selection.grid_info())

add_new_line(root, HEADER_LEN, variables, actions, lines)








root.mainloop()