""" Niveau 1 & 2
Wat gaat hier mis?
"""
try:
    fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )
    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except ValueError:
    print("je kan aleen maar cijfes invoeren")
except IndexError:
    print("er zijn niet meer fruitsoorten")
except:
    print("er ging iets algemeen mis")



""" Niveau 3 (haal uit commentaar) """
# while True:
#     fruit = input("Element aan lijst toevoegen: ")
    
#     if fruit == "":
#         break # Loop stopt wanneer gebruiker een lege string ingeeft.
#     else:
#         fruit_lijst.append(fruit)

# print(fruit_lijst)
