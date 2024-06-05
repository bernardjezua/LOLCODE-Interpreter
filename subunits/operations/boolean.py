import initial_vals

class Boolean_Temp():
    def __init__(self, tab, pars) -> None:
        # Initialization for the class
        self.tab = tab
        self.pars = pars
        self.literal1 = None
        self.literal2 = None
        self.result = None

    def logic_op(self):
        """
        LOLCODE Grammar:
        <logic_op> ::= (BOTH OF | EITHER OF | WON OF) <literal> AN <literal>

        EXAMPLE:
        BOTH OF <x> AN <y> : <x> and <y>
        EITHER OF <x> AN <y> : <x> or <y>
        WON OF <x> AN <y> : (<x> or <y>) and not (<x> and <y>)

        Algorithm:
        1. Get the first literal (store in literal1 variable)
        2. Get rid of AN delimiter
        3. Get the second literal (store in literal2 variable)
        4. Call the logic_op function
        5. Store the result of the comparison to IT variable and return result

        """
        self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
        self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
        self.literal2 = self.pars.get_lexemes(["boolean", "literal"])

    def both_of(self):
        # <both_of> ::= BOTH OF <literal> AN <literal>
        self.logic_op()
        self.result = bool(self.literal1 and self.literal2)
        self.tab.variables["IT"] = self.result
        return self.result

    def either_of(self):
        # <either_of> ::= EITHER OF <literal> AN <literal>
        self.logic_op()
        self.result = bool(self.literal1 or self.literal2)
        self.tab.variables["IT"] = self.result
        return self.result

    def won_of(self):
        # <won_of> ::= WON OF <literal> AN <literal>
        self.logic_op()
        self.result = bool((self.literal1 or self.literal2) and not (self.literal1 and self.literal2))
        self.tab.variables["IT"] = self.result
        return self.result

    def not_operation(self):
        """
        LOLCODE Grammar:
        <not_operation> ::= NOT <literal>
        """
        # <not_operation> ::= NOT <literal>
        self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
        self.result = bool(not self.literal1)
        self.tab.variables["IT"] = self.result
        return self.result

    def all_of(self):
        """
        LOLCODE Grammar:
        <all_of> ::= ALL OF <literal> AN <literal> <loop> | MKAY
        <loop> ::= AN <literal> <loop> | MKAY
        """
        self.logic_op()
        self.result = bool(self.literal1 and self.literal2)

        while True:
            if not self.pars.get_rid("^AN ", "delimiter", match=True):
                self.pars.get_rid("^MKAY ?", "delimiter", "There should be an 'MKAY' delimiter")
                break
            self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
            self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
            self.result = bool(self.result and self.literal1)
        
        self.tab.variables["IT"] = self.result
        return self.result


    def any_of(self):
        """
        LOLCODE Grammar:
        <any_of> ::= ANY OF <literal> AN <literal> <loop> | MKAY
        <loop> ::= AN <literal> <loop> | MKAY
        """
        self.logic_op()
        self.result = bool(self.literal1 or self.literal2)

        while True:
            if not self.pars.get_rid("^AN ", "delimiter", match=True):
                self.pars.get_rid("^MKAY ?", "delimiter", "There should be an 'MKAY' delimiter")
                break
            self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
            self.literal1 = self.pars.get_lexemes(["boolean", "literal"])
            self.result = bool(self.result or self.literal1)

        self.tab.variables["IT"] = self.result
        return self.result

class Boolean():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def both_of(self):
        return Boolean_Temp(self.tab, self.pars).both_of()
    def either_of(self):
        return Boolean_Temp(self.tab, self.pars).either_of()
    def won_of(self):
        return Boolean_Temp(self.tab, self.pars).won_of()
    def not_operation(self):
        return Boolean_Temp(self.tab, self.pars).not_operation()
    def all_of(self):
        return Boolean_Temp(self.tab, self.pars).all_of()
    def any_of(self):
        return Boolean_Temp(self.tab, self.pars).any_of()
