""" Niveau 1 """
dict = {
    "belgie": {
        "provincie": {
            "naam": "limburg",
            "weetjes": {
                "oppervlakte":  2.422,
                "inwoners": 885.951,
                "gouverneur": "Jos Lantmeeters"
            }
        }
    }
}
dict["belgie"]["provincie"]["info"] = dict["belgie"]["provincie"].pop("weetjes")
print(dict)

""" Niveau 2 """
extra_info = [  ["mannen", 49.77], 
                ["vrouwen", 50.23], 
                ["hoofdstad", "hasselt"] ]
for lijst in extra_info:
    dict["belgie"]["provincie"]["info"][lijst[0]] = lijst[1]
print(dict)