# modules importeren
import json                       # voor lexicon
import string                     # voor opsomming leestekens  
# lexicon inlezen. Zorg dat het pad correct is (hoofdmap is hfst_5_AI)!
with open("lexicondict.json", "rb") as file: # bestand lexicondict.json in map data bevat het sentimentlexicon
    lexicon = json.load(file)