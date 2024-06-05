
class Output():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars
        

    def main(self):
        self.__concat("^\+ ")
        self.tab.terminal += self.concat

    def concatination(self):
        con = self.__concat()
        self.tab.variables["IT"] = con
        return con

    def __concat(self, delimiter= "^AN "):

        # <output> ::= VISIBLE <literal> <concat>
        # <concat> ::= <linebreak> | + <literal> <concat> 
        self.concat = ""
        while True:
            self.concat += str(self.pars.get_lexemes(["boolean","concatination", "infinite","expression", "comparison", "literal"]))

            if self.pars.get_rid("^! ?","delimeter"): # if there is newline supression 
                self.pars.get_rid_new_line()
                break
            if (self.pars.get_rid_new_line(error= False, match=True) or
                (self.pars.get_rid("^\+ ","delimiter", match=True) and delimiter == "^AN ")): # if there is new line
                if delimiter == "^\+ ":
                    self.concat+= "\n"
                break

            # if there still given 
            self.pars.get_rid(delimiter,"delimeter", f"there should be a '{delimiter}' delimiter")

        return self.concat
    




            
        



 
