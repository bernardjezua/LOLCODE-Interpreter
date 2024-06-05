import subunits as s
import re

class Parser_Function():

    def __init__(self, tab) -> None:
        self.tab = tab
        
    # add here if you have an 'or' in your grammar
        """
        Naming convention for the context-free grammar
        self.cfg = {
            'abstractions' : {
                'regex1' : function1
                'regex2' : function2
            }
        }
        """
        self.cfg = {
            "number":{
                "^-?[0-9]+(\.[0-9]+) ?": s.Data_Type(self.tab).numbar,
                "^-?[0-9]+ ?": s.Data_Type(self.tab).numbr,
                "^\"(-?[0-9]+(\.[0-9]+)?)\" ?" : s.Typecasting(self.tab, self).str_to_num,
                "^(WIN|FAIL) ?": s.Data_Type(self.tab).troof,
                "^([a-zA-Z][a-zA-Z0-9_]*) ?": s.Variable(self.tab, self).num_var,
            },  
            "expression":{
                '^SUM OF ' : s.Arithmetic(self.tab, self).add, 
                '^DIFF OF ': s.Arithmetic(self.tab, self).minus,
                '^PRODUKT OF ': s.Arithmetic(self.tab, self).mul, 
                '^QUOSHUNT OF ': s.Arithmetic(self.tab, self).div, 
                '^MOD OF ': s.Arithmetic(self.tab, self).mod,
                '^BIGGR OF ': s.Arithmetic(self.tab, self).biggr,
                '^SMALLR OF ': s.Arithmetic(self.tab, self).smallr,
            },
            "literal":{
                "^-?[0-9]+\.[0-9]+ ?": s.Data_Type(self.tab).numbar,
                "^-?[0-9]+ ?": s.Data_Type(self.tab).numbr,
                "^\"([-+\w\s.\[\]:()<>,\*!'?=/%]*)\" ?": s.Data_Type(self.tab).yarn, 
                "^(WIN|FAIL) ?": s.Data_Type(self.tab).troof,
                "^([a-zA-Z][a-zA-Z0-9_]*) ?": s.Variable(self.tab, self).get_var,
            },
            "statement":{
                "^GIMMEH ": s.Input(self.tab, self).main,
                "^VISIBLE ": s.Output(self.tab, self).main,
                "^IM IN YR ": s.Loops(self.tab,self).main,
                "^I IZ ": s.Functions(self.tab,self).calling,
                "^MAEK " : s.Typecasting(self.tab,self).main,
                "^O RLY\?" : s.IfElse(self.tab,self).main,
                "^WTF\?": s.Switch(self.tab,self).main,
                "^SMOOSH ": s.Output(self.tab, self).concatination,
                "^([a-zA-Z][a-zA-Z0-9_]*) R ": s.Assignment(self.tab,self).assign,
                "^([a-zA-Z][a-zA-Z0-9_]*) IS NOW A ": s.Assignment(self.tab,self).recasting,
                "^(BOTH SAEM|DIFFRINT) ": s.Comparison(self.tab, self).main,
                "^([a-zA-Z][a-zA-Z0-9_]*) ?": s.Variable(self.tab, self).put_IT
            },
            "function":{
                "^HOW IZ I ": s.Functions(self.tab,self).instantiation,
            },
            "skip":{
                "^O RLY\?" : s.IfElse(self.tab,self).skip,
                "^WTF\?": s.Switch(self.tab,self).skip,
                "^IM IN YR " : s.Loops(self.tab,self).skip,
            },
            "boolean": {
                "^BOTH OF ": s.Boolean(self.tab, self).both_of,
                "^EITHER OF ": s.Boolean(self.tab, self).either_of,
                "^WON OF ": s.Boolean(self.tab, self).won_of,
                "^NOT ": s.Boolean(self.tab, self).not_operation,
            },
            "infinite": {
                "^ALL OF ": s.Boolean(self.tab, self).all_of,
                "^ANY OF ": s.Boolean(self.tab, self).any_of,
            },
            "comparison": {
                "^(BOTH SAEM|DIFFRINT) ": s.Comparison(self.tab, self).main,
            },
            "compnumber": {
                "^-?[0-9]+\.[0-9]+ ?": s.Data_Type(self.tab).numbar,
                "^-?[0-9]+ ?": s.Data_Type(self.tab).numbr,
                "^\"([-+\w\s.\[\]:()<>,\*!'?=/%]*)\" ?": s.Data_Type(self.tab).yarn,
                "^(WIN|FAIL) ?": s.Data_Type(self.tab).troof,
                "^([a-zA-Z][a-zA-Z0-9_]*) ?": s.Variable(self.tab, self).num_var,
            },
            "concatination":{
                 "^SMOOSH ": s.Output(self.tab, self).concatination,
            },
            "terminate": {
                "^KTHXBYE ?" :self.tab.exit_program, 
            }
        }

    def get_lexemes(self, cfg,  error=True, match=False) :
        """Get lexemes

        This is where you implement the 'or' in your cfg. It loops over the
        regex of the 'abstractions' in self.cfg, will also run if one matches.
        Also already has error handler

        Args: 
            cfg (list[str]): List of string which abstractions inculded in the list
            error(optional| True) - 
                    if the lexeme is optional toggle False
                    if strict, non need to put True

        Returns: 
            return (Any| None): what ever the function in being executed

        Examples:
            // will return the resulting value from the function and assigning it

            self.val1 = self.pars.get_lexemes(["expression", "number"])

            // printing the resulting value from the expression function

            print(pars.get_lexemes(["expression"]))
        """

        self.__line_contn()
        for abtraction in cfg:
            for reg in self.cfg[abtraction]:
                if  self.__get_data(reg, abtraction, match=match):
                    return self.cfg[abtraction][reg]()
        else:
            if not error: 
                return None
            
            error_des = f"""
                No {' '.join([f'<{abs}>' for abs in cfg])} matched."""
            
            self.syntax_error(error_des)
                
    def __get_data(self, reg, description, match = False):
        """Get data
        search if there is a match. If there is a match: 
            add the column (currently being analyzed for error handler);
            puts the captured string in the table of values;
            removed the captured string in the line

        Args:
            reg (str): the keyword being removed using regex 
            description (str): used to described the lexeme got

        Returns:
            res (regex class| None):  returns if there is mathc or none
        
        """
        res = re.search(reg, self.tab.line)

        if match:
            return res
    
        if res:
            # print(self.tab.line) # comment if you dont like it
            self.tab.capture_group = res.groups()
            self.tab.column += res.span()[1]
            self.tab.capture = res.group()
            self.tab.line = self.tab.line[res.span()[1]:]

            if description in ["newline", "comment"]:
                self.tab.lexemes.append((self.tab.capture.strip()+"\\n", description))
                return res 

            if  description not in ["spacing"]:
                self.tab.lexemes.append((self.tab.capture, description))

        return res   

    def __line_contn(self):
        if self.__get_data("^[ \t]*\.\.\. ?", "line continuation"):
            self.get_rid_new_line()
            self.get_rid_spacing()

    
    def get_rid (self, reg, lex_description, error_description = False, match = False):
        """Get rid
        For context-free grammar with a certain keyword such as 'AN'
        or 'ITZ', 'get_rid' get rid of this keywords. If the keyword is 
        not seen error will be shown

        Args:
            reg (str): the keyword being removed using regex 
            lex_description (str): used to described the lexeme got
            error_description (str| False): if error ==false non need to put anything
                        syntaxt erro description

        Returns:
            res (regex class| None):  returns if there is mathc or none

        Examples: 
            self.pars.get_rid("^AN ")
        """
        
        self.__line_contn()
        res = self.__get_data(reg, lex_description, match=match)
    
        if not res and error_description:
            self.syntax_error(error_description)

        return res


    def get_rid_spacing(self):
        """Get rid of the spacing 
        The spacing is included in the regex
        " " and "\t"
        """
        if self.__get_data("^[ \t]*", "spacing"):
            return True
        
        return False

    
    def get_rid_new_line(self, error = True, match = False):
        """Get rid new line
        
        This is a strict new line checker. It will also detect if there is a comment
        if there is a comment or \n, automatically go to next line.
        else error

        Args:
            error(optional| True) - toggle true if error is needed that there is no new line
                    if the newline is optional toggle true
                    if strick, non need to put True
        Return: (bool) : True if new line is executed, False if there is no newline of comment
        
        """
        
        # print(self.get_lexemes(["m_comment"], error=False))
        if self.__get_data("^[ \t]*OBTW", "comment", match=match):
            if match:
                return True
            else:
                s.Multiline_Comment(self.tab, self).main()
                return True
        
        if self.__get_data("^[ \t]*, ?", "soft newline", match=match):
            return True
        
        if self.__get_data("^[ \t]*BTW .*", "comment", match=match) or self.__get_data("^[ \t]*\n", "newline", match=match):
            if match:
                return True
            else:
                self.tab.new_line()
                return True
        
        if error:
            self.syntax_error("There should be a new line here")

        return False
    
    def get_rid_multiple_lines(self):
        """Get rid multiple lines
        Get rids of all newline and comments  
        """

        while True:
            if not self.get_rid_new_line(error=False):
                break
        return
    
    def run_lines(self, delimiter, skip = False):
        """run lines
        function that will run multi lines of "boolean","infinite", "expression", "statement".
        you can also skip it if you toggle skip

        Params
            delimiter (str): regex for the delimeter 
            skip (bool = False): toggle true if you want to skip the multi lines 
        """

        while True:
            self.get_rid_multiple_lines()
            self.get_rid_spacing()

            if not skip and self.return_checker() :
                return

            if self.get_rid(delimiter, "delimeter"):
                return

            if skip:
                self.get_lexemes(["skip"], error=False) or self.tab.new_line()
            else:
                self.get_lexemes(["boolean","infinite", "expression", "statement"])

    def return_checker (self):

        # special case for switch
        if self.get_rid("^(GTFO)", "return", match=True) and self.tab.stack[-1] == "switch":
            return False

        # returning if
        if self.get_rid("^(FOUND YR |GTFO|IF U SAY SO)", "return", match=True):

            if "func" not in self.tab.stack:
                self.tab.semantic_error("You cannot return if there is no function")
            
            # if it is not the function yet in the stack
            if self.tab.stack[-1] != "func":
                return True
    
        return False


    def syntax_error (self, error_description = None):

        self.tab.terminal += f"""
    SYNTAX ERROR !!
    There is an error in line {self.tab.row+1}:{self.tab.column}

    File
    .\{self.tab.file} {self.tab.row+1}:{self.tab.column}
    \t{self.tab.row+1}. | {self.tab.code[self.tab.row][:-1]}
    \t{' '*len(str(self.tab.row+1))}{' '*(self.tab.column+4)}^
"""
        if error_description: 
            self.tab.terminal += f"""
        Description:
            {error_description}
            """

        raise SyntaxError()
