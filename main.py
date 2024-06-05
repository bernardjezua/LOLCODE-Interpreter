

# here you can call you functions 
from initial_vals import *
from subunits import *
import traceback

tab = Tables_Values(root=True)
pars = Parser_Function(tab)

file = r'testcases\final\05_bool.lol'
f = open( file,  'r')

tab.file = file
tab.code = f.readlines()

tab.row = 0
tab.line = tab.code[tab.row]


"""
Instructions in getting the classes up and running

1. Build your class in .\subunits folder
2. make sure that import your class in .\subunits\__init__.py
3. add the abtractions and regex in .\init_vals\parser_function.py 
    in self.cfg variablew


"""
try: 
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
    print("\n")
    print(tab.function)
    print(" -------TERMINAL----")
    # change your printing here
    print(tab.terminal)
    

except Exception as error:
    print("\n")
    print(error)
    traceback.print_exc()





    
