HAI
    WAZZUP
        BTW variable dec
        I HAS A x
        I HAS A y
    BUHBYE

    VISIBLE "x:" + WIN + ", y:" + WIN
    x R WIN
    y R WIN

    VISIBLE BOTH OF x AN y BTW TRUE
    VISIBLE EITHER OF x AN y BTW TRUE
    VISIBLE WON OF x AN y BTW TRUE AND NOT TRUE EDI FALSE
    VISIBLE NOT x BTW FALSE
    VISIBLE ALL OF x AN x AN x AN y MKAY BTW TRUE
    VISIBLE ANY OF y AN y AN y AN 0 MKAY BTW TRUE
    VISIBLE ANY OF BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y MKAY BTW X AND (~X OR Y) OR Y OR ~Y EDI TRUE
    VISIBLE BOTH OF x AN EITHER OF NOT x AN y BTW X AND (~X OR Y) EDI TRUE

    VISIBLE "x:" + FAIL + ", y:" + WIN
    x R FAIL

    VISIBLE BOTH OF x AN y BTW FALSE
    VISIBLE EITHER OF x AN y BTW TRUE
    VISIBLE WON OF x AN y BTW TRUE AND NOT FALSE EDI TRUE 
    VISIBLE NOT x BTW TRUE
    VISIBLE ALL OF x AN x AN x AN y MKAY BTW FALSE
    VISIBLE ANY OF y AN y AN y AN 0 MKAY BTW TRUE
    VISIBLE ANY OF BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y MKAY BTW X AND (~X OR Y) OR Y OR ~Y EDI TRUE
    VISIBLE BOTH OF x AN EITHER OF NOT x AN y BTW X AND (~X OR Y) EDI FALSE

    VISIBLE "x:" + FAIL + ", y:" + FAIL
    y R FAIL

    VISIBLE BOTH OF x AN y BTW FALSE
    VISIBLE EITHER OF x AN y BTW FALSE
    VISIBLE WON OF x AN y BTW FALSE AND NOT TRUE EDI FALSE
    VISIBLE NOT x BTW TRUE
    VISIBLE ALL OF x AN x AN x AN y MKAY BTW FALSE
    VISIBLE ANY OF y AN y AN y AN 0 MKAY BTW FALSE
    VISIBLE ANY OF BOTH OF x AN EITHER OF NOT x AN y AN y AN NOT y MKAY BTW X AND (~X OR Y) OR Y OR ~Y EDI TRUE KASI ~Y AY NAGING TRUE
    VISIBLE BOTH OF x AN EITHER OF NOT x AN y BTW X AND (~X OR Y) EDI FALSE
KTHXBYE