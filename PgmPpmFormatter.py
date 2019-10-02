import numpy as np
# import matplotlib.pyplot as plt

DarkRange = 50

def main():
    data = readpgm('Kit-Kat.pgm')
    writePGMFile(data)

def readpgm(fileName):
    with open(fileName) as pgmFile:
        allLines = pgmFile.readlines()
    
    assert allLines[0].strip() == 'P2' 

    #Ignoring Comments
    for str_line in list(allLines): #Turn Lines into a list and check for any string that starts with # and remove it
        if str_line[0] == '#':
            allLines.remove(str_line)

    #list
    data_list = []
    for line in allLines[1:]:
        data_list.extend([int(i) for i in line.split()])

    resultMulti = (np.array(data_list[3:]),(data_list[1],data_list[0]),data_list[2])

    return resultMulti

def writePGMFile(data):
    rangeNum = 255 / DarkRange
    count = 0
    newData = np.reshape(data[0],data[1]) #Reshape the list of numbers using the provided row and colums
    
    blackWhiteArray = np.copy(newData)
    darkerArray = np.copy(newData)
    brighterArray = np.copy(newData)
    tdCopy = np.copy(newData)
    lrCopy = np.copy(newData)

    #Create New PGM files - Inverted Black and White, Left Right, Top Bottom, Bright and Dark.
    ########################################################################
    print "Inverting Black and White - PGM..............\n"
    blkWhtFile = open("BlackWhite_Invert-Kat.pgm","w")
    blkWhtFile.write("P2\n")
    blkWhtFile.write("1770 1170\n")
    blkWhtFile.write("255\n")
    for x in np.nditer(blackWhiteArray, op_flags = ['readwrite']):
        x[...] =  255 - x

    np.savetxt(blkWhtFile, blackWhiteArray, fmt="%s")  
    ########################################################################
    
    print "Reflecting Left to Right - PGM..............\n"
    ltRtFile = open("LeftRight-Kat.pgm","w")
    ltRtFile.write("P2\n")
    ltRtFile.write("1770 1170\n")
    ltRtFile.write("255\n")
    leftRightReverse = lrCopy[::, ::-1]

    np.savetxt(ltRtFile, leftRightReverse, fmt="%s")  
    ########################################################################

    print "Reflecting Top to Bottom - PGM..............\n"
    tdBtFile = open("TopBottom-Kat.pgm","w")
    tdBtFile.write("P2\n")
    tdBtFile.write("1770 1170\n")
    tdBtFile.write("255\n")
    topDownReverse = tdCopy[::-1]

    np.savetxt(tdBtFile, topDownReverse, fmt="%s")  
    ########################################################################

    print "Increasing Brightness of Image - PGM..............\n"
    brightFile = open("Bright-Kat.pgm","w")
    brightFile.write("P2\n")
    brightFile.write("1770 1170\n")
    brightFile.write("400\n")
    for x in np.nditer(brighterArray, op_flags = ['readwrite']):
        x[...] =  (x + 150)

    np.savetxt(brightFile, brighterArray, fmt="%s")  
    ########################################################################

    print "Darkening Image - PGM..............\n"
    darkFile = open("Darken-Kat.pgm","w")
    darkFile.write("P2\n")
    darkFile.write("1770 1170\n")
    darkFile.write("255\n")
    for x in np.nditer(darkerArray, op_flags = ['readwrite']):
        x[...] =  (x / rangeNum)

    np.savetxt(darkFile, darkerArray, fmt="%s")  
    ########################################################################

if __name__== "__main__":
    main()
