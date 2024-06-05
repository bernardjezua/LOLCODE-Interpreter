
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))



# here you can call you functions 
from initial_vals import *
from subunits import *

def interpreter(code, tab):

    pars = Parser_Function(tab)


    try: 
        tab.code = code

        tab.row = 0
        tab.line = tab.code[tab.row] 

        pars.get_rid_multiple_lines()
        pars.get_rid("^HAI ?", "code initialized", "No lolcode initailization, Add the keyword 'HAI'")
        pars.get_rid_new_line()

        while True:
            pars.get_rid_multiple_lines()
            pars.get_rid_spacing()

            if not pars.get_rid("^HOW IZ I ", "function", match=True):
                break

            pars.get_lexemes(["function"])
        
        pars.get_rid("^WAZZUP ?", "variables initailization","Variables sould be initialized using 'WAZZUP'" )
        Variable(tab, pars).main()
        pars.get_rid_multiple_lines()

        while True:
            pars.get_rid_multiple_lines()
            pars.get_rid_spacing()

            if pars.get_lexemes(["terminate"], False):
                break

            pars.get_lexemes(["expression","boolean","infinite","statement"])

    except SyntaxError:
       
        return tab
