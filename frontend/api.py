

import tkinter as tk
from tkinter import filedialog
from interpreter import interpreter

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))



# here you can call you functions 
from initial_vals import *

class Api ():

    def __init__(self,root, editor, terminal, lexemes,variables) -> None:
        self.root = root
        self.editor = editor
        self.terminal = terminal
        self.lexemes = lexemes
        self.variables = variables

    def open_file_dialog(self):
        """ Open file 
        function  when button is clicked to look for files
        """
        file_path = filedialog.askopenfilename(initialdir = "testcases")
        if file_path:
            f =  open(file_path, "r")
            code = f.readlines()
            self.editor.delete(1.0, tk.END)  # Clear previous content
            self.editor.insert(tk.END, "".join(code)) 
            self.__get_results(code)

    def execute (self):
        """ Execute
        will execute the code in the IDE
        """
        text_data = self.editor.get("1.0", tk.END)
        code = [x+'\n' for x in text_data.split('\n') if x]
        self.__get_results(code)

    def show_data(self):
        """Show data
        this will show the data in the frontend, also this is used byt hte input command
        """
        self.terminal.delete(1.0, tk.END)
        self.terminal.insert(tk.END, self.tab.terminal) 
        self.__create_lexemes(self.tab.lexemes)
        self.__create_variables(self.tab.variables)

        
    def on_enter_pressed(self, event):
        """On enter 
        is the terminal has been entered. this will be triggered
        """
        text_data = self.terminal.get("1.0", tk.END) # Get data from the Text widget
        text = text_data[len(self.tab.terminal):]
        self.tab.terminal += text
        self.tab.buffer.set(text)

    def __get_results(self, code):
        """ get results
        will trigger the interpreter
        """
        self.tab = Tables_Values(self.root)
        self.tab.buffer = tk.StringVar()
        self.tab.show_data = self.show_data
        interpreter(code, self.tab)
        self.show_data()


    def __create_lexemes (self, lex):
        """ create lexemes
        This will populate the lexeme table
        """
        self.lexemes.delete(1.0, tk.END)  # Clear previous content
        self.lexemes.insert(tk.END, "".join(["" if l=='\n' else f"{l}\t\t\t{dex}\n"
                                        for l, dex in lex ])) 
        
    def __create_variables (self, var):
        """ create variables
        This will populate the variable table
        """
        self.variables.delete(1.0, tk.END)  # Clear previous content
        self.variables.insert(tk.END, "".join([f"{name}\t{val}\n"
                                        for name, val  in  var.items()])) 
