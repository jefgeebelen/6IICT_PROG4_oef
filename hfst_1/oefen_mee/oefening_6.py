engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

""" eerste methoden """

vertaal = []
key_value_dict = list(engels_nederlands.items())
print(key_value_dict)
zin = input()
woorden = zin.split()

for woord in woorden:
    for key,value in key_value_dict:
        if woord == value:
            vertaal.append(key)

vertaalde_zin = " ".join(vertaal)
print(vertaalde_zin)

""" een andere manier """

vertalde_zin = ""
zin = input("Geef een zin in het nederland: ")
woorden = zin.split()
for woord in woorden:
    if woord in engels_nederlands.values():
        vertalde_zin += f"{(list(engels_nederlands.keys())[list(engels_nederlands.values()).index(woord)])} "
print(vertalde_zin)

