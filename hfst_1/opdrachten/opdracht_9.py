""" Niveau 1 """
puntenlijst = [
    ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], # 1 punt
    ["D", "G"],                                         # 2 punten
    ["B", "C", "M", "P"],                               # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    ["K"],                                              # 5 punten
    ["J", "X"],                                         # 6 punten
    ["Q","Z"]                                           # 7 punten
]
dict_aantal1 = {}
for index, list1 in enumerate(puntenlijst):
    for leter in list1:
        dict_aantal1[leter] = index+1
sorted(dict_aantal1.keys())
print(dict_aantal1)
""" Niveau 2"""
puntenlijst_en = [
    ["A", "E", "I", "O", "U", "L", "N", "S", "T"],      # 1 punt
    ["D", "G", "K"],                                    # 2 punten
    ["B", "M", "P", "Q", "R"],                          # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    [],                                                 # 5 punten
    ["J", "X"],                                         # 6 punten
    ["C","Z"]                                           # 7 punten
]
dict_aantal2 = {}
for index, list2 in enumerate(puntenlijst_en):
    for leter in list2:
        dict_aantal2[leter] = index+1
sorted(dict_aantal2.keys())
print(dict_aantal2)
""" Niveau 3"""
woord = input("voer een woord in")
letters = list(woord)
punten = 0
for lijst, index in dict_aantal2.items():
    for i in lijst:
        if letters == i:
            punten += index
print(punten)

