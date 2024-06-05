
class IfElse():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        """
        LOLCODE Grammar:
        <if_else> ::= <comparison> <linebreak> O RLY? <linebreak> <if_clause>
        <if_clause> ::= YA RLY <linebreak> <statement> (<else_if_clause> | <else_clause> | OIC <linebreak>)
        <else_if_clause> ::= MEBBE <comparison> <linebreak> <statement> (<else_clause | OIC <linebreak>)
        <else_clause> ::= NO WAI <linebreak> <statement> OIC <linebreak>
        """
        self.pars.get_rid_new_line()
        self.pars.get_rid_multiple_lines()
        self.pars.get_rid_spacing()
        self.pars.get_rid("^YA RLY", "if statement", "There should be a 'YA RLY' if-statement")
        self.pars.get_rid_new_line()
        self.pars.get_rid_multiple_lines()
        
        delimiter = "^(NO WAI|MEBBE|OIC) ?"

        self.tab.stack.append("ifelse")
        has_run = False
        captured_delm = "YA RLY"
        while True:
            if ((self.tab.variables["IT"] and not has_run) or (captured_delm == "NO WAI" and not has_run)): # YA RLY and MEBBE, and NO WAI
                self.pars.run_lines(delimiter)
                has_run = True
            else: # skip
                self.pars.run_lines(delimiter, skip=True)

            if self.pars.return_checker():
                self.tab.stack.pop()
                return
            
            captured_delm = self.tab.capture_group[0] # capture delimiter
            
            if captured_delm == "OIC": 
                self.pars.get_rid_new_line()
                self.tab.stack.pop()
                self.pars.get_rid_multiple_lines()
                break 
            elif captured_delm == "NO WAI":
                self.pars.get_rid_new_line()
                self.pars.get_rid_multiple_lines()
                delimiter = "^(OIC) ?"
                continue
            else: # MEBBE
                self.pars.get_lexemes(["comparison"])
                continue

    def skip(self):
        self.pars.run_lines("^OIC *", skip=True)
