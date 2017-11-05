# Search for Words in a String

import WordFinder

# Begin Main Program

fileI = open('theMessage.txt', 'r')  # Open Input file for reading
myText = list(fileI)  # Read file into string myText
fileI.close()  # Close input file

# Print lines that contain the selected word
lineCnt = 0
for line in myText:
    lineCnt += 1
    theResult = WordFinder.findWord(line)
    if theResult != None: # Word Found
        output = '\'{}\' found on line {}:\n{}\n'.format(theResult.title(), lineCnt, line.strip())
        print(output)
