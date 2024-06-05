
class Switch():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.literal1 = 0

    def main(self):
        """
        LOLCODE Grammar:
        <switch> ::= WTF? <case> <default_case> OIC <linebreak>
        <case> ::= OMG <comparison> <linebreak> <statement> GTFO | <case> | <default_case>
        <default_case> ::= OMGWTF <linebreak> <statement> <linebreak> OIC <linebreak>
        """
        self.pars.get_rid_new_line()
        self.pars.get_rid_multiple_lines()
        self.pars.get_rid_spacing()
        self.pars.get_rid("^OMG ", "switch statement", "There should be a 'OMG' switch-statement")
        self.literal1 = self.pars.get_lexemes(["literal"])
        self.pars.get_rid_new_line()
        self.pars.get_rid_multiple_lines()
        
        delimiter = "^(OMG |OMGWTF|GTFO|OIC)"
        has_run = False
        checkCont = False
        captured_delm = "OMG"
        self.tab.stack.append("switch")

        
        while True:
            if ((self.tab.variables["IT"] == self.literal1 and not has_run) or
            (captured_delm == "OMGWTF" and not has_run) or checkCont):
                self.pars.run_lines(delimiter)
                has_run = True
            else: # skip 
                self.pars.run_lines(delimiter, skip=True)
                
            captured_delm = self.tab.capture_group[0] # capture delimiter
            if captured_delm == "OIC":
                self.tab.stack.pop()
                self.pars.get_rid_new_line()
                self.pars.get_rid_multiple_lines()
                break
            elif captured_delm == "GTFO":
                checkCont = False
                self.pars.get_rid_new_line()
                self.pars.get_rid_multiple_lines()
                self.pars.get_rid_spacing()
                self.pars.get_rid("^(OMG |OMGWTF)", "switch statement", "There should be a 'OMG' switch-statement")
                captured_delm = self.tab.capture_group[0]
                if captured_delm == "OMG ":
                    self.literal1 = self.pars.get_lexemes(["literal"])
                    self.pars.get_rid_new_line()
                    self.pars.get_rid_multiple_lines()
                    continue
                self.pars.get_rid_new_line()
                self.pars.get_rid_multiple_lines()
                continue
            elif captured_delm == "OMG ":
                checkCont = True
                self.literal1 = self.pars.get_lexemes(["literal"])
                self.pars.get_rid_new_line()
                self.pars.get_rid_multiple_lines()
                continue
            elif captured_delm == "OMGWTF":
                checkCont = True
                self.pars.get_rid_new_line()
                self.pars.get_rid_multiple_lines()
                delimiter = "^(OIC) ?"
                continue
        
    def skip(self):
        self.pars.run_lines("^OIC *", skip=True)

