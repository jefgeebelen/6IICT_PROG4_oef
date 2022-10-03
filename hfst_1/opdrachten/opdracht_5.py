poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Pieter", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Pieter": "c",    
    "Joris": "ruby"}
# for i in poll_talen:
#     if i in favorite_languages:
#         print("bedankt voor u deelnamen")
#     else:
#         print("zouw u willen deelenemen")

for i in poll_talen:
    if i in favorite_languages:
        print("bedankt voor u deelnamen")
    else:
        print("zouw u willen deelenemen")
        nieuwe = input("vul in")
        if nieuwe == "":
            print("jammer")
        else:
            print("danku")
            favorite_languages[i] = nieuwe
print(favorite_languages)