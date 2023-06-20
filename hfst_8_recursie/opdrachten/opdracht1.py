""" Los de reeks van Fibonacci recursief op. """
def fib(getal):
    if getal == 1:
        return 1
    if getal == 2:
        return 1
    return fib(getal-1) + fib(getal-2)
    
print( fib(2) )     # 1
print( fib(4) )     # 3
print( fib(10) )    # 55
print( fib(25) )    # 75025