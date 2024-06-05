import subunits as s

class Loops():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):

        # walang carat regex
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")
        label = self.tab.capture_group[0]

        self.pars.get_rid("^(UPPIN|NERFIN) ?", "label", "there should be a valid label")
        operation = self.tab.capture_group[0]

        self.pars.get_rid("^YR ?", "delimeter", "there should be a YR delimeter")
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")
        var_name = self.tab.capture_group[0]
        value = s.Variable(self.tab, self.pars).get_var()        

        self.pars.get_rid("^(TIL|WILE) ?", "condition")
        loop_cond = self.tab.capture_group[0]
        saved_row = self.tab.row # isasave yung row na babalikan
        self.tab.stack.append("loop")

        while True:
            value = self.pars.get_lexemes(["comparison"])
            # pacheck if tama yung pagswitch ng value
            if "TIL" == loop_cond: 
                value = not value

            if not value:# if hindi tama yung condition, skip
                self.pars.run_lines("^IM OUTTA YR ",  skip=True)
                break
        
            # if tama yung condition
            self.pars.run_lines("^IM OUTTA YR ")
            self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")

            if self.tab.capture_group[0]!= label:
                self.tab.semantic_error(f"{self.tab.capture_group[0]} is not the same with defined label {label}")
            self.tab.go_line(saved_row) # going back to the loop

            self.pars.get_rid("^.*(TIL|WILE) ","loop") # kukunin hangang til or wile

            if operation == "UPPIN":
                self.tab.variables[var_name] += 1
            elif operation == "NERFIN":
                self.tab.variables[var_name] -= 1

        self.tab.stack.pop()
        self.pars.get_rid("([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")
        self.pars.get_rid_new_line()


    def skip(self):
        self.pars.run_lines("^IM OUTTA YR ", skip=True)
        self.pars.get_rid("^([a-zA-Z][a-zA-Z0-9_]*) ?", "label", "there should be a valid label")

