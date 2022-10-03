lijst_lijst = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10]
]

for lijst in lijst_lijst:
    for element in lijst:
        print(element)

lijst_dict = [
    {'foo':12, 'bar':14 },
    {'moo':52, 'car':641},
    {'doo':6 , 'tar':84, 'var':38 }
]

for dict in lijst_dict:
    for key, value in dict.items():
        print(f"{key}\n{value}")

dict_dict = {
    1: {'naam': 'John',  'leeftijd': 27, 'geslacht': 'Man'},
    2: {'naam': 'Marie', 'leeftijd': 22, 'geslacht': 'Vrouw'},
    3: {'naam': 'Kurt',  'leeftijd': 23}
}
for key, dict in dict_dict.items():
    print(key)
    for key, value in dict.items():
        print(f"{key}\n{value}")
