# ⚡ LOLCODE Interpreter & IDE

A modern, dark-themed LOLCODE interpreter and IDE built with Python and CustomTkinter. This application parses and executes LOLCODE scripts while displaying live Lexemes and Variable/Symbol tables in a beautiful grid interface.

---

## ✨ Features

- **Dark Mode User Interface**: Styled using CustomTkinter with custom responsive layouts, buttons, and monospace syntax areas.
- **Interactive Terminal**: A built-in terminal console for program input (`GIMMEH`) and standard outputs (`VISIBLE`).
- **Real-time Analysis**: Displays a live lexeme table and global symbol/variable state changes upon execution.
- **Implicit Type Coercion**: Automatically coerces `YARN` (string) values to `NUMBR`/`NUMBAR` inside arithmetic contexts.
- **Optional keywords**: Allows cleaner function calling (optional `MKAY` termination) and typecasting (optional `A` keyword in `MAEK`).

---

## 🚀 Getting Started

### 📋 Prerequisites

Make sure you have **Python 3.10+** installed on your system.

### 📥 Installation

Install all required external dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

### Running the IDE (Graphical UI)

To launch the modern IDE interface where you can write, edit, open, and execute LOLCODE files:

```bash
python frontend/main.py
```

### Running the Interpreter (CLI/Console Mode)

To run a specific test script directly in the console (note that interactive `GIMMEH` input is mock-emulated in this mode):

```bash
python main.py
```

---

## 📁 Project Structure

- `frontend/main.py` - IDE window initialization and layout structure.
- `frontend/api.py` - Connects the frontend elements to the backend interpreter.
- `subunits/` - Modular components of the LOLCODE interpreter (parsing variables, functions, arithmetic, etc.).
- `testcases/` - Folder containing standard LOLCODE files (`.lol`) for testing.
