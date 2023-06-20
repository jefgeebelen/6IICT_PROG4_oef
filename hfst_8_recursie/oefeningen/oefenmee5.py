""" Niveau 1: los sommatie recursief op """
def draaiom(woord):
    if len(woord) == 0:
        return
    if len(woord) == 1:
        return woord
    return woord[-1] + draaiom(woord[0:-1])

print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI

""" Niveau 2: los sommatie met while-loops op """