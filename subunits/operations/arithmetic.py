import initial_vals

class Arithmetic_Temp():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        # Use main function for the context-free grammar
        # <expression> | <number> AN <expression> | <number> 
        self.val1 = self.pars.get_lexemes(["expression", "number"])
        self.pars.get_rid("^AN ", "delimiter", "There should be 'AN' delimeter")
        self.val2 = self.pars.get_lexemes(["expression", "number"])
        

    def add(self):
        self.main()
        self.tab.variables["IT"] = self.val1 + self.val2 
        return self.val1 + self.val2
    
    def minus(self):
        self.main()
        self.tab.variables["IT"] = self.val1 - self.val2
        return self.val1 - self.val2
    
    def mul(self):
        self.main()
        self.tab.variables["IT"] = self.val1 * self.val2
        return self.val1 * self.val2
    
    def div(self):
        self.main()
        self.tab.variables["IT"] = self.val1 / self.val2 
        return self.val1 / self.val2
    
    def mod (self):
        self.main()
        self.tab.variables["IT"] = self.val1 % self.val2
        return self.val1 % self.val2
    
    def biggr(self):
        self.main()
        self.tab.variables["IT"] = max(self.val1, self.val2)
        return max(self.val1, self.val2)
    
    def smallr(self):
        self.main()
        self.tab.variables["IT"] = min(self.val1, self.val2)
        return min(self.val1, self.val2 )
    
class Arithmetic():
    def __init__(self, tab, pars) -> None:
        self.tab = tab
        self.pars = pars

    def add(self):
        return Arithmetic_Temp(self.tab, self.pars).add()
    def minus(self):
        return Arithmetic_Temp(self.tab, self.pars).minus()
    def mul(self):
        return Arithmetic_Temp(self.tab, self.pars).mul()
    def div(self):
        return Arithmetic_Temp(self.tab, self.pars).div()
    def mod(self):
        return Arithmetic_Temp(self.tab, self.pars).mod()
    def biggr(self):
        return Arithmetic_Temp(self.tab, self.pars).biggr()
    def smallr(self):
        return Arithmetic_Temp(self.tab, self.pars).smallr()
    
# TODO: BIGGR OF x AN BIGGR OF y AN 5