""" (  / 5)
Bepaal recursief of een string een palindroom is.
De functie returnt True als het woord een palindroom is, False indien niet zo.

Een palindroom is een woord waarvan de letters symmetrisch gerangschikt zijn.
Het woord is van achter naar voor, identiek als van voor naar achter.
(VB. negen <--> negen )

Tip: controleer of de eerste & laatste letter van het woord gelijk zijn.
        Zo nee, dan is het geen palindroom.
        Zo ja, verwijder de eerste & laatste letter van het woord.  
               Controleer of de nieuwe eerste & laatste letter gelijk zijn.
                    Zo nee, dan is het geen palindroom
                    Zo ja , verwijder de eerste & laatste letter van het woord.
                            ... 

     Bepaal zelf wanneer dit proces moet stoppen.
"""
def bepaal_palindroom(woord):
    if len(woord) == 0 or len(woord) == 1:
        return True
    if woord[0] == woord[-1]:
        return bepaal_palindroom(woord[1:-1])
    else:
        return False

# Hier enkele voorbeelden om te testen.
print( bepaal_palindroom("woord") ) # False
print( bepaal_palindroom("hah") )   # True
print( bepaal_palindroom("daad") )  # True
print( bepaal_palindroom("dadel") ) # False
print( bepaal_palindroom("o"))      # True
print( bepaal_palindroom(""))       # True