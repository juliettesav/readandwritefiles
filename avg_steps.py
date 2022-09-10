import csv

infile2 = open('steps.csv','r')
outfile2 = open('avg_steps.csv','w')

csvfile2 = csv.reader(infile2,delimiter=',')

next(csvfile2) #to skip the header

months = ['null','January','February','March','April','May','June','July','August','September','October','November','December']
####

with open('steps.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    count = 0
    fsa = []
    for row in reader:
        count = count + 1
        fsa.append(int(row['Steps']))
        if count > 31:
            break
avg_fsa = str((sum(fsa))/len(fsa))
print("January,",avg_fsa)
outfile2.write('January'+', '+avg_fsa+'\n')


###
#for record in csvfile2: 

#    monthrecord=int(record[0])
#    XXX avg = record[1] #find the avg here
#    print(months[monthrecord],',',avg)
#    outfile2.write(months[monthrecord]+', '+avg+'\n')

outfile2.close()