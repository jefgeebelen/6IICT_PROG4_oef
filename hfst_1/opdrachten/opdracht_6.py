# Open lied.txt in Python
lied = open("hfst_1/opdrachten/lied.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
# Test inhoud van lied

""" Begin eigen code hier """
dict_aantal = {}
woorden = lied.split()
for woord in woorden:
    if woord in dict_aantal:
        dict_aantal[woord] += 1
    else: 
        dict_aantal[woord] = 1
print(dict_aantal)
