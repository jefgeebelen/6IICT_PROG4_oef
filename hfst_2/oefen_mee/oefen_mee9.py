import json

fp = open("hfst_2/oefen_mee/oefen_mee9.json", "r")
quiz = json.load(fp)
fp.close()

for key, onderwerp in quiz["quiz"].items():
    for key2, vraag in onderwerp.items():
        print(vraag["vraag"])
        print("kies uit:")
        for antwoorden in vraag["opties"]:
            print(antwoorden)
        antwoord = input("geef het juiste antwoord:")
        if antwoord == vraag["antwoord"]:
            print("juist")
        