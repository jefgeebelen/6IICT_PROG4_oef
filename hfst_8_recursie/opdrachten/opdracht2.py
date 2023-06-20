""" Schrijf een recursieve functie die controleert of een lijst geordend is. """
def geordend(getalen):
    if len(getalen) == 0 or len(getalen) == 1:
        return True
    if getalen[0] < getalen[1]:
        return geordend(getalen[1:])
    else:
        return False
print( geordend([1, 2, 3, 4]) ) # True
print( geordend([5, 2, 8, 4]) ) # False
print( geordend([9]) )          # True
print( geordend([0,1,2,4,3,5])) # False

def draaiom(woord):
    if len(woord) == 0:
        return
    if len(woord) == 1:
        return woord
    return woord[-1] + draaiom(woord[0:-1])