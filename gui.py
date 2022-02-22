from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk

import os
import pickle
import position
import tkinter as tkinter

import main


class Scenario():
    def __init__(self, list, name) -> None:
        self.name = name
        self.actions = []
        self.parameters = []
        for i in range(len(list)):
            self.actions.append(list[i][0]['text'])
            self.parameters.append(list[i][1].get())
    
    def toPickle(self, file):
        return pickle.dump(self, file)


def get_pos(entry, root, isEnable):
    p = position.Postion()
    p.call(entry, isEnable, root)


class Interface():
    def __init__(self) -> None:
        self.HEADER_LEN = 1
        self.ACTIONS = ['LOOP', 'BUTTON1', 'BUTTON2', 'BUTTON3', 'BUTTON4', 'BUTTON5', 
        'BUTTON6', 'BUTTON7', 'BUTTON8', 'REPEAT BUTTON', 'WAIT BETWEEN CLICKS', 'WAIT AFTER BUTTON']
        self.lines = []
        self.is_get_pos_enable = False
        self.frame_options = None
        self.canvas = None
        self.script = None
        self.bot_stop = False
        self.scenario_selection = None
        self.run()
    
    def callback():
        pass

    def call(self, root, commands):
        self.script = main.Script()
        self.script.call(commands)
        
    def pause(self, stop):
        self.script.isStopped = True

    def remove_line(self, row, lines):
        if row >= 1:
            for _ in range(0, 4):
                t = self.lines[-1]
                for i in range(len(t)):
                    t[i].destroy()
                self.lines.pop(-1)
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

        while len(self.lines) > 0:
            t = self.lines[0]
            for i in range(len(t)):
                t[i].destroy()
            self.lines.pop(0)

        for i in range(0, len(s.parameters)):
            self.add_new_line(parent, i)
            self.lines[-1][0].config(text = s.actions[i])
            self.lines[-1][1].insert(0, s.parameters[i])
        
        self.scenario_selection.delete(0, END)
        self.scenario_selection.insert(0, path.split('/')[-1].replace('.scen', ''))
            

    def add_new_line(self, parent, row):
        action_list = Label(parent, text='LOOP')
        action_list.grid(row=row, column=0, sticky='news')
        action_list.grid(row=row, column=0, padx=10, pady=5)

        parameter1 = Entry(parent, width=20)
        parameter1.grid(row=row, column=1, stick='news')

        parent.update_idletasks()

        self.lines.append((action_list, parameter1))
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def add_new_button(self, parent, row):
        button_index = str(int(1 + row/4))
        for i in range(4):
            dic_action = {
                0: 'BUTTON ' + button_index,
                1: 'REPEAT BUTTON ' + button_index,
                2: 'WAIT BETWEEN CLICKS ' + button_index,
                3: 'WAIT AFTER BUTTON ' + button_index
            }

            dic_parameter = {
                0: '',
                1: '1',
                2: '0',
                3: '0.5'
            }

            action_list = Label(parent, text=dic_action[i])
            action_list.grid(row=row+i+1, column=0, sticky='news')
            action_list.grid(row=row+i+1, column=0, padx=10, pady=5)

            parameter1 = Entry(parent, width=20)
            parameter1.insert(0, dic_parameter[i])
            parameter1.grid(row=row+i+1, column=1, stick='news')

            parent.update_idletasks()

            self.lines.append((action_list, parameter1))
            self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def stop_bot(self):
        if self.script != None:
            self.script.isStopped = True

    def run(self):
        root = tkinter.Tk()
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.title('Programmable Bot -')
        root.geometry('400x560')
        root.maxsize(width=400, height=560)
        root.minsize(width=400, height=560)

        frame_main = Frame(root)
        frame_main.grid(stick='news')

        self.scenario_selection = ttk.Entry(frame_main, width=23)
        self.scenario_selection.grid(row=0, column=0, padx=10, pady=5)

        load_scenario_button = Button(frame_main, text='Load Scenario', command=lambda: self.load_scenario(self.frame_options, len(self.lines) + self.HEADER_LEN), width=19)
        load_scenario_button.grid(row = 1, column=0, padx=10, pady=5)

        add_line_button = Button(frame_main, text='+', command=lambda: self.add_new_button(self.frame_options, len(self.lines) + self.HEADER_LEN), width=19)
        add_line_button.grid(row=2, column=0, padx=10, pady=5)

        remove_line_button = Button(frame_main, text='-', command=lambda: self.remove_line(len(self.lines) - 1, self.lines), width=19)
        remove_line_button.grid(row=3, column=0, padx=10, pady=5)

        get_pos_button = Button(frame_main, text='Get Position', command=lambda: get_pos(root.focus_get(), frame_main, self.is_get_pos_enable), width=19)
        get_pos_button.grid(row = 4, column=0, padx=10, pady=5)

        save_scenario_button = Button(frame_main, text='Save Scenario', command=lambda: self.save_scenario(scenario_selection.get(), self.lines), width=19)
        save_scenario_button.grid(row = 5, column=0, padx=10, pady=5)

        run_button = Button(frame_main, text='Run', command=lambda: self.call(frame_main, self.lines), width=19)
        run_button.grid(row = 6, column=0, padx=10, pady=5)

        stop_button = Button(frame_main, text='Stop', command=lambda: self.stop_bot(), width=19)
        stop_button.grid(row = 7, column=0, padx=10, pady=5)

        frame_action = Frame(frame_main)
        frame_action.grid(row=8, column=0, pady=(5, 0), sticky='nw')
        frame_action.grid_rowconfigure(0, weight=1)
        frame_action.grid_columnconfigure(0, weight=1)

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
        self.add_new_line(self.frame_options, len(self.lines) + self.HEADER_LEN)

        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        root.mainloop()


i = Interface()

