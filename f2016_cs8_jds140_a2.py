#name       : John Dale Shoemaker
# email      : jds140@pitt.edu
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)

# need this for the remove and rename functions so says the book
import os.path
# need this to define length of key
key_length = 30
# first, need to define printKV function
def printKV(key,value,klen = 0):
    klen = max(klen,len(key));
    #here we gotta check the type of vaiable we'll get
    if isinstance(value,str):
        fvalue = '20s'
    elif isinstance(value,float):
        fvalue = '10.3f'
    elif isinstance(value,int):
        fvalue = '10d'
    else:
        value = str(value)
        fvalue = '20s'
    print(format(key,'>'+str(klen)+'s'),' : ',format(value,fvalue))
def processFile(fh):
    # now we need to define the processFile function. this should count how many lines the files has and sum the distance that is the second field of each line
    partialtotaldistance = 0
    # partial total number of lines
    partialtotalnumberlines = 0
    for line in fh:
        [name, distance] = line.rstrip('\n').split(',')
        # gotta convert distance from string to float
        distance = float(distance)
        # print name and distance in this record properly formatted
        printKV('Name', name, key_length)
        printKV('Distance', distance, key_length)
        partialtotaldistance += distance
        # partial total number of lines
        partialtotalnumberlines += 1
    return [partialtotalnumberlines, partialtotaldistance]
#end of this part
# do partial totals
totaldistance = 0
totalnumberlines = 0
numberoffiles = 0
#okay now ask the user for the first file
print('Please enter the name of the first file to process.')
file = input('File name : ')
# check if file name is empty, or is q or quit and also if
while ( file != '' and file != 'quit' and file != 'q' and os.path.exists(file) ):
# open the file in read mode and creates the file object
    fh = open(file, 'r')
    # okay need to process the file and get the number of lines and the sum of the distances
    partialtotalnumberlines, partialtotaldistance = processFile(fh)
    # shut this file on down
    fh.close()
#time to print the partials out
    print('')
    printKV('Partial Names found', partialtotalnumberlines, key_length)
    printKV('Partial Distance', partialtotaldistance, key_length)
    print('')
    numberoffiles += 1
    totaldistance += partialtotaldistance
    totalnumberlines += partialtotalnumberlines
    # need to ask user the next file
    print('Please enter the name of the second file you want to process. Type nothing or q/quit to exit')
    file = input('File name : ')
# time to print this stuff
print('')
printKV('Files read', numberoffiles, key_length)
printKV('Total Distance', totaldistance, key_length)
printKV('Names found', totalnumberlines, key_length)
print('')
