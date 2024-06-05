import subunits as s

class Functions():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def instantiation(self):
        # get variable name
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "function name", "there should be a valid function name")
        funcname = self.tab.capture_group[0]
        var = self.__get_variables(instantiation = True)
        row = self.tab.row
        self.tab.function[funcname] = [var, row] 
        self.pars.run_lines("^IF U SAY SO", skip = True)

    def calling (self):
        # get variable ka muna
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "function name", "there should be a valid function name")
        funcname = self.tab.capture_group[0]
        try:
            func = self.tab.function[funcname]
        except:
            # if the function does not exits
            self.tab.semantic_error(f"{funcname} does not exist")
        
        # if it exist 
        keys, row = func                 # deconsruct the function
        val = self.__get_variables()     # get variables 
        cur_row = self.tab.row           # get the current row to be saved

        if len(keys) != len(val):   # if the variables does not match
            self.tab.semantic_error("The number of parameters called is not equal to the number of parameters declared in the function") 
        
        self.tab.go_line(row)         # go the code block of the function
        # assign the function's variable to the global variable
        saved_var = self.tab.variables  
        
        self.tab.variables = dict(zip(keys, val))
        # palagyan ng IT = None
        self.tab.variables["IT"] = None

        print(self.tab.variables)
        has_return = False          # checker ng return
        
        self.tab.stack.append("func")
        # 'GTFO ?' baka hindi pumasok sa 'GTFO' condition mo sa baba
        self.pars.run_lines("^(FOUND YR |GTFO|IF U SAY SO)") # run until return or delimiter
        capture = self.tab.capture_group[0] # get results

        # if there is a return
        if capture == "FOUND YR ":
            saved_return = self.pars.get_lexemes(["expression","boolean","infinite", "concatination", "comparison","literal"])
            has_return = True
            self.pars.run_lines("IF U SAY SO", skip = True)
        elif capture == "GTFO":
            saved_return = None 
            has_return = True
            self.pars.run_lines("IF U SAY SO", skip = True)   
        elif capture == "IF U SAY SO" and not has_return:
            saved_return = None
        
        self.tab.go_line(cur_row+1)
        self.tab.stack.pop()
        #print(cur_row)
        self.tab.variables = saved_var
        self.tab.variables["IT"] = saved_return
        
    def __get_variables(self, instantiation = False):
        variable = []
        delimiter = "^YR "
        
        while True:
            if instantiation and self.pars.get_rid_new_line(error = False):
                break
            
            if not instantiation and not self.pars.get_rid(delimiter, "delimeter", match = True):
                self.pars.get_rid("^MKAY", "delimeter", "There must be an MKAY delimeter")
                break

            self.pars.get_rid(delimiter, "delimeter",f"There must be a delimeter '{delimiter}'")

            if instantiation:
                self.pars.get_rid("([a-zA-Z][a-zA-Z0-9_]*) ?", "variable", "There must be a variable")
                var = self.tab.capture_group[0]
                variable.append(var)
            else:
                variable.append(self.pars.get_lexemes(["expression","boolean","infinite", "concatination", "comparison", "literal"]))
       
            delimiter = "^AN YR "

        return variable
        