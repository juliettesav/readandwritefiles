def main():
    infile = open('philosophers.txt','r')
 
    file_contents = infile.read()
    #line1=infile.readline()
    #line2=infile.readline()
    #line3=infile.readline()
    #line4=infile.readline()

    print(file_contents) 
    #print(line1.rstrip('\n'))
    #print(line2.rstrip('\n'))
    #print(line3.rstrip('\n'))
    #print(line4.rstrip('\n'))

main()