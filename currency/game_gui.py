#!/usr/bin/env python3
################################################################################
#   game_gui.py
#
#   Game view
#
#   02.08.2018  Created by:  rada
################################################################################
from tkinter import *
from game import *

class GameGUI():
    def __init__(self, master, game):
        self.master = master
        
        # Default attributes
        self.master.title = "Назовите валюту страны"
        self.master.geometry(self.center(master))
        self.master.attributes('-topmost', True)
        self.master.config(background='lightblue')

        # Widgets
        self.top_frame = Frame(self.master, width=300, height=400, bg='pink')
        self.top_frame.grid(row=0, sticky=W)
        
        self.label_question = Label(self.top_frame, text="Страна", background='lightblue')
        self.label_question.grid(row=0, sticky=E)
        
        self.question_box = Text(self.top_frame, width=20, height=1, bg='light grey')
        self.question_box.grid(row=0, column=1, sticky=W)
        
        self.label_reply = Label(self.top_frame, text="Введите валюту", background='lightblue')
        self.label_reply.grid(row=0, column=2, sticky=E)
        
        self.reply_box = Entry(self.top_frame, width=20, bg='light grey', bd=5)
        self.reply_box.grid(row=0, column=3, sticky=W)
        
        self.button_reply = Button(self.top_frame, text='Ответить', command=game.reply)
        self.button_reply.grid(row=0, column=4, sticky=E)
        self.button_reply.config(state=DISABLED)
        
        self.result_box = Text(self.top_frame, width=90, height=20, bg='cyan')
        self.result_box.grid(row=1, columnspan=5, sticky=W)
        
        self.bottom_frame = Frame(self.master, width=300, height=400, bg='light green')
        self.bottom_frame.grid(row=2, sticky=W)
        
        self.button_quit = Button(self.bottom_frame, text='Закончить', command=game.quit)
        self.button_quit.grid(row=0, column=1, sticky=E)

        self.button_start = Button(self.bottom_frame, text='Начать', command=lambda: game.start(self))
        self.button_start.grid(row=0, column=0, sticky=E)        
        
    def center(self, master):
        master_width  = 800
        master_height = 600
        
        screen_width    = master.winfo_screenwidth()
        screen_height  = master.winfo_screenheight()

        master_x = (screen_width  - master_width)/2
        master_y = (screen_height - master_height)/2
        return('%dx%d+%d+%d' % (master_width, master_height, master_x, master_y))
