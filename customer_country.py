import csv 

def main():
    outfile = open('customer_country.csv','w')
    outfile.write(record[1],record[2],record[4])

    csvfile = csv.reader(infile,delimiter=',')
    next(csvfile) #to skip the header

    for record in csvfile: 
        outfile.write(record[1],record[2],record[4])

    outfile.close()

main()