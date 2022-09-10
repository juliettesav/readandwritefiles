import csv

infile1 = open('EmployeePay.csv','r')

csvfile1 = csv.reader(infile1,delimiter=',')

next(csvfile1) #to skip the header

for record in csvfile1: 
    print()
    print('First Name:',record[1])
    print('Last Name:',record[2])
    #record[3]
    #record[4]
    bonus = int(record[3])*float(record[4])
    print("Original Pay: ", record[3])
    print("Bonus Pay: ",bonus)
    print("Total Pay: ",bonus+int(record[3]))

    input()
