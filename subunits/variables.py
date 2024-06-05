

class Variable():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        # <init_variables> ::= WAZZUP <linebreak> <undec_variable>
        # <undec_variable> ::= (BUHBYE | I HAS A <variable> (<linebreak> | <dec_variable>))
        # <dec_variable> ::= ITZ (<expression> | <literal> | <variable>) <linebreak> <undec_variable>
        self.pars.get_rid_new_line()

        while True:
            self.pars.get_rid_multiple_lines()
            self.pars.get_rid_spacing()

            if self.pars.get_rid("^BUHBYE ?","end variables"):
                self.pars.get_rid_new_line()
                return

            # I HAS A <variable>
            self.pars.get_rid("^I HAS A ", "variable declaration", "I HAS A is the keyword for initializing the variable")
            self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "variable", "There should be a variable")
            var_name = self.tab.capture_group[0]

            # if uninitialized variable set to None, nexline
            if not self.pars.get_rid("^ITZ ","variable assignment"):
                self.tab.variables[var_name] = None
                self.pars.get_rid_new_line()
                continue
            
            # if initialize, can pick between "expression", "literal", "variable" (variable here is inside literal)
            self.tab.variables[var_name] = self.pars.get_lexemes(["boolean","infinite", "expression","concatination", "comparison" ,"literal"])
            self.pars.get_rid_new_line()


    def get_var(self):
        # gets the variable and looking for it in the table of variable
        var_name = self.tab.capture_group[0]
        get_var = True if var_name in self.tab.variables.keys() else False

        if get_var:
            return self.tab.variables[var_name]
        
        self.tab.semantic_error(f"Variable '{var_name}' not initialized")

    def put_IT(self):
        self.tab.variables["IT"] = self.get_var()

    def num_var(self):
        var_name = self.tab.capture_group[0]
        val = self.get_var()

        if type(val).__qualname__ == 'str' :
            self.tab.semantic_error(f"The variable {var_name} is a YARN")
        
        return val

