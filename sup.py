import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile) #to skip the header

for record in csvfile: 
    outfile = open('customers_country.csv','w')
    name=record[1]+' '+record[2]
    country=record[4]
    list=[name,country]
    print(list)
    with open('customers_country.csv', 'w') as x:
        wr = csv.writer(x)
        wr.writerows(list)
    #outfile.write(name)
    #outfile.write(country)


    outfile.close()