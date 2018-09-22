#!/usr/bin/env python3
################################################################################
#   game.py
#
#   Game controller
#
#   02.08.2018  Created by:  rada
################################################################################
import sys
import time
from   tkinter import *

from valuta import *

class Game():
    def __init__(self):
        self.attempts = 10
        self.current_country = ''
        self.currency = Currency()
        self.gui_object = None

        
    def lap(self):
        if (self.attempt < self.attempts):
            self.current_country = self.currency.countries[self.attempt]
            self.gui_object.question_box.delete(1.0, END)
            self.gui_object.reply_box.delete(0, END)
            self.gui_object.question_box.insert(END, self.current_country)
            self.attempt += 1
#            print(self.current_country)
        else:
            self.report()
    
    def quit(self):
        print("...Completed")
        sys.exit(0)
    
    def reply(self):
        answer = self.gui_object.reply_box.get().strip().lower()
        message  = '\nВаш ответ: ' + self.current_country + ' - ' + answer
        
        if (answer == self.currency.valuta[self.current_country]):
            self.scores += 1
            message += '  ... Правильно!'
            tag = 'correct'
        else:
            message = '\nНеверно! Правильный ответ: ' + self.currency.valuta[self.current_country]
            tag = 'incorrect'
        
        self.gui_object.result_box.insert(END, message, tag)
        self.lap()
    
    def report(self):
        if   (self.scores <  3): text = '\n"Молодец!" 2'
        elif (self.scores <  5): text = '\n"Молодец!" 3'
        elif (self.scores <  8): text = '\nХорошо! 4'
        elif (self.scores < 10): text = '\nТы крут! 5'    
        else:                text = '\nТЫ ГЕНИЙ!!! 5+'        
    
        self.gui_object.result_box.insert(END, text, 'result')
        self.gui_object.button_reply.config(state=DISABLED)
        self.gui_object.button_start.config(state=NORMAL)
        
    def start(self, gui_object):
        self.attempt = 0
        self.scores  = 0
        self.currency.reset()
        print('Start...')    
        
        if (self.gui_object is None):
            self.gui_object = gui_object
            self.gui_object.result_box.tag_config("correct",   foreground='darkgreen')
            self.gui_object.result_box.tag_config("incorrect", foreground='red')
            self.gui_object.result_box.tag_config("result",    foreground='blue', background='pink')
        
        gui_object.result_box.delete(1.0, END)
        gui_object.question_box.delete(1.0, END)
        gui_object.reply_box.delete(0, END)
        gui_object.button_start.config(state=DISABLED)
        gui_object.button_reply.config(state=NORMAL)
        
        self.lap()