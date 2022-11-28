import csv 

 

fp = open( "nieuwe_csv.csv", "w", newline="") 

 

csv_writer = csv.writer( fp , delimiter=";") 

csv_writer.writerow( ["FILM", "SCORE"] ) 

csv_writer.writerow( ["Monty Python and the Holy Grail", 8] ) 

csv_writer.writerow( ["Monty Python's Life of Brian", 8.5] ) 

csv_writer.writerow( ["kabouter plop", 10] ) 

 

fp.close() # Na sluiten is CSV niet meer bruikbaar 

fp = open( "nieuwe_csv.csv", "r") 
lezer = csv.reader(fp, delimiter=";")

print(list(lezer))