import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile) #to skip the header
outfile = open('philosophers.txt','w')
for record in csvfile: 
    x=(record[1]+' '+record[2],record[4])
    outfile.write(x)
    #print(x)
    input()
    outfile.close()