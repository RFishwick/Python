# Search for Words in a String

# Define the words to search for the tuple searchWords
searchWords = ("c++", "basic", "java", "python")


# Define Functions
def findWord(iLine):  # Function to find a word within a string
    """Return first word in sentence matching a word in the searchWords tuple"""

    result = -1  # Pre-set result to -1 in case loop falls through
    try:
        iLine = iLine.lower()  # Convert string to lower case for searching

        # Loop through words in seachWords and try to find in string s
        for searchWord in searchWords:
            position = iLine.find(searchWord)  # Get postion of word in iLine
            if position != -1:
                result = searchWord  # Set result to value of found searchWord
                break

        # -1 will be returned if no search words found in string iLine
        return result

    except:
        # Fall through on any error
        return None


# Begin Main Program

fileI = open('theMessage.txt', 'r')  # Open Input file for reading
myText = list(fileI)  # Read file into string myText
fileI.close()  # Close input file

# Print lines that contain the selected word
lineCnt = 0
for line in myText:
    lineCnt += 1
    theResult = findWord(line)
    if theResult != -1: # Word Found
        output = '\'{}\' found on line {}:\n{}\n'.format(theResult, lineCnt, line.strip())
        print(output)

