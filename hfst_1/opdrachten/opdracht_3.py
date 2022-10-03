""" Niveau 1"""
# dict_1={1: 10, 2: 20}
# dict_2={3: 30, 4: 40}
# dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# dict_verzameling = {}
# for key, value in dict_1.items():
#     dict_verzameling[key] = value
# for key, value in dict_2.items():
#     dict_verzameling[key] = value
# for key, value in dict_3.items():
#     dict_verzameling[key] = value
# print(dict_verzameling)
""" Niveau 2 """
dict = {'a': 'Red', 'b': 'Green', 'c': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}
del dict['c']
print(dict)
""" Niveau 3 """
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})
dict_samen = {}
for key, value in dict_1.items():
    dict_samen[key] = value 
print(dict_samen)
for key1, value1 in dict_2.items():
    if key1 in dict_samen:
        dict_samen[key1] += value1
    else:
        dict_samen[key1] = value1
print(dict_samen)


