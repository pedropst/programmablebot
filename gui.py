from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
import os
import tkinter as tkinter
import main
import pickle
import threading
import position

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


def get_pos(entry, root, isEnable):
    p = position.Postion()
    p.call(entry, isEnable, root)


    

class Interface(threading.Thread):
    def __init__(self) -> None:
        threading.Thread.__init__(self)
        self.HEADER_LEN = 1
        self.ACTIONS = ['LOOP', 'BUTTON1', 'BUTTON2', 'BUTTON3', 'BUTTON4', 'BUTTON5', 
        'BUTTON6', 'BUTTON7', 'BUTTON8', 'WAIT AFTER BUTTON', 'WAIT BETWEEN CLICKS', 'REPEAT BUTTON']
        # self.ACTIONS = ['MOUSE MOVEMENT', 'WAIT', 'SCROLL', 'RIGHT CLICK', 'LEFT CLICK', 'SCROLL CLICK', 'START LOOP', 'END LOOP']
        self.lines = []
        self.is_get_pos_enable = False
        self.frame_options = None
        self.canvas = None
        self.script = main.Script()
        self.start()
    
    def callback():
        pass

    def call(self, root, commands):
        self.script.call(commands)
        self.script = main.Script()

    def remove_line(self, row, lines):
        if row >= 0:
            t = lines[row]
            for i in range(len(t)):
                t[i].destroy()
            lines.pop(row)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def save_scenario(self, scenario_name, lines):
        s = Scenario(lines, scenario_name)
        path = fd.askdirectory()
        file = open(os.path.join(path, scenario_name + '.scen'), 'wb')
        s.toPickle(file)
        file.close()

    def load_scenario(self, parent, row):
        path = fd.askopenfilename()
        file = open(path, 'rb')
        s = pickle.load(file)
        d = {
            'LOOP' : 0,
            'BUTTON1' : 1,
            'BUTTON2' : 2,
            'BUTTON3' : 3,
            'BUTTON4': 4,
            'BUTTON5': 5,
            'BUTTON6': 6,
            'BUTTON7': 7,
            'BUTTON8': 8,
            'WAIT AFTER BUTTON' : 9,
            'WAIT BETWEEN CLICKS' : 10,
            'REPEAT BUTTON' : 11
            }

        while len(self.lines) > 0:
            t = self.lines[0]
            for i in range(len(t)):
                t[i].destroy()
            self.lines.pop(0)

        # self.lines = []

        for i in range(0, len(s.parameters)):
            self.add_new_line(parent, row + i)
            self.lines[-1][0].current(d[s.actions[i]])
            self.lines[-1][1].insert(0, s.parameters[i])


    def add_new_line(self, parent, row):
        action_list = ttk.Combobox(parent)
        action_list['values'] = self.ACTIONS
        action_list.current(0)
        action_list.grid(row=row, column=0, sticky='news')
        # action_list.grid(row=row, column=0, padx=10, pady=5)

        parameter1 = Entry(parent, width=20)
        parameter1.grid(row=row, column=1, stick='news')

        parent.update_idletasks()
        # parameter1.grid(row=row, column=1, padx=10, pady=5)

        self.lines.append((action_list, parameter1))
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def run(self):
        root = tkinter.Tk()
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.title('Programmable Bot -')
        root.geometry('400x520')

        frame_main = Frame(root, bg='gray')
        frame_main.grid(stick='news')

        scenario_selection = ttk.Entry(frame_main, width=23)
        scenario_selection.grid(row=0, column=0, padx=10, pady=5)
        save_scenario_button = Button(frame_main, text='Save Scenario', command=lambda: self.save_scenario(scenario_selection.get(), self.lines), width=19)
        save_scenario_button.grid(row = 1, column=0, padx=10, pady=5)
        load_scenario_button = Button(frame_main, text='Load Scenario', command=lambda: self.load_scenario(self.frame_options, len(self.lines) + self.HEADER_LEN), width=19)
        load_scenario_button.grid(row = 2, column=0, padx=10, pady=5)

        add_line_button = Button(frame_main, text='+', command=lambda: self.add_new_line(self.frame_options, len(self.lines) + self.HEADER_LEN), width=19)
        add_line_button.grid(row=3, column=0, padx=10, pady=5)
        remove_line_button = Button(frame_main, text='-', command=lambda: self.remove_line(len(self.lines) - 1, self.lines), width=19)
        remove_line_button.grid(row=4, column=0, padx=10, pady=5)
        get_pos_button = Button(frame_main, text='Get Position', command=lambda: get_pos(root.focus_get(), frame_main, self.is_get_pos_enable), width=19)
        get_pos_button.grid(row = 5, column=0, padx=10, pady=5)

        run_button = Button(frame_main, text='Run', command=lambda: self.call(frame_main, self.lines), width=19)
        run_button.grid(row = 6, column=0, padx=10, pady=5)

        frame_action = Frame(frame_main)
        frame_action.grid(row=8, column=0, pady=(5, 0), sticky='nw')
        frame_action.grid_rowconfigure(0, weight=1)
        frame_action.grid_columnconfigure(0, weight=1)
        # frame_action.grid_propagate(False)

        self.canvas = Canvas(frame_action)
        self.canvas.grid(row=0, column=0, sticky='news')

        vsb = Scrollbar(frame_action, orient='vertical', command=self.canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=vsb.set)

    
        self.frame_options = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.frame_options, anchor='nw')

        header_action_label = Label(self.frame_options, text='ACTION TYPE', width=23, font='Helvetica 10 bold')
        header_action_label.grid(row=0, column=0, sticky='news')
        header_parameter1_label = Label(self.frame_options, text='PARAMETER', width=23, font='Helvetica 10 bold')
        header_parameter1_label.grid(row=0, column=1, sticky='news')
        # self.add_new_line(root, self.HEADER_LEN)

        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        root.mainloop()

i = Interface()