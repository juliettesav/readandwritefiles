infile = open('clients.txt','r')
num = 1
for line in infile:
    print(num,'. ',line.rstrip('\n'),sep='')
    #REMOVE \n SPACE print(str(num),'. ',line)
    num+=1