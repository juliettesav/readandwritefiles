import csv

infile = open('customers.csv','r')
outfile = open('customers_country.csv','w')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile) #to skip the header
outfile.write("Name, Country"+'\n')

for record in csvfile: 
    
    name=record[1]+' '+record[2]
    country=record[4]
    list=[name,country]
    print(list)
    outfile.write(name+', '+country+'\n')

outfile.close()