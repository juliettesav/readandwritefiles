import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile) #to skip the header
#outfile.write('John Locke\nDavid Hume\nEdmund Burke\n')

#outfile = open('customer_country.csv','w') #added

for record in csvfile: 
    #print(record[1],record[2],',',record[4])
    name=(record[1],record[2])
    country=(record[4])
    input()
    #outfile.write('')
    #outfile.write(name)