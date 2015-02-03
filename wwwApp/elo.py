# import math


def cal(Ra, Rb, W, k=20, r=3):
    '''
    PASSED IN VARS
    ---------------------------------------------------------------------------
    pas = Player A score
    pbs = Player B score
    paw = Player A win score: 1 = win (Player B lost)
                              0 = loss(Player A lost)
                              0.5 = Draw(The game was a draw)
    k   = The weight of the game
            (40,30,20,15,10)

    r   = number of decimal places to round to.
    VARS USED INTERNALLY
    ---------------------------------------------------------------------------
    pbw = Players B win score allways = paw - 1 if 0.5 it is positive
    ea  = probially A will win
    eb  = probially B will win

    ra  = New score for A
    rb  = New score for B

    qa  = used for mid cal
    qb  =    "
    qab =    "
    '''
    Ea = 1 / (1 + (10 ** ((Rb - Ra) / 400)))
    Eb = 1 / (1 + (10 ** ((Ra - Rb) / 400)))

    Sa = W
    Sb = 1 - Sa

    RaP = Ra + (k * (Sa - Ea))
    RbP = Rb + (k * (Sb - Eb))

    return (round(RaP, r), round(RbP, r))


def est(Ra, Rb):
    Ea = 1 / (1 + (10 ** ((Rb - Ra) / 400)))
    Eb = 1 / (1 + (10 ** ((Ra - Rb) / 400)))
    return (round((Ea * 100), 3), round((Eb * 100), 3))
