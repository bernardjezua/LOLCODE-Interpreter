import initial_vals
import subunits as s


class Assignment():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.var = " "
        
    def main(self):
        print(f""" 
            capture: {self.tab.capture}
            capture group: {self.tab.capture_group}
            line: {self.tab.line}
            row: {self.tab.row}
        """)

    def assign(self):
        var_name = self.tab.capture_group[0]
        value = s.Variable(self.tab, self.pars).get_var()        
        
        if(self.pars.get_rid("^MAEK ?", "typecasting")):
            new_val = s.Typecasting(self.tab, self.pars).main()
        else:
            new_val = self.pars.get_lexemes(["expression","boolean","infinite", "concatination", "literal"]) # huli yung literal, walang variable
            
        self.tab.variables[var_name] = new_val

            
    def recasting(self):
        var = self.tab.capture_group[0]
        value = s.Variable(self.tab, self.pars).get_var()
        new_val = s.Typecasting(self.tab, self.pars).typecast(value)
        
        if value == None: 
            if(type(new_val) == bool):
                self.tab.variables[var] = new_val
                print("Successfully typecasted!")
            else:
                self.tab.semantic_error("Cannot assign NOOB to data type other than TROOF!")
        else:
            self.tab.variables[var] = new_val
            print("Successfully typecasted!")



