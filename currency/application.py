#!/usr/bin/env python3
################################################################################
#   applicaition.py
#
#   This module initializes and runs the App
#
#   01.08.2018  Created by:  rada
################################################################################
#from tkinter import *

from game     import *
from game_gui import *
from valuta   import *

class Application:
  def __init__(self):
    self.game = Game()
    self.root = Tk()
    self.gui  = GameGUI(self.root, self.game)
