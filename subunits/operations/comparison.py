import initial_vals

class Comparison():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars
        self.literal1 = None
        self.literal2 = None
        self.literal3 = None
        self.result = None

    def main(self):
        """
        LOLCODE Grammar:
        <comparison> ::= (BOTH SAEM | DIFFRINT) [<expression> | <number>] AN [<expression> | <number> | <compare_greater_or_less_than>]
        <compare_greater_or_less_than> ::= (BIGGR OF | SMALLR OF) [<expression> | <number>] AN [<expression> | <number>]

        Example:
        BOTH SAEM <x> AN <y> : <x> == <y>
        DIFFRINT <x> AN <y> : <x> != <y>

        Algorithm:
        1. Use checker variables for BOTH SAEM or DIFFRINT and BIGGR OF or SMALLR OF
        2. Get literals through get_lexemes function (expression or number)
        3. Get rid of AN delimiter
        4. Check if there is BIGGR OF or SMALLR OF
            4.1. If TRUE, get the second literal (store in literal2 variable)
            # REQUIRED: The first literal must be the same as the second literal
            4.2. Get rid of AN delimiter
            4.3. Get the third literal (store in literal3 variable)
            4.4. Call the checkRelOp function
            4.5. Store the result of the comparison to IT variable and return result
        5. If none, get the second literal (store in literal2 variable)
        6. Check if BOTH SAEM or DIFFRINT
            6.1. If BOTH SAEM, check if the two literals are the same
            6.2. If DIFFRINT, check if the two literals are not the same
            6.3. Store the result of the comparison to IT variable and return result
        """

        checker1 = self.tab.capture_group[0]
        self.literal1 = self.pars.get_lexemes(["expression", "compnumber"])
        self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")

        # Checks if the next lexeme has a "BIGGR OF" or "SMALLR OF" keyword
        if self.pars.get_rid("^(BIGGR OF|SMALLR OF) ", "delimiter"):
            checker2 = self.tab.capture_group[0]
            self.literal2 = self.pars.get_lexemes(["expression", "compnumber"])
            if self.literal1 != self.literal2:
                self.tab.semantic_error(f"The two values {self.literal1} and {self.literal2} should be the same")
            self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimiter")
            self.literal3 = self.pars.get_lexemes(["expression", "compnumber"])
            self.checkRelOp(checker1, checker2)
            self.checkType2(self.literal2, self.literal3)
            self.tab.variables["IT"] = self.result
            return self.result 
            
        self.literal2 = self.pars.get_lexemes(["expression", "compnumber"])
        if checker1 == "BOTH SAEM":
            self.result = self.literal1 == self.literal2
        elif checker1 == "DIFFRINT":
            self.result = self.literal1 != self.literal2
        self.checkType1(self.literal1, self.literal2) # Checks type of the two literals
        self.tab.variables["IT"] = self.result 
        return self.result 

    # For comparisons with relational operations (BIGGR OF or SMALLR OF)
    def checkRelOp(self, checker1, checker2):
        """
        LOLCODE Grammar:
        BOTH SAEM <x> AN BIGGR OF <x> AN <y> : <x> >= <y>
        BOTH SAEM <x> AN SMALLR OF <x> AN <y> : <x> <= <y>
        DIFFRINT <x> AN BIGGR OF <x> AN <y> : <x> < <y>
        DIFFRINT <x> AN SMALLR OF <x> AN <y> : <x> > <y>
        """
        if checker1 == "BOTH SAEM" and checker2 == "BIGGR OF":
            self.result = self.literal2 >= self.literal3
        elif checker1 == "BOTH SAEM" and checker2 == "SMALLR OF":
            self.result = self.literal2 <= self.literal3
        elif checker1 == "DIFFRINT" and checker2 == "BIGGR OF":
            self.result = self.literal2 < self.literal3
        elif checker1 == "DIFFRINT" and checker2 == "SMALLR OF":
            self.result = self.literal2 > self.literal3

    def checkType1(self, literal1, literal2):
        if type(literal1).__qualname__ != type(literal2).__qualname__:
            self.result = False
    
    def checkType2(self, literal2, literal3):
        if type(literal2).__qualname__ != type(literal3).__qualname__:
            self.result = False
