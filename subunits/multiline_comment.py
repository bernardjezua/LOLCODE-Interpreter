import subunits as s

class Multiline_Comment():

    def __init__(self, tab , pars) -> None:
        self.tab = tab
        self.pars = pars

    def main(self):
        """
        <multi-line comment> := OBTW <loop>
        
        """

        while True :
            if self.pars.get_rid("^ *TLDR", "multiline delimeter"):
                self.pars.get_rid("^ *\n", "newline", "There should be a new line after 'TLDR'")
                self.tab.new_line()

                break

            self.tab.new_line()

        return True