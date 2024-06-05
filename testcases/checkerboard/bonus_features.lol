HAI

    HOW IZ I is_even YR i AN YR j
        FOUND YR BOTH SAEM MOD OF SUM OF i AN j AN 2 AN 0
    IF U SAY SO

    OBTW
        demonstrates the use of nested loops with if else statements 
        inside and also supress newline by printing a checker-board like pattern
    TLDR
    
    HOW IZ I checker_board YR x AN YR y AN YR z AN YR a
        VISIBLE "*"
        VISIBLE "INPUT DIMENSIONS FOR ROW: "
        GIMMEH x
        x IS NOW A NUMBR
        VISIBLE "INPUT DIMENSIONS FOR COLUMN: "
        GIMMEH y
        y IS NOW A NUMBR
        IM IN YR asc UPPIN YR z TIL BOTH SAEM x AN z
		    IM IN YR asc1 UPPIN YR a TIL BOTH SAEM y AN a
                I IZ is_even YR a AN YR z MKAY
                O RLY?
                    YA RLY
                       VISIBLE "[X]" !
                    NO WAI
                        VISIBLE "[ ]" !
	            OIC
	        IM OUTTA YR asc1
            VISIBLE ""
            a R 0
	    IM OUTTA YR asc
    IF U SAY SO
    
    
    HOW IZ I nested_if_else YR age
        BOTH SAEM age AN BIGGR OF age AN 18
        O RLY?
            YA RLY
                VISIBLE "You are an adult." 
                BOTH SAEM age AN BIGGR OF age AN 21
                O RLY?
                    YA RLY
                        VISIBLE "You are eligible to vote."
                    NO WAI
                        VISIBLE "You are not eligible to vote yet."
                OIC
            NO WAI
                VISIBLE "You are a minor."
                BOTH SAEM age AN BIGGR OF age AN 16
                O RLY?
                    YA RLY
                        VISIBLE "You are eligible for a driver's license with parental consent."
                    NO WAI
                        VISIBLE "You are not eligible for a driver's license yet."
                OIC
	    OIC
    IF U SAY SO

    HOW IZ I switch_nesting YR b
        VISIBLE "Choose between 1-3: "
        GIMMEH b
        b IS NOW A NUMBR
        b
        WTF?
            OMG 1
                VISIBLE "1"
                SUM OF b AN 1
                WTF?
                    OMG 2
                        VISIBLE "2 (nested)"
                        GTFO
                    OMGWTF
                        VISIBLE "Not 2 (nested)"
                OIC
                GTFO
            OMG 2
                VISIBLE "2"
                SUM OF b AN 1
                WTF?
                    OMG 3
                        VISIBLE "3 (nested)"
                        GTFO
                    OMGWTF
                        VISIBLE "Not 3 (nested)"
                OIC
                GTFO
            OMG 3
                VISIBLE "3"
                SUM OF b AN 1
                WTF?
                    OMG 4
                        VISIBLE "4 (nested)"
                        GTFO
                    OMGWTF
                        VISIBLE "Not 4 (nested)"
                OIC
                GTFO
            OMGWTF
                VISIBLE "Neither 1, 2, nor 3"
        OIC
    IF U SAY SO

    HOW IZ I nested_return YR var1
        VISIBLE "INPUT VALUE: "
        GIMMEH var1
        var1 IS NOW A NUMBR
        BOTH SAEM var1 AN 4
        O RLY?
            YA RLY
                GTFO
            MEBBE BOTH SAEM var1 AN 5
                FOUND YR "var1 SAME AS 5"
        OIC

        VISIBLE "hello po"

    IF U SAY SO

    WAZZUP 
        BTW asdasdasdasdadas
        I HAS A x
        I HAS A y 
        I HAS A z ITZ 0
        I HAS A a ITZ 0
        I HAS A i ITZ 12
        I HAS A j ITZ 3
        I HAS A age 
        I HAS A choice
        I HAS A loop ITZ 0
        I HAS A b
    BUHBYE
    
    IM IN YR menu UPPIN YR loop TIL BOTH SAEM loop AN 5
        VISIBLE "---- MAIN MENU ----"
        VISIBLE "[1] Checker Board"
        VISIBLE "[2] Nested If Else"
        VISIBLE "[3] Nested Switch Case"
        VISIBLE "[4] Nested Return"
        VISIBLE "ENTER CHOICE: "
        GIMMEH choice
        choice IS NOW A NUMBR
        choice
        WTF?
            OMG 1
                I IZ is_even YR i AN YR j MKAY
                VISIBLE IT
                I IZ checker_board YR x AN YR y AN YR z AN YR a MKAY

                GTFO
            OMG 2
                VISIBLE "ENTER AGE: "
                GIMMEH age
                age IS NOW A NUMBR
                I IZ nested_if_else YR age MKAY
                GTFO
            OMG 3
                I IZ switch_nesting YR b MKAY
                GTFO
            OMG 4 
                I IZ nested_return YR b MKAY
                VISIBLE IT
                GTFO
            OMGWTF 
                VISIBLE "INVALID NUMBER"
	    OIC
    IM OUTTA YR menu


KTHXBYE