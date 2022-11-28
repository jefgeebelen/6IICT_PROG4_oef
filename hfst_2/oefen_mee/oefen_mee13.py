import json 
fp = open("C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee13.json", "r") 
lijst = json.load(fp) 
fp.close()  
last_cases = 0
for dict in lijst:
    if last_cases == 0:
        current_case = 0
    else:
        current_case = dict['Cases']
    new_cases = current_case - last_cases
    print(f"{dict['Date']} waren er {new_cases} nieuwe coronagevallen")
    last_cases = dict["Cases"]
    fp = open("C:/Users/GEJE051205/Documents/programeren/6IICT_PROG4_oef/hfst_2/oefen_mee/oefen_mee13.json", "w")
    dict["New Cases"] = new_cases
    json.dump(lijst, fp)