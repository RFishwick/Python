# Search for Words in a String

import WordFinder

# Begin Main Program

fileI = open('theMessage.txt', 'r')  # Open Input file for reading
my_text = list(fileI)  # Read file into string myText
fileI.close()  # Close input file

# Print lines that contain the selected word
lineCnt = 0
for line in my_text:
    lineCnt += 1
    theResult = WordFinder.find_word(line)
    if theResult != None: # Word Found
        output = '\'{}\' found on line {}:\n{}\n'.format(theResult.title(), lineCnt, line.strip())