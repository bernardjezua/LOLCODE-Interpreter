import tkinter as tk

class Tables_Values:
    def __init__(self, root) -> None:

        self.capture = " "
        """Data type (str)
        This is where the lexemes are stored. 
        Note that it overwrites itself everytime it 
        encounters a lexeme
        """

        self.capture_group = " " 
        """Tuple[str]
        Tuple of captured in the regex
        """

        self.code = []
        """
        List if the code
        """

        self.line = " "
        """
            current line is assigned here
            this is the line we get the lexemes
        """

        self.variables = {'IT': None}
        """
        variables = {
            "var1": value
            "var2": value
        }
        
        """

        self.function = {}
        """
        function = {
            "func1": row number,
            "func2": [code ..],
        }
        
        """

        self.terminal = ""
        """
        This is where 
        
        """
        self.lexemes = []
        """
        lexemes = [
            ("lex" , "description"),
            ("lex" , "description"),
        ]
        """

        self.stack = []

        self.root_front = root # the root off the frontend
        self.buffer = " " # the value of the input
        self.show_data = "" # showing the data in the fronend if input is needed

        #  for error handling 
        self.file = " "
        self.row = 0        # current line index
        self.column =0      # current column

    def new_line(self):
        self.row+=1
        self.line = self.code[self.row]
        self.column =0

    def go_line(self, line):
        self.row = line
        self.line = self.code[self.row]
        self.column =0
    
    def semantic_error(self, description):
        line = self.code[self.row].strip('\n')
        self.terminal += f"""
    SEMANTIC ERROR !!
    There is an error in line {self.row+1}:{self.column}

    File:
    .\{self.file} {self.row+1}:{self.column}
    \t{self.row+1}. | {line}
    \t{' '*len(str(self.row+1))}{' '*(self.column+4 )}^
    
    Description:
        {description}
    """

        raise SyntaxError()

    def exit_program(self):

        raise SyntaxError()

