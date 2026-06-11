import tkinter as tk
import customtkinter as ctk
from api import Api

# Set customtkinter appearance and theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("1400x850")
root.title("LOLCODE Interpreter")

# Title/Header Frame
header_frame = ctk.CTkFrame(root, height=60, corner_radius=8)
header_frame.pack(fill=tk.X, padx=15, pady=(15, 5))

title_label = ctk.CTkLabel(
    header_frame, 
    text="LOLCODE Interpreter", 
    font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold")
)
title_label.pack(side=tk.LEFT, padx=20, pady=10)

# Buttons on the header
file_button = ctk.CTkButton(
    header_frame, 
    text="📂 Open File", 
    command=None,  # Will configure below
    font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
    fg_color="#3a3a3a",
    hover_color="#505050"
)
file_button.pack(side=tk.RIGHT, padx=10, pady=10)

ex = ctk.CTkButton(
    header_frame, 
    text="▶ Execute", 
    command=None,  # Will configure below
    font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
    fg_color="#1f6aa5",
    hover_color="#144870"
)
ex.pack(side=tk.RIGHT, padx=10, pady=10)

# Main Grid Frame
grid_frame = ctk.CTkFrame(root, fg_color="transparent")
grid_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

grid_frame.columnconfigure(0, weight=3)
grid_frame.columnconfigure(1, weight=2)
grid_frame.columnconfigure(2, weight=1)
grid_frame.rowconfigure(0, weight=1)

# Columns inside grid
# Editor Column
editor_container = ctk.CTkFrame(grid_frame)
editor_container.grid(row=0, column=0, padx=(0, 10), pady=0, sticky="nsew")

editor_label = ctk.CTkLabel(editor_container, text="LOLCODE Editor", font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"))
editor_label.pack(anchor="w", padx=15, pady=(10, 5))

editor = ctk.CTkTextbox(
    editor_container, 
    font=ctk.CTkFont(family="Consolas", size=13),
    fg_color="#1e1e1e",
    text_color="#ffffff",
    border_width=1,
    border_color="#333333"
)
editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# Lexemes Column
lexemes_container = ctk.CTkFrame(grid_frame)
lexemes_container.grid(row=0, column=1, padx=10, pady=0, sticky="nsew")

lexemes_label = ctk.CTkLabel(lexemes_container, text="Lexeme Table", font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"))
lexemes_label.pack(anchor="w", padx=15, pady=(10, 5))

lexemes = ctk.CTkTextbox(
    lexemes_container, 
    font=ctk.CTkFont(family="Consolas", size=13),
    fg_color="#1e1e1e",
    text_color="#a9b1d6",
    border_width=1,
    border_color="#333333"
)
lexemes.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# Variables Column
variables_container = ctk.CTkFrame(grid_frame)
variables_container.grid(row=0, column=2, padx=(10, 0), pady=0, sticky="nsew")

variables_label = ctk.CTkLabel(variables_container, text="Symbol Table", font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"))
variables_label.pack(anchor="w", padx=15, pady=(10, 5))

variables = ctk.CTkTextbox(
    variables_container, 
    font=ctk.CTkFont(family="Consolas", size=13),
    fg_color="#1e1e1e",
    text_color="#e0af68",
    border_width=1,
    border_color="#333333"
)
variables.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# Terminal Frame (at bottom)
terminal_frame = ctk.CTkFrame(root, height=250)
terminal_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

terminal_label = ctk.CTkLabel(terminal_frame, text="Terminal Output", font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"))
terminal_label.pack(anchor="w", padx=15, pady=(10, 5))

terminal = ctk.CTkTextbox(
    terminal_frame, 
    height=180,
    font=ctk.CTkFont(family="Consolas", size=13),
    fg_color="#0f0f0f",
    text_color="#00ffcc",
    border_width=1,
    border_color="#333333"
)
terminal.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

# API integration
api = Api(root, editor, terminal, lexemes, variables)

# Link commands of buttons to API methods
file_button.configure(command=api.open_file_dialog)
ex.configure(command=api.execute)

terminal.bind("<Return>", api.on_enter_pressed)

root.mainloop()





