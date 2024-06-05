from tkinter import *
from api import Api

root = Tk()
root.geometry("1500x800")

root.title("Lolcode Interpreter")


top_frame = Frame(root)
top_frame.pack(side = TOP, padx=10, pady=10)

""" Textboxs"""
editor = Text(top_frame, height=20, width=80)
editor.grid(row=0, column=0, padx=20, pady=10)

lexemes = Text(top_frame, height=20, width=50)
lexemes.grid(row=0, column=1, padx=20, pady=10)

variables = Text(top_frame, height=20, width=20)
variables.grid(row=0, column=2, padx=20, pady=10)

terminal = Text(root, height=20, width=70)
terminal.pack(side=BOTTOM, padx=20, pady=10)


""" Function calls """
api = Api(root, editor,terminal,  lexemes, variables )

terminal.bind("<Return>", api.on_enter_pressed)


ex = Button(root, text="Execute", command=api.execute)
ex.pack( padx=20, pady=10)

file_button = Button(root, text="Open File", command=api.open_file_dialog)
file_button.pack( padx=20, pady=10)



root.mainloop()




